# File: Main.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 20, 2023 (Today's Date)
# Last Modified: June 20, 2023 (Anush Varma - Initial commit)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QWidget


# File: Main.py | Cell Profiler: User-friendly software for .csv data analysis, manipulation, and visualization.

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cell Profiler")
        MainWindow.resize(760, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Horizontal layout
        self.split_left_right_layout = QtWidgets.QHBoxLayout()
        self.split_left_right_layout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.split_left_right_layout)

        # Modules section
        self.left_side_vertical_layout = QtWidgets.QVBoxLayout()
        self.left_side_vertical_layout.setObjectName("verticalLayout_2")
        self.modules_label = QtWidgets.QLabel(self.centralwidget)
        self.modules_label.setObjectName("modules_label")
        self.left_side_vertical_layout.addWidget(self.modules_label)
        self.types_button = QtWidgets.QPushButton(self.centralwidget)
        self.types_button.setObjectName("types_button")
        self.left_side_vertical_layout.addWidget(self.types_button)
        self.graph_button = QtWidgets.QPushButton(self.centralwidget)
        self.graph_button.setObjectName("graph_button")
        self.left_side_vertical_layout.addWidget(self.graph_button)
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setObjectName("settings_button")
        self.left_side_vertical_layout.addWidget(self.settings_button)
        self.left_side_vertical_layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.split_left_right_layout.addLayout(self.left_side_vertical_layout)

        # Data section

        self.images_page = QtGui.QPageLayout

        self.right_side_vertical = QtWidgets.QVBoxLayout()
        self.right_side_vertical.setObjectName("verticalLayout_3")
        self.file_loaded_label = QtWidgets.QLabel(self.centralwidget)
        self.file_loaded_label.setObjectName("file_loaded_label")


        self.right_side_vertical.addWidget(self.file_loaded_label)


        # pages to change modules
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidgetPages")
        self.stackedWidget.setEnabled(True)
        self.names_types_page = QWidget()
        self.names_types_page.setObjectName("Images_page")

        self.Check_all_box = QtWidgets.QCheckBox(self.names_types_page)
        self.Check_all_box.setObjectName("Check_all_box")
        self.right_side_vertical.addWidget(self.Check_all_box)

        # Scrollable area
        self.scrollArea = QtWidgets.QScrollArea(self.names_types_page)
        self.Check_all_box.stateChanged.connect(self.checkAll)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        # check boxes
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 6, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 3, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.right_side_vertical.addWidget(self.scrollArea)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.right_side_vertical.addWidget(self.tableView)
        self.split_left_right_layout.addLayout(self.right_side_vertical)

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
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.settings_button, self.graph_button)
        MainWindow.setTabOrder(self.graph_button, self.types_button)

    def retranslateUi(self, MainWindow):
        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "Cell Profiler"))
        self.modules_label.setText(translate("MainWindow", "Modules"))
        self.types_button.setText(translate("MainWindow", "Names / Types"))
        self.graph_button.setText(translate("MainWindow", "Graph"))
        self.settings_button.setText(translate("MainWindow", "Settings"))
        self.file_loaded_label.setText(translate("MainWindow", "No File Loaded"))
        self.Check_all_box.setText(translate("MainWindow", "Check All"))
        checkboxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                      self.checkBox_6, self.checkBox_7]
        checkbox_texts = ["CheckBox"] * len(checkboxes)
        for checkbox, text in zip(checkboxes, checkbox_texts):
            checkbox.setText(translate("MainWindow", text))
        self.menuFile.setTitle(translate("MainWindow", "File"))
        self.menuEdit.setTitle(translate("MainWindow", "Edit"))
        self.menuView.setTitle(translate("MainWindow", "View"))
        self.actionLoad_CSV.setText(translate("MainWindow", "Load CSV"))
        self.actionExit.setText(translate("MainWindow", "Exit"))

    def checkAll(self, state):
        # Check or uncheck all checkboxes based on the state of the "Check All" checkbox
        checkboxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                      self.checkBox_6, self.checkBox_7]
        for checkbox in checkboxes:
            checkbox.setChecked(state == QtCore.Qt.Checked)


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
