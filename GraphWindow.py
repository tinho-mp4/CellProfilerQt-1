from PyQt5 import QtWidgets


class GraphWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QtWidgets.QLabel("This is the Graph window", self)
        self.setCentralWidget(label)
