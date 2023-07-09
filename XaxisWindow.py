import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter


class AutoCompletingComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.lineEdit().setAlignment(Qt.AlignLeft)
        self.setCompleter(QCompleter(self.model()))
        self.lineEdit().setCompleter(self.completer())
        self.setInsertPolicy(QComboBox.NoInsert)

    def addItemToComboBox(self, item):
        super().addItem(item)
        self.completer().setModel(self.model())


class XaxisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(XaxisWindow, self).__init__()
        self.save_button = None
        self.save_horizontal_layout = None
        self.save_vertical_layout = None
        self.xAxisData = []
        self.items = set()
        self.data_frame = None
        self.top_combo_box = None
        self.from_label = None
        self.top_horizontal_layout = None
        self.top_vertical_layout = None
        self.bottom_combobox = None
        self.select_column_label = None
        self.bottom_horizontal_layout = None
        self.bottom_vertical_layout = None
        self.middle_combobox = None
        self.select_values_label = None
        self.middle_vertical_layout = None
        self.middle_horizontal_layout = None
        self.gridLayout_2 = None
        self.setObjectName("x_axis_window")
        self.setFixedSize(550, 220)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.top_combo_box = None
        self.middle_combobox = None
        self.bottom_combobox = None
        self.setupUi()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setupUi(self):
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.middle_vertical_layout = QtWidgets.QVBoxLayout()
        self.middle_vertical_layout.setObjectName("middle_vertical_layout")
        self.middle_horizontal_layout = QtWidgets.QHBoxLayout()
        self.middle_horizontal_layout.setObjectName("middle_horizontal_layout")
        self.select_values_label = QtWidgets.QLabel(self.centralwidget)
        self.select_values_label.setObjectName("select_values_label")
        self.middle_horizontal_layout.addWidget(self.select_values_label)
        self.middle_combobox = AutoCompletingComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_combobox.sizePolicy().hasHeightForWidth())
        self.middle_combobox.setSizePolicy(sizePolicy)
        self.middle_combobox.setObjectName("middle_combobox")
        self.middle_horizontal_layout.addWidget(self.middle_combobox)
        self.middle_vertical_layout.addLayout(self.middle_horizontal_layout)
        self.gridLayout_2.addLayout(self.middle_vertical_layout, 4, 0, 1, 1)

        self.bottom_vertical_layout = QtWidgets.QVBoxLayout()
        self.bottom_vertical_layout.setObjectName("bottom_vertical_layout")
        self.bottom_horizontal_layout = QtWidgets.QHBoxLayout()
        self.bottom_horizontal_layout.setObjectName("bottom_horizontal_layout")
        self.select_column_label = QtWidgets.QLabel(self.centralwidget)
        self.select_column_label.setObjectName("select_column_label")
        self.bottom_horizontal_layout.addWidget(self.select_column_label)
        self.bottom_combobox = AutoCompletingComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_combobox.sizePolicy().hasHeightForWidth())
        self.bottom_combobox.setSizePolicy(sizePolicy)
        self.bottom_combobox.setObjectName("bottom_combobox")
        self.bottom_horizontal_layout.addWidget(self.bottom_combobox)
        self.bottom_vertical_layout.addLayout(self.bottom_horizontal_layout)
        self.gridLayout_2.addLayout(self.bottom_vertical_layout, 5, 0, 1, 1)

        self.top_vertical_layout = QtWidgets.QVBoxLayout()
        self.top_vertical_layout.setObjectName("top_vertical_layout")
        self.top_horizontal_layout = QtWidgets.QHBoxLayout()
        self.top_horizontal_layout.setObjectName("top_horizontal_layout")
        self.from_label = QtWidgets.QLabel(self.centralwidget)
        self.from_label.setObjectName("from_label")
        self.top_horizontal_layout.addWidget(self.from_label)
        self.top_combo_box = AutoCompletingComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_combo_box.sizePolicy().hasHeightForWidth())
        self.top_combo_box.setSizePolicy(sizePolicy)
        self.top_combo_box.setObjectName("top_combo_box")
        self.top_horizontal_layout.addWidget(self.top_combo_box)
        self.top_vertical_layout.addLayout(self.top_horizontal_layout)
        self.gridLayout_2.addLayout(self.top_vertical_layout, 2, 0, 1, 1)

        self.save_vertical_layout = QtWidgets.QVBoxLayout()
        self.save_vertical_layout.setObjectName("save_vertical_layout")
        self.save_horizontal_layout = QtWidgets.QHBoxLayout()
        self.save_horizontal_layout.setObjectName("save_horizontal_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save_horizontal_layout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("Save")
        self.save_horizontal_layout.addWidget(self.save_button)
        self.save_vertical_layout.addLayout(self.save_horizontal_layout)
        self.gridLayout_2.addLayout(self.save_vertical_layout, 6, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.save_button.clicked.connect(self.saveButtonHandler)
        self.top_combo_box.activated.connect(self.fillMiddleComboBox)

    def retranslateUi(self):
        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("MainWindow", "X Axis"))
        self.select_values_label.setText(translate("MainWindow", "Select values of"))
        self.select_column_label.setText(translate("MainWindow", "Select column"))
        self.from_label.setText(translate("MainWindow", "From"))
        self.save_button.setText(translate("MainWindow", "Save"))

    def fillMiddleComboBox(self):
        self.middle_combobox.clear()
        self.items.clear()
        text = self.top_combo_box.currentText()
        column_values = self.data_frame[text]
        for value in column_values:
            if value not in self.items:
                self.items.add(value)
                self.middle_combobox.addItemToComboBox(str(value))

    def set_table_data_frame(self, data):
        self.data_frame = data

    def saveButtonHandler(self):
        rows = self.data_frame.index[
            self.data_frame[self.top_combo_box.currentText()] == self.middle_combobox.currentText()]
        for row in rows:
            self.xAxisData.append(
                self.data_frame.at[self.data_frame.index[row], str(self.bottom_combobox.currentText())])
        self.close()

    def getxAxisData(self):
        return self.xAxisData


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    x_axis_window = XaxisWindow()
    x_axis_window.show()
    sys.exit(app.exec_())
