from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from os.path import exists

from data_objects.question import Question
from constants.gui_constants import *
from constants.env_variables import RESOURCES_FOLDER

class QuestionWidget(QWidget):
    def __init__(self, question: Question):
        super().__init__()
        self.data = question
        self.exercise: QWidget = self.create_exercise()
        self.answer: QWidget = self.create_answer()
        self.show_button: QPushButton = QPushButton("SHOW ANSWER")
        self.value = question.value
        self.correct: bool|None = None

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

    def _set_correct(self, val):
        self.correct = val
    
    def set_correct(self):
        self._set_correct(True)

    def set_wrong(self):
        self._set_correct(False)

    def create_answer(self):
        return NotImplemented

    def create_exercise(self) -> QWidget:
        exercise  = QLabel(self.data.question)
        exercise.setFont(QFont('Arial', 16))
        exercise.setWordWrap(True)
        layout = QVBoxLayout() 
        layout.addWidget(exercise)

        if self.data.image is not None:
            img = QLabel()
            path = str(RESOURCES_FOLDER / "imgs" / self.data.image)
            if exists(path):
                pxmap = QPixmap(path).scaledToWidth(100)
                img.setPixmap(pxmap)
            else:
                img.setText(f"Unable to open {self.data.image}")

            layout.addWidget(img)

        result = QWidget()
        result.setLayout(layout)
        return result

    def show_answer(self):
        self.answer.setVisible(True)
