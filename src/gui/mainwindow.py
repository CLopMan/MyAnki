from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import listdir
from data_objects.deck import Deck, Question
from abc import ABC





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

    def down_layout(self, card_num: int):
        card_num_label = QLabel(str(card_num) + " cards")
        card_num_label.setAlignment(Qt.AlignCenter)
        card_num_label.setMaximumHeight(30)

        start_button = QPushButton("START")
        start_button.clicked.connect(self.start_deck)
        start_button.clicked.connect(lambda : print("pressed start"))

        objetive = QTextEdit()
        objetive.setPlaceholderText(str(card_num))
        objetive_label = QLabel("Goal")
        objetive_label.setAlignment(Qt.AlignCenter)
        objetive.setMaximumHeight(30)

        goal_layout = QHBoxLayout()
        goal_layout.addWidget(objetive_label)
        goal_layout.addWidget(objetive)

        down_layout = QHBoxLayout()
        down_layout.addWidget(card_num_label, 1)
        down_layout.addWidget(start_button, 1)
        down_layout.addLayout(goal_layout, 1)
        return down_layout
    
    def start_deck(self):
        pass


class DeckScrollableArray(QWidget):
    decks: dict[str, Deck] = {}
    def __init__(self):
        pass

    def add_deck(self, deck):
        pass

    def remove_deck(self, deck):
        pass


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Let's study")
        self.resize(int(1920 * 0.7), int(1080 * 0.7))
        aux = QVBoxLayout()
        aux.addWidget(DeckSelectorWidget(self, Deck("testdeck")))
        self.setLayout(aux)

class App(QApplication):
    def __init__(self, resources_folder_path, argv: list = []):
        super().__init__(argv)
        self.resources_folder_path = resources_folder_path
    def get_decks(self):
        print(listdir(self.resources_folder_path))
        pass

