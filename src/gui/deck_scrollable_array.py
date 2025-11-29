from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout 
from PyQt5.QtCore import Qt

from data_objects.deck import Deck
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
        parent = self.parentWidget() or QWidget()
        w, h = parent.width(), parent.height()
        self.setGeometry(0, 0, w//2, h)
        self.setFixedSize(w//2, h)

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

