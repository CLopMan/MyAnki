from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from data_objects.question import Question
from dtos.question_dto import QuestionType
from data_objects.normal_question import NormalQuestion
from data_objects.true_false_question import TrueFalseQuestion
from abc import abstractmethod


class QuestionForm(QDialog):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)
        # selector
        self.selector = self.build_selector()
        
        #editor
        self.normal_editor: NormalQuestionEditor = NormalQuestionEditor(self)
        self.true_false_editor: TrueFalseEditor = TrueFalseEditor(self)

        self.editor: QWidget = QWidget()
        self.editor_layout: QStackedLayout = QStackedLayout()
        self.editor_layout.addWidget(self.normal_editor)
        self.editor_layout.addWidget(self.true_false_editor)
        self.editor.setLayout(self.editor_layout)

        # Button menu
        self.accept_menu = self.__button_menu()


        layout = QVBoxLayout()
        layout.addWidget(self.selector)
        layout.addWidget(self.editor)
        layout.addWidget(self.accept_menu)
        self.setLayout(layout)

    def __close (self, accept: bool):
        if accept:
            print(self.editor_layout.currentWidget().get_question())
            self.accept()
        else:
            self.reject()
        return

    def __button_menu(self):
        w = QWidget()
        layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        ok_button.clicked.connect(lambda : self.__close(True))
        cancel_button.clicked.connect(lambda : self.__close(False))
        w.setLayout(layout)
        return w

    def __question_type_updator(self, value: QuestionType):
        self.question_type = value
        print(f"Changing type to {self.question_type.value}")
        match self.question_type:
            case QuestionType.normal:
                self.editor_layout.setCurrentIndex(0)
            case QuestionType.true_false:
                self.editor_layout.setCurrentIndex(1)
            case _:
                Exception(f"Unrecognized question_type {self.question_type}")

    def build_selector(self):
        result = QWidget()
        layout = QHBoxLayout()
        label = QLabel("Question Type:")
        self.question_type_selector = QComboBox()
        question_types: list[str] = [e.value for e in list(QuestionType)]
        self.question_type_selector.addItems(question_types)
        layout.addWidget(label)
        layout.addWidget(self.question_type_selector)
        result.setLayout(layout)
        self.question_type_selector.setCurrentIndex(question_types.index(QuestionType.normal.value))

        self.question_type_selector.currentIndexChanged.connect(lambda : self.__question_type_updator(QuestionType(self.question_type_selector.currentText())))
        return result

    def get_question(self) -> Question:
        raise NotImplemented


class QuestionEditor(QWidget):

    @abstractmethod
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)

    @abstractmethod
    def get_question(self) -> Question:
        return NotImplemented

    def build_tag_frame(self, editor: QWidget):
        layout = QVBoxLayout()
        title = QLabel("New Question")
        self.tags_label = QLabel("Tags (separated by ';'):")

        self.tags_string = QTextEdit()
        self.tags_string.setFixedHeight(128)
        layout.addWidget(title)
        layout.addWidget(editor)
        layout.addWidget(self.tags_label)
        layout.addWidget(self.tags_string)
        self.setLayout(layout)

    def parse_tags(self, tags: str):
        return [tag.strip() for tag in tags.split(';')]

class NormalQuestionEditor(QuestionEditor):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)

        self.label_question = QLabel("Question (Normal)")
        self.exercise = QTextEdit()
        self.label_answer = QLabel("Answer (Normal)")
        self.answer = QTextEdit()
        layout = QVBoxLayout()
        for x in (self.label_question, self.exercise, self.label_answer, self.answer):
            layout.addWidget(x)
        w = QWidget()
        w.setLayout(layout)
        self.build_tag_frame(w)

    def get_question(self) -> NormalQuestion:
        return NormalQuestion(self.exercise.toPlainText(),
                              self.parse_tags(self.tags_string.toPlainText()),
                              self.answer.toPlainText(), None
                              )

class OptionWidget(QWidget):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)
        layout = QHBoxLayout()
        layoutV = QVBoxLayout()

        self.option = QTextEdit()
        self.checkbox = QCheckBox()

        layoutV.addWidget(QLabel("True?"))
        layoutV.addWidget(self.checkbox)

        layout.addWidget(self.option)
        layout.addLayout(layoutV)
        self.setLayout(layout)

    def get_option(self) -> tuple[str, bool]:
        return (self.option.toPlainText(), self.checkbox.isChecked())

class OptionList(QScrollArea):
    def __init__(self, parent: QWidget, items: list[OptionWidget]|None = None):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        if items is None:
            self.items = []
        else:
            self.items = items

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        container = QWidget()
        self.setWidget(container)
        for opt in self.items:
            layout.addWidget(opt)
        container.setLayout(layout)

    def add_option(self, option: OptionWidget):
        self.widget().layout().addWidget(option)

    def remove_option(self, index):
        raise NotImplemented

    def get_options(self):
        return [opt.get_option() for opt in self.items]


class TrueFalseEditor(QuestionEditor):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)


        self.options: OptionList = OptionList(self)
        self.label_question = QLabel("Question (True-False)")
        self.exercise = QTextEdit()
        self.label_answer = QLabel("Answer (True-False)")
        self.answer = self.build_options()
        layout = QVBoxLayout()
        for x in (self.label_question, self.exercise, self.label_answer, self.answer):
            layout.addWidget(x)
        w = QWidget()
        w.setLayout(layout)
        self.build_tag_frame(w)

    def add_option(self):
        self.options.add_option(OptionWidget(None))

    def build_options(self):
        layout = QVBoxLayout()
        add_opt = QPushButton("+")
        add_opt.clicked.connect(self.add_option)
        layout.addWidget(self.options)
        layout.addWidget(add_opt)
        w = QWidget()
        w.setLayout(layout)
        return w


    def get_question(self) -> TrueFalseQuestion:
        return NotImplemented
