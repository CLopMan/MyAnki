from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QButtonGroup
from data_objects.normal_question import NormalQuestion
from gui.question_widget import QuestionWidget


class NormalQuestionWidget(QuestionWidget):
    def __init__(self, question: NormalQuestion):
        super().__init__(question)
        self.data: NormalQuestion = question # not necesary. Added for typehinting in the editor
       

    def show_answer(self):
        self.answer.setVisible(True)

    def create_answer(self):
        answer = QWidget()
        answer_layout = QVBoxLayout()
        answer_text = QLabel(self.data.right_answer)
        answer_layout.addWidget(answer_text)

        self.button_widget = self.create_button_widget()

        answer_layout.addWidget(self.button_widget)

        answer.setVisible(False)
        no_resize = answer.sizePolicy()
        no_resize.setRetainSizeWhenHidden(True)
        answer.setSizePolicy(no_resize)
        answer_text.setWordWrap(True)
        answer.setLayout(answer_layout)
        return answer

    def create_button_widget(self) -> QWidget:
        button_widget = QWidget();
        
        button_layout = QHBoxLayout()
        bad_button = QPushButton("BAD")
        bad_button.clicked.connect(self.set_wrong)
        good_button = QPushButton("GOOD")
        good_button.clicked.connect(self.set_correct)

        for b in (bad_button, good_button):
            b.setCheckable(True)
            b.setStyleSheet(
"""
                QPushButton {
                    background-color: #dddddd;
                    border: 2px solid #888;
                    padding: 8px;
                    border-radius: 6px;
                }
                QPushButton:checked {
                    background-color: #4472c4;
                    color: white;
                    border: 2px solid #2f5597;
                }
            """
            )

        button_group = QButtonGroup(self)
        button_group.setExclusive(True)
        button_group.addButton(bad_button)
        button_group.addButton(good_button)

        button_layout.addWidget(bad_button)
        button_layout.addWidget(good_button)

        button_widget.setLayout(button_layout)

        return button_widget

