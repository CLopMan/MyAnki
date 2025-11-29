from PyQt5.QtWidgets import QMainWindow

from data_objects.deck import Deck
from gui.deck_scrollable_array import DeckScrollableArray
from adapters.deck_adapter import DeckAdapter
from dtos.deck_dto import DeckDto
from constants.env_variables import RESOURCES_FOLDER

DECK_FOLDER = RESOURCES_FOLDER / "decks"


class MainWindow(QMainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        deck_adapter = DeckAdapter()
        decks: list[Deck] = []
        for file in self.app.get_decks():
            with open(DECK_FOLDER / file, "r") as fd:
                try:
                    deck_dto = DeckDto.model_validate_json(fd.read())
                    decks.append(deck_adapter.adapt_deck(deck_dto))
                except Exception as e:
                    print(f"deck could not be parsed: {file}\n\t{str(e)}")

        self.decks_widget = DeckScrollableArray(self, decks)
        self.setCentralWidget(self.decks_widget)
        self.setWindowTitle("Let's study")
        self.decks_widget.move(self.rect().center())

