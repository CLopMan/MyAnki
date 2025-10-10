from PyQt5.QtWidgets import QWidget, QLabel
from data_objects.question import Question

class QuestionWidget(QWidget):
    def __init__(self, question: Question):
        super().__init__()
        self.data = question

    def create_answer(self):
        return NotImplemented

    def create_exercise(self) -> QLabel:
        return QLabel(self.data.question)

    def show_answer(self):
        self.answer.setVisible(True)
