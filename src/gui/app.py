from PyQt5.QtWidgets import QApplication
from os import listdir
from gui.mainwindow import MainWindow

class App(QApplication):

    def __init__(self, resources_folder_path, argv: list = []):
        super().__init__(argv)
        self.resources_folder_path = resources_folder_path
        self.main_window = MainWindow(self.get_decks())

    def get_decks(self):
        return list(listdir(self.resources_folder_path / "decks"))

    def exec_(self, *_):
        self.main_window.show()
        super().exec_()
        

