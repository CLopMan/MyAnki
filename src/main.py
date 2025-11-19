import random
from gui.mainwindow import *
from gui.exam import *
from constants.env_variables import RESOURCES_FOLDER
from dtos.deck_dto import DeckDto
from adapters.deck_adapter import DeckAdapter
from gui.true_false_question_widget import TrueFalseQuestionWidget
from gui.mainwindow import App


if __name__ == "__main__":
    app = App(RESOURCES_FOLDER)
    window = MainWindow(app)
    window.show()
    app.exec_()

