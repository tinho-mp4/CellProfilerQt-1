import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter
from PyQt5 import QtCore, QtGui, QtWidgets


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


class YaxisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(YaxisWindow, self).__init__()
        self.rows = None
        self.data_frame = None
        self.save_button = None
        self.bottom_layout = None
        self.column_combo_box = None
        self.select_column_label = None
        self.top_layout = None
        self.verticalLayout = None
        self.gridLayout_2 = None
        self.yAxisData = []
        self.items = set()
        self.setObjectName("y_axis_window")
        self.setFixedSize(370, 200)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.setupUi()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def setupUi(self):
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.setObjectName("top_layout")
        self.select_column_label = QtWidgets.QLabel(self.centralwidget)
        self.select_column_label.setObjectName("select_column_label")
        self.top_layout.addWidget(self.select_column_label)
        self.column_combo_box = AutoCompletingComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.column_combo_box.sizePolicy().hasHeightForWidth())
        self.column_combo_box.setSizePolicy(sizePolicy)
        self.column_combo_box.setObjectName("column_combo_box")
        self.top_layout.addWidget(self.column_combo_box)
        self.verticalLayout.addLayout(self.top_layout)
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.setObjectName("bottom_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.bottom_layout.addWidget(self.save_button)
        self.verticalLayout.addLayout(self.bottom_layout)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.save_button.clicked.connect(self.saveButtonHandler)

    def retranslateUi(self):
        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("y_axis_window", "Y Axis"))
        self.select_column_label.setText(translate("y_axis_window", "Select Column"))
        self.save_button.setText(translate("y_axis_window", "Save"))

    def set_table_data_frame(self, data):
        self.data_frame = data

    def saveButtonHandler(self):
        for row in self.rows:
            self.yAxisData.append(
                self.data_frame.at[self.data_frame.index[row], str(self.column_combo_box.currentText())])
        print("worked?")
        self.close()

    def getyAxisData(self):
        return self.yAxisData

    def setRows(self, xRows):
        self.rows = xRows
