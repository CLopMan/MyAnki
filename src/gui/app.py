from PyQt5.QtWidgets import QApplication
from os import listdir

class App(QApplication):

    def __init__(self, resources_folder_path, argv: list = []):
        super().__init__(argv)
        self.resources_folder_path = resources_folder_path

    def get_decks(self):
        return list(listdir(self.resources_folder_path / "decks"))

