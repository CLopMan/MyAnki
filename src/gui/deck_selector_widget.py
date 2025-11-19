from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
from gui.exam import Exam
from data_objects.deck import Deck

class DeckSelectorWidget(QWidget):
    def __init__(self, parent: QWidget|None, deck: Deck):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        title_label = QLabel(deck.title)

        down_layout = self.down_layout(deck.card_num)

        layout.addWidget(title_label, 2)
        layout.addLayout(down_layout, 1)
        
        self.setLayout(layout)
        self.setMaximumSize(300,100)
        self.deck = deck

    def down_layout(self, card_num: int):
        card_num_label = QLabel(str(card_num) + " cards")
        card_num_label.setAlignment(Qt.AlignCenter)
        card_num_label.setMaximumHeight(30)

        start_button = QPushButton("START")
        start_button.clicked.connect(self.start_deck)
        start_button.clicked.connect(lambda : print("pressed start"))

        objetive = QTextEdit()
        objetive.setPlaceholderText(str(card_num))
        objetive_label = QLabel("Cards to study")
        objetive_label.setWordWrap(True)
        
        objetive_label.setAlignment(Qt.AlignCenter)
        objetive.setMaximumHeight(30)

        self.objetive = objetive

        goal_layout = QHBoxLayout()
        goal_layout.addWidget(objetive_label)
        goal_layout.addWidget(objetive)

        down_layout = QHBoxLayout()
        down_layout.addWidget(card_num_label, 1)
        down_layout.addWidget(start_button, 1)
        down_layout.addLayout(goal_layout, 1)
        return down_layout

    def __validate_goal_text(self, value: str) -> int:
        if value == "":
            print("Empty, returning max value")
            return int(len(self.deck))

        for c in value:
            if not c.isnumeric():
                raise ValueError("Number of cards must be a number")
        out_value = int(value) 
        if out_value > 0:
            return min(len(self.deck), out_value)

        raise ValueError("Cannot do an exam with no questions, you stupid fella")

    def start_deck(self):
        try:
            value: int = self.__validate_goal_text(self.objetive.toPlainText())
        except ValueError as e:
            print("Cannot estart the exam because of bad input") # TODO: warn message
            w = QWidget()
            b = QPushButton("Close")
            b.clicked.connect(lambda : w.close() )
            w.setLayout(QVBoxLayout())
            w.layout().addWidget(QLabel(str(e)))
            w.layout().addWidget(b)
            w.show()
            return 

        exam = Exam(deck=self.deck, sequence=random.sample(range(len(self.deck)), value))
        exam.show()
