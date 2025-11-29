from data_objects.deck import Deck
from data_objects.normal_question import NormalQuestion
from data_objects.true_false_question import TrueFalseQuestion
from data_objects.combo_box_question import ComboBoxQuestion
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QProgressBar
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui.question_widget import QuestionWidget
from gui.normal_question_widget import NormalQuestionWidget
from gui.true_false_question_widget import TrueFalseQuestionWidget
from gui.combo_box_question_widget import ComboBoxQuestionWidget
from gui.finish_widget import FinishWidget
from gui.warning_dialog import WarningDialog
from constants.gui_constants import EXERCISE_WIDTH, COLUMNS

class Exam(QWidget):
    def __init__(self, deck: Deck, sequence: list[int]):
        layout = QGridLayout()
        layout.setColumnMinimumWidth(1, EXERCISE_WIDTH)

        super().__init__()
        self.deck: Deck = deck
        self.sequence = sequence
        self.curr_index = 0
        self.questions = self.__get_questions(layout)
        self.questions_answer = [False for _ in range(0, len(self.questions))]
        self.answered: int = 0

        layout.addWidget(self.title(), 0, 0, 1, 3, Qt.AlignHCenter)
        self.progress_bar = self.build_progress_bar()
        layout.addWidget(self.progress_bar, 1, 0, 1, 3, Qt.AlignHCenter)

        self.index_widget = self.create_index()
        self.__update_index()

        self.finish_widget: FinishWidget = FinishWidget(len(self.questions), COLUMNS)
        self.finish_widget.setVisible(False)

        layout.addWidget(self.finish_widget, 2, 1)

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
        self.prev = prev
        self.next = next_q
        self.finish_exam_button = QPushButton("QUIT EXAM")
        self.finish_exam_button.clicked.connect(lambda : self.close())
        self.finish_exam_button.setVisible(False)
        button_layout.addWidget(self.finish_exam_button)

        layout.addLayout(bottom_layout, 3, 0, 1, 3, Qt.AlignHCenter)

        self.setLayout(layout)
        self.questions[self.curr_index].setVisible(True)

    def create_index(self):
        index_widget = QLabel()
        index_widget.adjustSize()
        index_widget.setMaximumHeight(16)
        index_widget.setAlignment(Qt.AlignHCenter)
        return index_widget

    def build_progress_bar(self):
        bar = QProgressBar()
        bar.setMaximum(len(self.sequence))
        bar.setMinimum(0)
        bar.setValue(0)
        bar.setFixedWidth(EXERCISE_WIDTH - 20)
        return bar

    def update_progress_bar(self):
        self.progress_bar.setValue(self.answered)

    def title(self):
        title: QLabel = QLabel()
        title.setText(self.deck.title)
        title.setFont(QFont('Arial', 24))
        title.adjustSize()
        title.setMaximumHeight(40)
        #title.setStyleSheet("border: 1px solid red;")
        return title

    def __get_questions(self, layout: QGridLayout) -> list[QuestionWidget]:
        result: list[QuestionWidget] =  []
        cards = self.deck.questions
        for i in self.sequence:
            question = cards[i]
            if isinstance(question, NormalQuestion):
                curr = NormalQuestionWidget(question)
                curr.setVisible(False)
                result.append(curr)
                curr.show_button.clicked.connect(self.__update_answered)
                layout.addWidget(curr, 2, 1)
            if isinstance(question, TrueFalseQuestion):
                curr = TrueFalseQuestionWidget(question)
                curr.setVisible(False)
                result.append(curr)
                curr.show_button.clicked.connect(self.__update_answered)
                layout.addWidget(curr, 2, 1)
            if isinstance(question, ComboBoxQuestion):
                curr = ComboBoxQuestionWidget(question)
                curr.setVisible(False)
                result.append(curr)
                curr.show_button.clicked.connect(self.__update_answered)
                layout.addWidget(curr, 2, 1)

        return result

    def __advance(self, n: int):
        if self.curr_index + n >= len(self.sequence) or self.curr_index + n < 0:
            if (self.curr_index == len(self.questions) - 1):
                self.__finish()
            return 
        self.questions[self.curr_index].setVisible(False)
        self.curr_index = (self.curr_index + n) % self.deck.card_num
        self.questions[self.curr_index].setVisible(True)
        self.__update_index()
        if (self.curr_index == len(self.questions) - 1):
            self.next.setText("FINISH")
            self.next.setStyleSheet("background: #4472c4")
        else:
            self.next.setText("NEXT")
            self.next.setStyleSheet("")

    def _answer(self, index):
        self.questions_answer[index] = True

    def __update_answered(self):
        self.answered += not self.questions_answer[self.curr_index]
        self._answer(self.curr_index)
        self.update_progress_bar()

    def __update_index(self):
        self.index_widget.setText(f"{self.curr_index + 1}/{len(self.sequence)}")

    def next_question(self):
        self.__advance(1)
    
    def __finish(self):
        dlg = WarningDialog(self, f"Are you sure you want to finish the exam?\nYou have answer {self.answered} out of {len(self.questions)} questions", "Finish Exam?")
        if dlg.exec():
            self.questions[self.curr_index].setVisible(False)
            self.finish_widget.update_result(self.questions)
            self.finish_widget.setVisible(True)
            self.finish_exam_button.setVisible(True)

            self.prev.setVisible(False)
            self.next.setVisible(False)

    def prev_question(self):
        self.__advance(-1)

