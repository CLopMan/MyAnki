import json 
import random
from gui.mainwindow import *
from gui.exam import *
from env_variables import RESOURCES_FOLDER
from dtos.deck_dto import DeckDto
from adapters.deck_adapter import DeckAdapter


if __name__ == "__main__":
    deck_adapter = DeckAdapter()
    app = QApplication([])
    with open(RESOURCES_FOLDER / "testdeck.json", "r") as fd:
        deck_dto = DeckDto.model_validate_json(fd.read())
    window = Exam(deck=deck_adapter.adapt_deck(deck_dto), sequence=random.sample(range(len(deck_dto)), len(deck_dto)))
    window.show()
    app.exec_()

