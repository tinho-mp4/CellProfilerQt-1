from PyQt5 import QtWidgets

class NameTypeWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QtWidgets.QLabel("This is the Name/Types window", self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)
