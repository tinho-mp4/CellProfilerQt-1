# File: Main.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 20, 2023,
# Last Modified: June 22, 2023 (Anush - Search bar implemented)

import os

from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import numpy as np


import csv_handler


class Ui_MainWindow(object):

    def __init__(self):
        self.horizontal_layout_gernerate_button = None
        self.graph_page = None
        self.settings_page = None
        self.settings_window = None
        self.graph_window = None
        self.names_types_window = None
        self.checkboxes = None
        self.data = None
        self.actionExit = None
        self.actionRemoveNA = None
        self.actionExport_CSV = None
        self.actionNormalizeData = None
        self.actionLoad_CSV = None
        self.statusbar = None
        self.menuView = None
        self.menuEdit = None
        self.menuFile = None
        self.menubar = None
        self.model = None
        self.tableView = None
        self.gridLayout = None
        self.scrollAreaWidgetContents = None
        self.scrollArea = None
        self.searchbar = None
        self.Check_all_box = None
        self.check_all_horizontal_layout = None
        self.gridLayout_3 = None
        self.names_types_page = None
        self.stacked_pages = None
        self.file_loaded_label = None
        self.right_side_vertical_layout = None
        self.settings_button = None
        self.graph_button = None
        self.types_button = None
        self.modules_label = None
        self.verticalLayout_2 = None
        self.horizontalLayout = None
        self.gridLayout_2 = None
        self.verticalLayout = None
        self.centralwidget = None

    def setupUi(self, Main_window):
        Main_window.setObjectName("Cell Profiler")
        Main_window.resize(760, 410)
        # Set application icon
        icon = QIcon("img/710590.png")
        Main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")


        # Grid layout for names and types page
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

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

        # types button
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
        self.right_side_vertical_layout = QtWidgets.QVBoxLayout()
        self.right_side_vertical_layout.setObjectName("right_side_vertical_layout")
        self.file_loaded_label = QtWidgets.QLabel(self.centralwidget)
        self.file_loaded_label.setObjectName("file_loaded_label")
        self.right_side_vertical_layout.addWidget(self.file_loaded_label, 0, QtCore.Qt.AlignTop)

        # Stacked pages setup to change between pages (change between modules)
        self.stacked_pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_pages.setObjectName("stacked_pages")

        # Graph page
        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setEnabled(True)
        self.graph_page.setObjectName("graph_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.graph_page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graph_grid_frame = QtWidgets.QFrame(self.graph_page)
        self.graph_grid_frame.setObjectName("graph_grid_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.graph_grid_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.vertical_layout_graph_left = QtWidgets.QWidget(self.graph_grid_frame)
        self.vertical_layout_graph_left.setObjectName("vertical_layout_graph_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.vertical_layout_graph_left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scatter_plot_radio = QtWidgets.QRadioButton(self.vertical_layout_graph_left)
        self.scatter_plot_radio.setObjectName("scatter_plot_radio")
        self.verticalLayout.addWidget(self.scatter_plot_radio)
        self.bar_graph_radio = QtWidgets.QRadioButton(self.vertical_layout_graph_left)
        self.bar_graph_radio.setObjectName("bar_graph_radio")
        self.verticalLayout.addWidget(self.bar_graph_radio)
        self.example_button = QtWidgets.QCheckBox(self.vertical_layout_graph_left)
        self.example_button.setObjectName("example_button")
        self.verticalLayout.addWidget(self.example_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_4.addWidget(self.vertical_layout_graph_left, 0, 0, 1, 1)
        self.vertical_layout_graph_right = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_right.setObjectName("vertical_layout_graph_right")
        self.check_all_horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.check_all_horizontal_layout_2.setObjectName("check_all_horizontal_layout_2")
        self.Check_all_box_2 = QtWidgets.QCheckBox(self.graph_grid_frame)
        self.Check_all_box_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.Check_all_box_2.setObjectName("Check_all_box_2")
        self.check_all_horizontal_layout_2.addWidget(self.Check_all_box_2)
        self.searchbar_2 = QtWidgets.QLineEdit(self.graph_grid_frame)
        self.searchbar_2.setObjectName("searchbar_2")
        self.check_all_horizontal_layout_2.addWidget(self.searchbar_2)
        self.vertical_layout_graph_right.addLayout(self.check_all_horizontal_layout_2)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.graph_grid_frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 749, 178))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.vertical_layout_graph_right.addWidget(self.scrollArea_2)
        self.horizontal_layout_gernerate_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_gernerate_button.setObjectName("horizontal_layout_gernerate_button")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_gernerate_button.addItem(spacerItem2)
        self.generate_graph = QtWidgets.QPushButton(self.graph_grid_frame)
        self.generate_graph.setObjectName("generate_graph")
        self.horizontal_layout_gernerate_button.addWidget(self.generate_graph)
        self.vertical_layout_graph_right.addLayout(self.horizontal_layout_gernerate_button)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_right, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.graph_grid_frame, 0, 0, 1, 1)
        self.stacked_pages.addWidget(self.graph_page)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)



        # settings page
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.stacked_pages.addWidget(self.settings_page)

        # names and types page setup
        self.names_types_page = QtWidgets.QWidget()
        self.names_types_page.setObjectName("names_types_page")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.names_types_page)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.check_all_horizontal_layout = QtWidgets.QHBoxLayout()
        self.check_all_horizontal_layout.setObjectName("check_all_horizontal_layout")

        # check all box and search bar setup
        self.Check_all_box = QtWidgets.QCheckBox(self.names_types_page)
        self.Check_all_box.setObjectName("Check_all_box")
        self.Check_all_box.stateChanged.connect(self.checkAll)
        self.check_all_horizontal_layout.addWidget(self.Check_all_box)
        self.Check_all_box.setEnabled(False)

        self.searchbar = QtWidgets.QLineEdit(self.names_types_page)
        self.searchbar.setObjectName("searchbar")
        self.check_all_horizontal_layout.addWidget(self.searchbar)
        self.gridLayout_3.addLayout(self.check_all_horizontal_layout, 1, 0, 1, 1)
        self.searchbar.textChanged.connect(self.handle_search)
        self.searchbar.setEnabled(False)

        # checkboxes scroll area setup
        self.scrollArea = QtWidgets.QScrollArea(self.names_types_page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 120))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.stacked_pages.addWidget(self.names_types_page)
        self.right_side_vertical_layout.addWidget(self.stacked_pages)

        # Table view setup
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.right_side_vertical_layout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.right_side_vertical_layout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.model = QStandardItemModel(self.tableView)
        self.tableView.setModel(self.model)

        # Menu and status bar
        Main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        Main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Main_window)
        self.statusbar.setObjectName("statusbar")
        Main_window.setStatusBar(self.statusbar)

        self.actionLoad_CSV = QtWidgets.QAction(Main_window)
        self.actionLoad_CSV.setObjectName("actionLoad_CSV")
        self.actionLoad_CSV.setText("Load CSV")
        self.actionLoad_CSV.triggered.connect(self.loadCSV)
        self.menuFile.addAction(self.actionLoad_CSV)

        self.actionExport_CSV = QtWidgets.QAction(Main_window)
        self.actionExport_CSV.setObjectName("actionExport_CSV")
        self.actionExport_CSV.setText("Export CSV")
        self.actionExport_CSV.triggered.connect(self.exportCSV)
        self.menuFile.addAction(self.actionExport_CSV)

        self.actionNormalizeData = QtWidgets.QAction(Main_window)
        self.actionNormalizeData.setObjectName("actionNormalizeData")
        self.actionNormalizeData.setText("Normalize Data")
        self.actionNormalizeData.triggered.connect(self.normalizeData)
        self.menuEdit.addAction(self.actionNormalizeData)

        self.actionRemoveNA = QtWidgets.QAction(Main_window)
        self.actionRemoveNA.setObjectName("actionRemoveNA")
        self.actionRemoveNA.setText("Remove N/A entries")
        self.actionRemoveNA.triggered.connect(self.removeNA)
        self.menuEdit.addAction(self.actionRemoveNA)

        self.actionExit = QtWidgets.QAction(Main_window)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("Exit")
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.types_button.clicked.connect(lambda: self.on_name_types_clicked(self.stacked_pages))
        self.graph_button.clicked.connect(lambda: self.on_graph_clicked(self.stacked_pages))
        self.settings_button.clicked.connect(lambda: self.on_settings_clicked(self.stacked_pages))


        self.retranslateUi(Main_window)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

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

    def handle_search(self, text):
        for checkbox in self.checkboxes:
            if text.lower() in checkbox.text().lower():
                checkbox.setVisible(True)
            else:
                checkbox.setVisible(False)

    def handleItemChanged(self, item):
        if item.isCheckable() and (item.checkState() == QtCore.Qt.Checked):
            for index in range(self.model.rowCount()):
                self.model.item(index, item.column()).setEnabled(False)
        elif item.isCheckable() and (item.checkState() == QtCore.Qt.Unchecked):
            for index in range(self.model.rowCount()):
                self.model.item(index, item.column()).setEnabled(True)

    def retranslateUi(self, Main_window):
        translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(translate("MainWindow", "Cell Profiler"))
        self.modules_label.setText(translate("MainWindow", "Modules"))
        self.types_button.setText(translate("MainWindow", "Names / Types"))
        self.graph_button.setText(translate("MainWindow", "Graph"))
        self.settings_button.setText(translate("MainWindow", "Settings"))
        self.file_loaded_label.setText(translate("MainWindow", "No File Loaded"))
        self.Check_all_box.setText(translate("MainWindow", "Check All"))
        self.searchbar.setPlaceholderText(translate("MainWindow", "Search for column name in table"))
        self.menuFile.setTitle(translate("MainWindow", "File"))
        self.menuEdit.setTitle(translate("MainWindow", "Edit"))
        self.menuView.setTitle(translate("MainWindow", "View"))
        self.actionLoad_CSV.setText(translate("MainWindow", "Load CSV"))
        self.actionExit.setText(translate("MainWindow", "Exit"))
        self.scatter_plot_radio.setText(translate("MainWindow", "Scatter Plot"))
        self.bar_graph_radio.setText(translate("MainWindow", "Bar Graph"))
        self.example_button.setText(translate("MainWindow", "Graph Options Example button"))
        self.Check_all_box_2.setText(translate("MainWindow", "Check All"))
        self.generate_graph.setText(translate("MainWindow", "Generate"))


    def checkAll(self, state):
        self.Check_all_box.setEnabled(True)
        self.searchbar.setEnabled(True)
        # Check or uncheck all checkboxes based on the state of the "Check All" checkbox
        for checkbox in self.checkboxes:
            checkbox.setChecked(state == QtCore.Qt.Checked)

    def normalizeData(self):
        try:
            for column in self.data.columns:
                # Check if column is numeric type
                if pd.api.types.is_numeric_dtype(self.data[column]):
                    # Replace NaN values with column mean
                    column_mean = self.data[column].mean()
                    self.data[column].fillna(column_mean, inplace=True)
                    # Perform normalization
                    min_val = self.data[column].min()
                    max_val = self.data[column].max()
                    if min_val != max_val:
                        self.data[column] = (self.data[column] - min_val) / (max_val - min_val)
                    else:
                        # Handle the case where all values in the column are the same
                        self.data[column] = np.nan

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

    def on_name_types_clicked(self, stacked_pages):
        stacked_pages.setCurrentWidget(self.names_types_page)

    def on_graph_clicked(self, stacked_pages):
        stacked_pages.setCurrentWidget(self.graph_page)

    def on_settings_clicked(self, stacked_pages):
        stacked_pages.setCurrentWidget(self.settings_page)


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())