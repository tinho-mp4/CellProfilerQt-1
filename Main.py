# File: Main.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 20, 2023,
# Last Modified: June 26, 2023 (Juned - Fixed NormalizeData)

import os
import math

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QMainWindow, \
    QDialogButtonBox, QVBoxLayout, QComboBox, QLabel, QDialog, QInputDialog

import pandas as pd
import numpy as np

import CSVHandler
from SettingsWindow import SettingWindow
from GraphPage import GraphPage


class LoadGraphThread(QThread):
    finished_loading = pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(LoadGraphThread, self).__init__(*args, **kwargs)
        self.graph_page = None

    def run(self):
        self.graph_page = GraphPage()
        self.finished_loading.emit(self.graph_page)


class LoadCSVThread(QThread):
    finished_loading = pyqtSignal(pd.DataFrame)  # Signal emitted when loading finishes

    def __init__(self, filename, *args, **kwargs):
        super(LoadCSVThread, self).__init__(*args, **kwargs)
        self.filename = filename

    def run(self):
        # Load the CSV data using pandas
        df = pd.read_csv(self.filename)
        self.finished_loading.emit(df)


class Ui_MainWindow(object):
    def __init__(self):
        self.load_thread = None
        self.graph_page = None
        self.search_text = None
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.perform_search)
        self.actionGroupColumns = None
        self.actionToggleFullScreen = None
        self.gridLayout_6 = None
        self.settings_ui = None
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

        # settings page
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.stacked_pages.addWidget(self.settings_page)

        # graph page
        self.graph_page = GraphPage()
        self.stacked_pages.addWidget(self.graph_page)

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

        self.menuEdit.addSeparator()  # Add separator before "Group Columns"

        self.actionGroupColumns = QtWidgets.QAction(Main_window)
        self.actionGroupColumns.setObjectName("actionGroupColumns")
        self.actionGroupColumns.setText("Group Columns")
        self.actionGroupColumns.triggered.connect(self.groupColumns)
        self.menuEdit.addAction(self.actionGroupColumns)

        self.actionExit = QtWidgets.QAction(Main_window)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("Exit")
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.actionToggleFullScreen = QtWidgets.QAction(Main_window)
        self.actionToggleFullScreen.setObjectName("actionToggleFullScreen")
        self.actionToggleFullScreen.setText("Toggle Full Screen")
        self.actionToggleFullScreen.triggered.connect(
            lambda: self.toggleFullScreen(Main_window, self.actionToggleFullScreen))
        self.menuView.addAction(self.actionToggleFullScreen)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.types_button.clicked.connect(lambda: self.on_name_types_clicked(self.stacked_pages))
        self.graph_button.clicked.connect(lambda: self.on_graph_clicked(self.stacked_pages))
        self.settings_button.clicked.connect(self.on_settings_clicked)

        self.retranslateUi(Main_window)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def load_graph_page(self):
        if self.graph_page is None:  # GraphPage is not yet loaded
            self.load_thread = LoadGraphThread()
            self.load_thread.finished_loading.connect(self.on_finished_loading)
            self.load_thread.start()
        else:  # GraphPage is already loaded, just switch to it
            index = self.stacked_pages.indexOf(self.graph_page)
            self.stacked_pages.setCurrentIndex(index)

    def on_finished_loading(self, graph_page):
        self.graph_page = graph_page
        self.stacked_pages.addWidget(self.graph_page)
        index = self.stacked_pages.indexOf(self.graph_page)
        self.stacked_pages.setCurrentIndex(index)

    def loadCSV(self):
        filename = CSVHandler.browse_file()
        if filename:
            self.file_loaded_label.setText(f"File Loaded: {os.path.basename(filename)}")
            self.load_thread = LoadCSVThread(filename)
            self.load_thread.finished_loading.connect(self.onFinishedLoading)
            self.load_thread.start()

    def onFinishedLoading(self, df):
        if df is not None and not df.empty:
            plate_column = next((col for col in df.columns if col.lower() == 'plate'), None)
            if plate_column:
                df[plate_column].fillna('Unknown', inplace=True)
            self.display_data(df)
            self.create_checkboxes(df.columns)
            self.Check_all_box.setChecked(True)
        else:
            error_message = "No data in the file."
            print(error_message)
            QMessageBox.warning(None, "No Data", error_message, QMessageBox.Ok)

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
            QMessageBox.critical(None, "Error", f"Error: {e}", QMessageBox.Ok, QMessageBox.Critical)

    def handle_search(self, text):
        self.search_text = text
        self.timer.start(500)

    def perform_search(self):
        text = self.search_text.lower()
        for checkbox in self.checkboxes:
            checkbox.setVisible(text in checkbox.text().lower())

    def handleItemChanged(self, item):
        if item.isCheckable() and (item.checkState() == QtCore.Qt.Checked):
            for index in range(self.model.rowCount()):
                self.model.item(index, item.column()).setEnabled(False)
        elif item.isCheckable() and (item.checkState() == QtCore.Qt.Unchecked):
            for index in range(self.model.rowCount()):
                self.model.item(index, item.column()).setEnabled(True)

    @staticmethod
    def toggleFullScreen(window, action):
        if window.isFullScreen():
            window.showNormal()
            window.setWindowState(Qt.WindowNoState)
            action.setText("Toggle Full Screen")
        else:
            window.showFullScreen()
            action.setText("Restore Normal Size")

    def checkAll(self, state):
        self.Check_all_box.setEnabled(True)
        self.searchbar.setEnabled(True)
        # Check or uncheck all checkboxes based on the state of the "Check All" checkbox
        for checkbox in self.checkboxes:
            checkbox.setChecked(state == QtCore.Qt.Checked)

    def normalizeData(self):
        try:
            if self.data is not None:
                columns_to_normalize = [col for col in self.data.columns if
                                        col not in ['PLATE', 'Metadata_Compound_Plate']]

                if len(columns_to_normalize) > 0:
                    for column in columns_to_normalize:
                        # Check if column is numeric type
                        if pd.api.types.is_numeric_dtype(self.data[column]):
                            # Replace NaN values with column mean
                            column_mean = self.data[column].mean()
                            self.data[column].fillna(column_mean, inplace=True)
                            # Perform normalization
                            column_std = self.data[column].std()
                            if math.isclose(column_std, 0):
                                # Handle the case where standard deviation is close to zero
                                self.data[column] = np.nan
                            else:
                                self.data[column] = (self.data[column] - column_mean) / column_std

                    self.display_data(self.data)
                    self.create_checkboxes(self.data.columns)
                    QMessageBox.information(
                        None, "Normalization Complete", "Data normalized successfully.", QMessageBox.Ok
                    )
                else:
                    QMessageBox.warning(
                        None, "Normalization Error", "No columns available for normalization.", QMessageBox.Ok
                    )
            else:
                QMessageBox.warning(
                    None, "Normalization Error", "No data loaded. Please load a CSV file first.", QMessageBox.Ok
                )
        except Exception as e:
            error_message = f"Error while normalizing data: {e}"
            print(error_message)
            QMessageBox.critical(None, "Normalization Error", error_message, QMessageBox.Ok, QMessageBox.Critical)

    def removeNA(self):
        try:
            if self.data is not None:
                self.data = self.data.dropna()  # Remove rows with missing values
                self.display_data(self.data)
                QMessageBox.information(
                    None, "N/A Removal", "N/A entries removed successfully.", QMessageBox.Ok
                )
            else:
                QMessageBox.warning(
                    None,
                    "N/A Removal",
                    "No data loaded. Please load a CSV file first.",
                    QMessageBox.Ok,
                )
        except Exception as e:
            error_message = f"Error while removing N/A entries: {e}"
            print(error_message)
            QMessageBox.critical(
                None, "N/A Removal Error", error_message, QMessageBox.Ok
            )

    @staticmethod
    def exportCSV(self):
        try:
            if isinstance(self.data, pd.DataFrame):  # Check if self.data is a DataFrame
                if not self.data.empty:
                    filename = CSVHandler.browse_save_file()
                    if filename:
                        CSVHandler.export_csv_file(filename, self.data)
                        success_message = f"CSV file exported successfully as {os.path.basename(filename)}"
                        print(success_message)
                        QMessageBox.information(None, "CSV Export Success", success_message, QMessageBox.Ok)
                else:
                    error_message = "No data to export. Please load a CSV file first."
                    print(error_message)
                    QMessageBox.warning(None, "Export CSV Warning", error_message, QMessageBox.Ok)
            else:
                error_message = "No CSV file loaded. Please load a CSV file first."
                print(error_message)
                QMessageBox.warning(None, "Export CSV Warning", error_message, QMessageBox.Ok)
        except Exception as e:
            error_message = f"No CSV file loaded. Please load a CSV file first."
            print(f"Unexpected error: {str(e)}")
            QMessageBox.critical(None, "Export CSV Error", error_message, QMessageBox.Ok)

    def groupColumns(self):
        try:
            if self.data is not None and not self.data.empty:
                column_dialog = QInputDialog()
                column_dialog.setWindowTitle("Select Grouping Column")
                column_dialog.setLabelText("Select a column to group by:")
                column_dialog.setComboBoxItems(self.data.columns)
                column_dialog.setComboBoxEditable(False)
                if column_dialog.exec_() == QInputDialog.Accepted:
                    grouping_column = column_dialog.textValue()
                    if grouping_column in self.data.columns:
                        numeric_columns = self.data.select_dtypes(include=np.number).columns
                        numeric_columns = [col for col in numeric_columns if col != grouping_column]
                        if len(numeric_columns) > 0:
                            grouped_data = self.data.groupby(grouping_column)[numeric_columns]
                            aggregated_data = grouped_data.mean()  # Replace 'mean' desired aggregation function

                            self.data = aggregated_data
                            self.display_data(self.data)
                            self.create_checkboxes(self.data.columns)

                            QMessageBox.information(None, "Group Columns", "Columns grouped successfully.",
                                                    QMessageBox.Ok)
                        else:
                            QMessageBox.warning(None, "Group Columns", "No numeric columns available for grouping.",
                                                QMessageBox.Ok)
                    else:
                        QMessageBox.warning(None, "Group Columns", f"Column '{grouping_column}' not found in data.",
                                            QMessageBox.Ok)
            else:
                QMessageBox.warning(None, "Group Columns", "No data available. Please load a CSV file first.",
                                    QMessageBox.Ok)
        except Exception as e:
            error_message = f"Error while grouping columns: {e}"
            print(error_message)
            QMessageBox.critical(None, "Group Columns Error", error_message, QMessageBox.Ok)

    def on_name_types_clicked(self, stacked_pages):
        stacked_pages.setCurrentWidget(self.names_types_page)

    def on_graph_clicked(self, stacked_pages):
        if self.data is not None:  # Check if data is loaded
            stacked_pages.setCurrentWidget(self.graph_page)
            self.graph_page.display_data_columns(self.data.columns)
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("No CSV Data")
            message_box.setText("No CSV data loaded. Please load a CSV file before accessing the Graph.")
            message_box.exec_()

    def on_settings_clicked(self):
        self.settings_window = SettingWindow()
        self.settings_window.show()

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


class GroupColumnsDialog(QDialog):
    def __init__(self, columns, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Group Columns")
        self.columns = columns
        self.grouped_columns = []

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        label = QLabel("Select columns to group:")
        layout.addWidget(label)

        self.column_combobox = QComboBox()
        self.column_combobox.addItems(self.columns)
        layout.addWidget(self.column_combobox)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        add_button = button_box.addButton("Add", QDialogButtonBox.ActionRole)
        add_button.clicked.connect(self.addColumn)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def addColumn(self):
        column = self.column_combobox.currentText()
        if column not in self.grouped_columns:
            self.grouped_columns.append(column)

    def getGroupedColumns(self):
        return self.grouped_columns


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
