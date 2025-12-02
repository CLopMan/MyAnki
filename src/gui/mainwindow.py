from PyQt5.QtWidgets import QMainWindow

from data_objects.deck import Deck
from gui.deck_scrollable_array import DeckScrollableArray
from adapters.deck_adapter import DeckAdapter
from dtos.deck_dto import DeckDto
from constants.gui_constants import APP_TITLE



class MainWindow(QMainWindow):
    def __init__(self, deck_paths: list[str], resources_folder) -> None:
        super().__init__()
        deck_adapter = DeckAdapter()
        decks: list[Deck] = []

        self.resources_folder = resources_folder
        self.deck_folder = resources_folder / "decks"
        for file in deck_paths:
            with open(self.deck_folder / file, "r") as fd:
                try:
                    deck_dto = DeckDto.model_validate_json(fd.read())
                    decks.append(deck_adapter.adapt_deck(deck_dto))
                except Exception as e:
                    print(f"deck could not be parsed: {file}\n\t{str(e)}")

        self.decks_widget = DeckScrollableArray(self, decks)
        self.setCentralWidget(self.decks_widget)
        self.setWindowTitle(APP_TITLE)
        self.decks_widget.move(self.rect().center())

