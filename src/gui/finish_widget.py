from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout)
from PyQt5.QtCore import Qt
from constants.gui_constants import RESULT_WIDTH, RESULT_HEIGH, EXERCISE_WIDTH, EXERCISE_HEIGHT
from gui.question_widget import QuestionWidget

class FinishWidget(QWidget):
    def __init__(self, n_questions, columns):
        super().__init__()
        n_questions_discount = n_questions
        layout: QGridLayout = QGridLayout()
        rows = n_questions // columns + (n_questions % columns > 0)
        self.questions = []
        for x in range(rows):
            for y in range(min(columns, n_questions_discount)):
                w = QLabel(str(n_questions - n_questions_discount + 1))
                w.setStyleSheet("background: #aaaaaa;")
                w.setFixedSize(RESULT_WIDTH, RESULT_HEIGH)
                w.setAlignment(Qt.AlignCenter)
                layout.addWidget(w, x, y, 1, 1)
                n_questions_discount -= 1
                self.questions.append(w)

        self.setLayout(layout)
        self.setFixedSize(EXERCISE_WIDTH, EXERCISE_HEIGHT)

    def update_result(self, questions: list[QuestionWidget]):
        for i, b in enumerate(questions):
            if b.correct is None:
                pass
            elif b.correct:
                self.questions[i].setStyleSheet("background: #00ff00")
            else:
                self.questions[i].setStyleSheet("background: #ff0000")

