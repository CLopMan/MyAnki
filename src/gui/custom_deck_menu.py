from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CustomDeckMenu(QDialog):
    class TagList(QScrollArea):
        def __init__(self, parent: QWidget, tags: set[str]):
            super().__init__(parent)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            container = QWidget()
            container_layout = QVBoxLayout()
            self.checked: dict[str, bool] = {}
            for tag in tags:
                self.checked[tag] = False
                checkbox = QCheckBox()
                checkbox.clicked.connect(lambda _, t=tag, cb=checkbox : self.checked.__setitem__(t, cb.isChecked()))
                hlayout = QHBoxLayout()
                hlayout.addWidget(QLabel(tag))
                hlayout.addWidget(checkbox)
                container_layout.addLayout(hlayout)
            container.setLayout(container_layout)
            self.setWidget(container)

    def __init__(self, parent: QWidget | None, possible_tags):
        super().__init__(parent)
        self.tag_list = self.TagList(self, possible_tags)
        self.ok = QPushButton("OK")
        self.ok.clicked.connect(super().accept)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Filter by Tag"))
        layout.addWidget(self.tag_list)
        layout.addWidget(self.ok)
        self.setLayout(layout)

    def get_filtered(self):
        d = self.tag_list.checked
        return [k for k, v in d.items() if v == True]

