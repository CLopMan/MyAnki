from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from data_objects.question import Question
from constants.gui_constants import *

class QuestionWidget(QWidget):
    def __init__(self, question: Question):
        super().__init__()
        self.data = question
        self.exercise: QLabel = self.create_exercise()
        self.answer: QLabel = self.create_answer()
        self.show_button: QPushButton = QPushButton("SHOW ANSWER")

        layout = QVBoxLayout()
        layout.addWidget(self.exercise)
        layout.addWidget(self.answer)
        layout.addWidget(self.show_button)
        self.show_button.clicked.connect(self.show_answer)
        self.setLayout(layout)
        self.setFixedSize(EXERCISE_WIDTH, EXERCISE_HEIGHT)

    def create_answer(self):
        return NotImplemented

    def create_exercise(self) -> QLabel:
        return QLabel(self.data.question)

    def show_answer(self):
        self.answer.setVisible(True)
