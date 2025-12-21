from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QTextEdit, QHBoxLayout, QDialog, QPushButton, QCheckBox, QStackedLayout
from data_objects.question import Question
from dtos.question_dto import QuestionType


class QuestionEditor(QDialog):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)

        layout = QVBoxLayout()
        exercise, self.exercise_editor = self.__exercise_constructor()
        selector, self.question_type_selector = self.__question_type_selector()
        self.question_type: QuestionType = QuestionType.normal 
        self.editor_container = QWidget()
        self.normal_editor = self.__back_constructor(QuestionType.normal)
        self.true_false_editor = self.__back_constructor(QuestionType.true_false)
        self.combo_box_editor = self.__back_constructor(QuestionType.combo_box)

        print("1___")
        self.editor_container.setLayout(QStackedLayout())
        print("2___")
        self.editor_container.layout().addWidget(self.normal_editor)
        self.editor_container.layout().addWidget(self.true_false_editor)
        self.editor_container.layout().children()
        #self.editor_container.layout().addWidget(self.combo_box_editor)
        print("3___")

        self.button_menu = self.__button_menu()
        self.created_question: Question|None = None

        print("___")
        self.__question_type_updator(self.question_type)
        print("___")

        layout.addWidget(exercise)
        layout.addWidget(selector)
        layout.addWidget(self.editor_container)
        layout.addLayout(self.button_menu)

        self.setLayout(layout)
 
    def __get_question(self):
        return
        
    def __close (self, accept: bool):
        if accept:
            self.created_question = self.__get_question()
            self.accept()
        else:
            self.created_question = None
            self.reject()
        return

    def __button_menu(self):
        layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        ok_button.clicked.connect(lambda : self.__close(True))
        cancel_button.clicked.connect(lambda : self.__close(False))

        return layout

    def __exercise_constructor(self):
        result = QWidget()
        layout = QVBoxLayout()
        question_label = QLabel("Question:")
        question_exercise = QTextEdit()
        layout.addWidget(question_label)
        layout.addWidget(question_exercise)
        result.setLayout(layout)
        return (result, question_exercise)


    def __question_type_selector(self):
        result = QWidget()
        layout = QHBoxLayout()
        label = QLabel("Question Type:")
        question_type_selector = QComboBox()
        question_types: list[str] = [e.value for e in list(QuestionType)]
        question_type_selector.addItems(question_types)
        print("LOOOK: ", [question_type_selector.itemText(i) for i in range(question_type_selector.count())])
        layout.addWidget(label)
        layout.addWidget(question_type_selector)
        result.setLayout(layout)
        question_type_selector.setCurrentIndex(question_types.index(QuestionType.normal.value))

        question_type_selector.currentIndexChanged.connect(lambda : self.__question_type_updator(QuestionType(self.question_type_selector.currentText())))
        return (result, question_type_selector)
    
    def __back_constructor(self, question_type):
        match question_type:
            case QuestionType.normal:
                layout = QVBoxLayout()
                label = QLabel("Answer (Normal)")
                editbox = QTextEdit()
                layout.addWidget(label)
                layout.addWidget(editbox)
                w = QWidget()
                w.setLayout(layout)
                return w
                
            case QuestionType.true_false:
                super_layout = QVBoxLayout()
                layout = QVBoxLayout()
                option_edit = QTextEdit()
                Option_checkbox = QCheckBox()
                option_layout = QHBoxLayout()
                option_layout.addWidget(option_edit)
                option_layout.addWidget(Option_checkbox)
                layout.addLayout(option_layout)
                super_layout.addLayout(layout)

                add_option = QPushButton("+")
                add_option.clicked.connect(lambda : self.add_option() )
                super_layout.addWidget(add_option)
                
                w = QWidget()
                w.setLayout(super_layout)
                return w

            case QuestionType.combo_box:
                pass
            case _:
                Exception(f"Unrecognized question_type {question_type}")

    def add_option(self):
        # Hay que hacer las opciones un scrollable area
        layout = self.true_false_editor.layout().children()[0]
        option_edit = QTextEdit()
        Option_checkbox = QCheckBox()
        option_layout = QHBoxLayout()
        option_layout.addWidget(option_edit)
        option_layout.addWidget(Option_checkbox)
        layout.addLayout(option_layout)



    def __question_type_updator(self, value: QuestionType):
        self.question_type = value
        print(f"Changing type to {self.question_type.value}")
        match self.question_type:
            case QuestionType.normal:
                self.editor_container.layout().setCurrentIndex(0)
            case QuestionType.true_false:
                print(self.editor_container.layout().children())
                self.editor_container.layout().setCurrentIndex(1)
            case QuestionType.combo_box:
                return
                self.editor_container.setLayout(self.combo_box_editor)
            case _:
                Exception(f"Unrecognized question_type {self.question_type}")
        

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    test = QuestionEditor(None)
    test.show()


