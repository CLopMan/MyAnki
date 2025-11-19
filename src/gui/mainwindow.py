from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import listdir
from data_objects.deck import Deck
from adapters.deck_adapter import DeckAdapter
from dtos.deck_dto import DeckDto
from constants.env_variables import RESOURCES_FOLDER
from gui.deck_selector_widget import DeckSelectorWidget


class DeckScrollableArray(QScrollArea):
    def __init__(self, parent: QWidget, items: list[Deck]|None = None):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        if items is None:
            self.items = []
        else:
            self.items = items

        self.items_ui = []

        self.init_ui()
        w, h = int(self.parentWidget().width()), int(self.parentWidget().height())
        print(w, h)
        self.setGeometry(0, 0, w//2, h)
        self.setFixedSize(w//2, h)
        print(self.width(), self.height())

#        self.setStyleSheet("border: 1px solid red")

    def init_ui(self):
        self.items_ui = []
        layout = QVBoxLayout()
        container = QWidget()
        self.setWidget(container)
        for i, d in enumerate(self.items):
            self.items_ui.append(DeckSelectorWidget(self, d))
            layout.addWidget(self.items_ui[i])
        container.setLayout(layout)


    def add_deck(self, deck: Deck):
        raise NotImplemented

    def remove_deck(self, index):
        raise NotImplemented





class MainWindow(QWidget):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        deck_adapter = DeckAdapter()
        aux = QVBoxLayout()
        decks: list[Deck] = []
        for file in self.app.get_decks():
            with open(RESOURCES_FOLDER / file, "r") as fd:
                try:
                    deck_dto = DeckDto.model_validate_json(fd.read())
                    decks.append(deck_adapter.adapt_deck(deck_dto))
                    #aux.addWidget(DeckSelectorWidget(self, adapted_deck))
                    #self.deck_set.add_deck(adapted_deck)
                except Exception as e:
                    print(f"deck could not be parsed: {file}\n\t{str(e)}")

        #aux.addWidget(self.deck_set)
        self.decks_widget = DeckScrollableArray(self, decks)
        aux.addWidget(self.decks_widget)
        self.setWindowTitle("Let's study")
        self.resize(int(1920 * 0.7), int(1080 * 0.7))
        self.setLayout(aux)

class App(QApplication):

    def __init__(self, resources_folder_path, argv: list = []):
        super().__init__(argv)
        self.resources_folder_path = resources_folder_path

    def get_decks(self):
        return list(listdir(self.resources_folder_path))

