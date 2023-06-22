# File: Main.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 20, 2023 (Today's Date)
# Last Modified: June 20, 2023 (Juned Miah - Adding Dask + edit menu for normalization and pre-processing)

import os

from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFileDialog


import csv_handler


# noinspection PyUnresolvedReferences
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cell Profiler")
        MainWindow.resize(760, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Modules section
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.modules_label = QtWidgets.QLabel(self.centralwidget)
        self.modules_label.setObjectName("modules_label")
        self.verticalLayout_2.addWidget(self.modules_label)
        self.types_button = QtWidgets.QPushButton(self.centralwidget)
        self.types_button.setObjectName("types_button")
        self.verticalLayout_2.addWidget(self.types_button)
        self.graph_button = QtWidgets.QPushButton(self.centralwidget)
        self.graph_button.setObjectName("graph_button")
        self.verticalLayout_2.addWidget(self.graph_button)
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_2.addWidget(self.settings_button)
        self.verticalLayout_2.addSpacerItem(
            QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # Data section
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_loaded_label = QtWidgets.QLabel(self.centralwidget)
        self.file_loaded_label.setObjectName("file_loaded_label")
        self.verticalLayout_3.addWidget(self.file_loaded_label)
        self.Check_all_box = QtWidgets.QCheckBox(self.centralwidget)
        self.Check_all_box.setObjectName("Check_all_box")
        self.Check_all_box.stateChanged.connect(self.checkAll)
        self.verticalLayout_3.addWidget(self.Check_all_box)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.model = QStandardItemModel(self.tableView)
        self.tableView.setModel(self.model)

        # Menu and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionLoad_CSV = QtWidgets.QAction(MainWindow)
        self.actionLoad_CSV.setObjectName("actionLoad_CSV")
        self.actionLoad_CSV.setText("Load CSV")
        self.actionLoad_CSV.triggered.connect(self.loadCSV)
        self.menuFile.addAction(self.actionLoad_CSV)

        self.actionExport_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_CSV.setObjectName("actionExport_CSV")
        self.actionExport_CSV.setText("Export CSV")
        self.actionExport_CSV.triggered.connect(self.exportCSV)
        self.menuFile.addAction(self.actionExport_CSV)

        self.actionNormalizeData = QtWidgets.QAction(MainWindow)
        self.actionNormalizeData.setObjectName("actionNormalizeData")
        self.actionNormalizeData.setText("Normalize Data")
        self.actionNormalizeData.triggered.connect(self.normalizeData)
        self.menuEdit.addAction(self.actionNormalizeData)

        self.actionRemoveNA = QtWidgets.QAction(MainWindow)
        self.actionRemoveNA.setObjectName("actionRemoveNA")
        self.actionRemoveNA.setText("Remove N/A entries")
        self.actionRemoveNA.triggered.connect(self.removeNA)
        self.menuEdit.addAction(self.actionRemoveNA)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.settings_button, self.graph_button)
        MainWindow.setTabOrder(self.graph_button, self.types_button)

    def loadCSV(self):
        filename = csv_handler.browse_file()
        if filename:
            self.file_loaded_label.setText(f"File Loaded: {os.path.basename(filename)}")
            self.data = csv_handler.load_csv_file(filename)
            if self.data is not None:
                self.display_data(self.data)
                self.create_checkboxes(self.data.columns)
                self.Check_all_box.setChecked(True)
            else:
                print("No data in the file.")
        else:
            print("No file selected.")

    def create_checkboxes(self, columns):
        self.checkboxes = []
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for i, column in enumerate(columns):
            checkbox = QtWidgets.QCheckBox(column, self.scrollAreaWidgetContents)
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(lambda state, x=i: self.toggle_column(x, state))
            self.gridLayout.addWidget(checkbox, i, 0, 1, 1)
            self.checkboxes.append(checkbox)

    def toggle_column(self, column, state):
        self.tableView.setColumnHidden(column, not bool(state))

    def display_data(self, data):
        try:
            if data is not None:
                self.model.clear()
                for column in data.columns:
                    item = QStandardItem(column)
                    item.setCheckable(True)
                    self.model.setHorizontalHeaderItem(data.columns.get_loc(column), item)

                for i in range(data.shape[0]):
                    for j in range(data.shape[1]):
                        item = QStandardItem(str(data.iat[i, j]))
                        self.model.setItem(i, j, item)

        except Exception as e:
            print(f"Error: {e}")

    def handleItemChanged(self, item):
        if item.isCheckable() and (item.checkState() == QtCore.Qt.Checked):
            for index in range(self.model.rowCount()):
                self.model.item(index, item.column()).setEnabled(False)
        elif item.isCheckable() and (item.checkState() == QtCore.Qt.Unchecked):
            for index in range(self.model.rowCount()):
                self.model.item(index, item.column()).setEnabled(True)

    def retranslateUi(self, MainWindow):
        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "Cell Profiler"))
        self.modules_label.setText(translate("MainWindow", "Modules"))
        self.types_button.setText(translate("MainWindow", "Names / Types"))
        self.graph_button.setText(translate("MainWindow", "Graph"))
        self.settings_button.setText(translate("MainWindow", "Settings"))
        self.file_loaded_label.setText(translate("MainWindow", "No File Loaded"))
        self.Check_all_box.setText(translate("MainWindow", "Check All"))
        self.menuFile.setTitle(translate("MainWindow", "File"))
        self.menuEdit.setTitle(translate("MainWindow", "Edit"))
        self.menuView.setTitle(translate("MainWindow", "View"))
        self.actionLoad_CSV.setText(translate("MainWindow", "Load CSV"))
        self.actionExit.setText(translate("MainWindow", "Exit"))

    def checkAll(self, state):
        # Check or uncheck all checkboxes based on the state of the "Check All" checkbox
        for checkbox in self.checkboxes:
            checkbox.setChecked(state == QtCore.Qt.Checked)

    def normalizeData(self):
        try:
            self.data = (self.data - self.data.min()) / (self.data.max() - self.data.min())
            self.display_data(self.data)
            self.create_checkboxes(self.data.columns)
            print("Data normalized successfully.")
        except Exception as e:
            print(f"Error while normalizing data: {e}")

    def removeNA(self):
        try:
            self.data = self.data.dropna()  # Remove rows with missing values
            self.display_data(self.data)
            print("N/A entries removed successfully.")
        except Exception as e:
            print(f"Error while removing N/A entries: {e}")

    def exportCSV(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(None, "Export CSV", ".", "CSV Files (*.csv)")
            if filename:
                csv_handler.export_csv_file(filename, self.data)
            else:
                print("No file selected.")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
