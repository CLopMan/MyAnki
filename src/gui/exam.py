from data_objects.deck import Deck
from data_objects.normal_question import NormalQuestion
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui.normal_question_widget import NormalQuestionWidget


class Exam(QWidget):
    def __init__(self, deck: Deck, sequence: list[int]):
        layout = QGridLayout()
        layout.setColumnMinimumWidth(1, 300)

        super().__init__()
        self.deck: Deck = deck
        self.sequence = sequence
        self.curr_index = 0
        self.questions = self.__get_questions(layout)

        layout.addWidget(self.title(), 0, 0, 1, 3, Qt.AlignHCenter)

        self.index_widget = self.create_index()
        self.__update_index()

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.index_widget)


        prev = QPushButton("PREV")
        next_q = QPushButton("NEXT")
        next_q.clicked.connect(self.next_question)
        prev.clicked.connect(self.prev_question)

        button_layout = QHBoxLayout()
        button_layout.addWidget(prev)
        button_layout.addWidget(next_q)
        bottom_layout.addLayout(button_layout)

        layout.addLayout(bottom_layout, 3, 0, 1, 3, Qt.AlignHCenter)

        self.setLayout(layout)
        self.questions[self.curr_index].setVisible(True)

    def create_index(self):
        index_widget = QLabel()
        index_widget.adjustSize()
        index_widget.setMaximumHeight(16)
        index_widget.setAlignment(Qt.AlignHCenter)
        return index_widget


    def title(self):
        title: QLabel = QLabel()
        title.setText(self.deck.title)
        title.setFont(QFont('Arial', 24))
        title.adjustSize()
        title.setMaximumHeight(40)
        #title.setStyleSheet("border: 1px solid red;")
        return title

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
        self.__update_index()

    def __update_index(self):
        self.index_widget.setText(f"{self.curr_index + 1}/{len(self.sequence)}")

    def next_question(self):
        self.__advance(1)

    def prev_question(self):
        self.__advance(-1)

