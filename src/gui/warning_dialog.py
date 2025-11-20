from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from collections.abc import Callable

class WarningDialog(QDialog):
    def  __init__(self, parent: QWidget | None, msg: str, title: str = "", accept_call: Callable[[], None] | None = None, reject_call: Callable[[], None] | None = None):
        super().__init__(parent)
        self.accept_call = accept_call
        self.reject_call = reject_call
        self.setWindowTitle(title)
        self.msg = msg

        

        accept = QPushButton("Accept")
        reject =  QPushButton("Reject")

        accept.clicked.connect(self.accept)
        reject.clicked.connect(self.reject)
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.addWidget(accept)
        button_layout.addWidget(reject)

        layout.addWidget(QLabel(msg))
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def accept(self):
        if self.accept_call is not None:
            self.accept_call()
        super().accept()

    def reject(self):
        if self.reject_call is not None:
            self.reject_call()
        super().reject()
