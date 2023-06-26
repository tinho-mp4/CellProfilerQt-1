# File: GraphPage.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 26, 2023,
# Last Modified: June 26, 2023 (Juned - Displaying Data)

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize, QRect, Qt



class GraphPage(QtWidgets.QWidget):
    def __init__(self):
        super(GraphPage, self).__init__()
        self.setEnabled(True)
        self.setObjectName("graph_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graph_grid_frame = QtWidgets.QFrame(self)
        self.graph_grid_frame.setObjectName("graph_grid_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.graph_grid_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # Left section with radio buttons
        self.vertical_layout_graph_left = QtWidgets.QVBoxLayout(self.graph_grid_frame)
        self.vertical_layout_graph_left.setObjectName("vertical_layout_graph_left")
        self.scatter_plot_radio = QtWidgets.QRadioButton("Scatter Plot", self.graph_grid_frame)
        self.scatter_plot_radio.setObjectName("scatter_plot_radio")
        self.vertical_layout_graph_left.addWidget(self.scatter_plot_radio)
        self.bar_graph_radio = QtWidgets.QRadioButton("Bar Graph", self.graph_grid_frame)
        self.bar_graph_radio.setObjectName("bar_graph_radio")
        self.vertical_layout_graph_left.addWidget(self.bar_graph_radio)
        self.histogram_radio = QtWidgets.QRadioButton("Histogram", self.graph_grid_frame)
        self.histogram_radio.setObjectName("histogram_radio")
        self.vertical_layout_graph_left.addWidget(self.histogram_radio)
        self.vertical_layout_graph_left.addStretch(1)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_left, 0, 0, 1, 1)

        # Right section with checkboxes and scroll area
        self.vertical_layout_graph_right = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_right.setObjectName("vertical_layout_graph_right")

        self.check_all_horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.check_all_horizontal_layout_2.setObjectName("check_all_horizontal_layout_2")
        self.Check_all_box_2 = QtWidgets.QCheckBox(self.graph_grid_frame)
        self.Check_all_box_2.setSizeIncrement(QSize(0, 0))
        self.Check_all_box_2.setObjectName("Check_all_box_2")
        self.Check_all_box_2.setChecked(True)
        self.Check_all_box_2.setText("Check All")
        self.check_all_horizontal_layout_2.addWidget(self.Check_all_box_2)
        self.searchbar_2 = QtWidgets.QLineEdit(self.graph_grid_frame)
        self.searchbar_2.setObjectName("searchbar_2")
        self.check_all_horizontal_layout_2.addWidget(self.searchbar_2)
        self.vertical_layout_graph_right.addLayout(self.check_all_horizontal_layout_2)

        self.scrollArea_2 = QtWidgets.QScrollArea(self.graph_grid_frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget(self.scrollArea_2)
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 200, 200))  # Set the initial size

        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.vertical_layout_graph_right.addWidget(self.scrollArea_2)

        self.horizontal_layout_generate_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_generate_button.setObjectName("horizontal_layout_generate_button")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_generate_button.addItem(spacerItem2)
        self.generate_graph = QtWidgets.QPushButton("Generate", self.graph_grid_frame)
        self.generate_graph.setObjectName("generate_graph")
        self.horizontal_layout_generate_button.addWidget(self.generate_graph)
        self.vertical_layout_graph_right.addLayout(self.horizontal_layout_generate_button)

        self.gridLayout_4.addLayout(self.vertical_layout_graph_right, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.graph_grid_frame, 0, 0, 1, 1)

        # Connect the signal handlers
        self.Check_all_box_2.stateChanged.connect(self.toggleAllCheckboxes)
        self.searchbar_2.textChanged.connect(self.handleSearch)
        self.generate_graph.clicked.connect(self.generate_graph_handler)

        self.checkboxes = []

    def display_data_columns(self, columns):
        for i in range(self.gridLayout_5.count()):
            widget = self.gridLayout_5.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        self.checkboxes = []
        for i, column in enumerate(columns):
            checkbox = QtWidgets.QCheckBox(column, self.scrollAreaWidgetContents_2)
            checkbox.setChecked(True)
            self.gridLayout_5.addWidget(checkbox, i, 0, 1, 1)
            self.checkboxes.append(checkbox)

    def toggleAllCheckboxes(self, state):
        for checkbox in self.checkboxes:
            checkbox.setChecked(state == QtCore.Qt.Checked)

    def handleSearch(self, text):
        for checkbox in self.checkboxes:
            checkbox.setVisible(text.lower() in checkbox.text().lower())

            if checkbox.isVisible() and checkbox.isChecked():
                checkbox.setVisible(True)  # Ensure the checkbox is visible if it matches the search text

        # Update the size of the scroll area's contents to reflect the visibility changes
        self.scrollAreaWidgetContents_2.adjustSize()

    def generate_graph_handler(self):
        selected_columns = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                selected_columns.append(checkbox.text())

        # Perform the graph generation using the selected columns
        self.generate_graph_with_columns(selected_columns)
