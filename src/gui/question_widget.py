from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from data_objects.question import Question
from constants.gui_constants import *

class QuestionWidget(QWidget):
    def __init__(self, question: Question):
        super().__init__()
        self.data = question
        self.exercise: QWidget = self.create_exercise()
        self.answer: QWidget = self.create_answer()
        self.show_button: QPushButton = QPushButton("SHOW ANSWER")
        self.value = question.value

        layout = QVBoxLayout()
        layout.addWidget(self.exercise)
        layout.addWidget(self.answer)
        layout.addWidget(self.show_button)
        self.show_button.clicked.connect(self.show_answer)
        self.setLayout(layout)
        self.setFixedSize(EXERCISE_WIDTH, EXERCISE_HEIGHT)

    @property
    def is_answered(self):
        return self.answer.isVisible()

    def create_answer(self):
        return NotImplemented

    def create_exercise(self) -> QLabel:
        result = QLabel(self.data.question)
        result.setFont(QFont('Arial', 16))
        result.setWordWrap(True)
        return result

    def show_answer(self):
        self.answer.setVisible(True)
