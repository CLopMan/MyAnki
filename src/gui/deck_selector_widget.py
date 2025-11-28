from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
from gui.exam import Exam
from data_objects.deck import Deck

class CustomDeckMenu(QDialog):
    class TagList(QScrollArea):
        def __init__(self, parent: QWidget, tags: set[str]):
            super().__init__(parent)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            container = QWidget()
            container_layout = QVBoxLayout()
            self.checked: dict[str, bool] = {}
            for tag in tags:
                self.checked[tag] = False
                checkbox = QCheckBox()
                checkbox.clicked.connect(lambda _, t=tag, cb=checkbox : self.checked.__setitem__(t, cb.isChecked()))
                hlayout = QHBoxLayout()
                hlayout.addWidget(QLabel(tag))
                hlayout.addWidget(checkbox)
                container_layout.addLayout(hlayout)
            container.setLayout(container_layout)
            self.setWidget(container)

    def __init__(self, parent: QWidget | None, possible_tags):
        super().__init__(parent)
        self.tag_list = self.TagList(self, possible_tags)
        self.ok = QPushButton("OK")
        self.ok.clicked.connect(super().accept)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Filter by Tag"))
        layout.addWidget(self.tag_list)
        layout.addWidget(self.ok)
        self.setLayout(layout)

    def get_filtered(self):
        d = self.tag_list.checked
        return [k for k, v in d.items() if v == True]


class DeckSelectorWidget(QWidget):
    def __init__(self, parent: QWidget|None, deck: Deck):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        title_label = QLabel(deck.title)

        down_layout = self.down_layout(deck.card_num)
        self.msg = QLabel("Filtered: None")

        layout.addWidget(title_label, 2)
        layout.addWidget(self.msg, 2)
        layout.addLayout(down_layout, 1)
        self.setLayout(layout)
        self.setMaximumSize(400,150)
        self.deck = deck
        self.custom_menu = CustomDeckMenu(self, deck.possible_tags)

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
        custom_study_button = QPushButton("⚙️")
        custom_study_button.setFixedSize(17, 17)
        custom_study_button.clicked.connect(self.custom_study_menu)

        goal_layout = QHBoxLayout()
        goal_layout.addWidget(objetive_label)
        goal_layout.addWidget(objetive)

        down_layout = QHBoxLayout()
        down_layout.addWidget(card_num_label, 1)
        down_layout.addWidget(start_button, 1)

        down_layout.addLayout(goal_layout, 1)
        down_layout.addWidget(custom_study_button, 1)
        return down_layout

    def custom_study_menu(self):
        self.custom_menu.exec()
        filtered = self.custom_menu.get_filtered()

        if len(filtered) > 0:
            self.msg.setText(f"Filtered: {filtered}")
        else:
            self.msg.setText(f"Filtered: None")

    @staticmethod
    def __validate_goal_text(value: str, deck: Deck) -> int:
        if value == "":
            print("Empty, returning max value")
            return int(len(deck))

        for c in value:
            if not c.isnumeric():
                raise ValueError("Number of cards must be a number")
        out_value = int(value) 
        if out_value > 0:
            return min(len(deck), out_value)

        raise ValueError("Cannot do an exam with no questions, you stupid fella")

    def start_deck(self):
        filtered = self.custom_menu.get_filtered()
        deck = self.deck.filter(filtered)
        try:
            value: int = self.__validate_goal_text(self.objetive.toPlainText(), deck)
        except ValueError as e:
            print("Cannot estart the exam because of bad input")
            w = QDialog(self)
            w.setWindowTitle("Error")
            b = QPushButton("Accept")
            b.clicked.connect(w.accept)
            layout = QVBoxLayout()
            w.setLayout(layout)
            layout.addWidget(QLabel(str(e)))
            layout.addWidget(b)
            w.exec()
            return

        exam = Exam(deck=deck, sequence=random.sample(range(len(deck)), value))
        exam.show()
