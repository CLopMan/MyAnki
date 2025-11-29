from gui.mainwindow import MainWindow
from gui.app import App
from constants.env_variables import RESOURCES_FOLDER


if __name__ == "__main__":
    app = App(RESOURCES_FOLDER)
    window = MainWindow(app)
    window.show()
    app.exec_()

