from data_objects.deck import Deck
from data_objects.normal_question import NormalQuestion
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui.normal_question_widget import NormalQuestionWidget


class Exam(QWidget):
    def __init__(self, deck: Deck, sequence: list[int]):
        layout = QGridLayout()
        super().__init__()
        self.deck: Deck = deck
        self.sequence = sequence
        self.curr_index = 0
        self.questions = self.__get_questions(layout)
        title: QLabel = QLabel()
        w, h = self.size().width(), self.size().height()
        title.setText(self.deck.title)
        title.setFont(QFont('Arial', 24))
        title.adjustSize()
        title.setMaximumHeight(40)
        #title.setStyleSheet("border: 1px solid red;")
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignHCenter)

        button_layout = QHBoxLayout()
        prev = QPushButton("PREV")
        next_q = QPushButton("NEXT")
        button_layout.addWidget(prev)
        button_layout.addWidget(next_q)
        layout.addLayout(button_layout, 3, 0, 1, 3, Qt.AlignHCenter)

        next_q.clicked.connect(self.next_question)
        prev.clicked.connect(self.prev_question)
        self.setLayout(layout)
        self.questions[self.curr_index].setVisible(True)

    def __get_questions(self, layout: QGridLayout) -> list[QWidget]:
        result: list[QWidget] =  []
        cards = self.deck.questions
        for i in self.sequence:
            question = cards[i]
            if isinstance(question, NormalQuestion):
                curr = NormalQuestionWidget(question)
                curr.setVisible(False)
                result.append(curr)
                layout.addWidget(curr, 1, 1)
        return result

    def __advance(self, n: int):
        if self.curr_index + n >= len(self.sequence) or self.curr_index + n < 0:
            # finish
            return 
        self.questions[self.curr_index].setVisible(False)
        self.curr_index = (self.curr_index + n) % self.deck.card_num
        self.questions[self.curr_index].setVisible(True)

    def next_question(self):
        self.__advance(1)

    def prev_question(self):
        self.__advance(-1)

