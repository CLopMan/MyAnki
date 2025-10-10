from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from data_objects.normal_question import NormalQuestion
from gui.question_widget import QuestionWidget

class NormalQuestionWidget(QuestionWidget):
    def __init__(self, question: NormalQuestion):
        super().__init__(question)
        self.data: NormalQuestion = question
        self.answer: QLabel = self.create_answer()
        self.exercise: QLabel = self.create_exercise()
        self.show_button: QPushButton = QPushButton("SHOW ANSWER")

        layout = QVBoxLayout()
        layout.addWidget(self.exercise)
        layout.addWidget(self.answer)
        layout.addWidget(self.show_button)
        self.show_button.clicked.connect(self.show_answer)


        self.setLayout(layout)
        #self.setStyleSheet("border: 1px solid red")

    def create_exercise(self) -> QLabel:
        result = QLabel(self.data.question)
        result.setFont(QFont('Arial', 16))
        result.setMaximumHeight(60)
        return result

    def show_answer(self):
        self.answer.setVisible(True)

    def create_answer(self):
        answer = QLabel(self.data.right_answer)
        answer.setVisible(False)
        no_resize = answer.sizePolicy()
        no_resize.setRetainSizeWhenHidden(True)
        answer.setSizePolicy(no_resize)
        answer.setMaximumHeight(60)
        return answer
