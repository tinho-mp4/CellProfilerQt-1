# File: GraphPage.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 26, 2023,
# Last Modified: June 26, 2023 (Juned - Fixed the search and check all for the GraphPage.py)

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

        # right side

        self.vertical_layout_graph_right = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_right.setObjectName("vertical_layout_graph_right")

        self.check_all_horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.check_all_horizontal_layout_2.setObjectName("check_all_horizontal_layout_2")
        self.check_all_box_2 = QtWidgets.QCheckBox(self.graph_grid_frame)
        self.check_all_box_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.check_all_box_2.setObjectName("Check_all_box_2")
        self.check_all_box_2.setText("Check All")
        self.check_all_horizontal_layout_2.addWidget(self.check_all_box_2)
        self.searchbar_2 = QtWidgets.QLineEdit(self.graph_grid_frame)
        self.searchbar_2.setObjectName("searchbar_2")
        self.searchbar_2.setPlaceholderText("Search for column name in table")
        self.check_all_horizontal_layout_2.addWidget(self.searchbar_2)

        self.vertical_layout_graph_right.addLayout(self.check_all_horizontal_layout_2)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.graph_grid_frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 569, 178))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.vertical_layout_graph_right.addWidget(self.scrollArea_2)

        self.horizontal_layout_generate_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_generate_button.setObjectName("horizontal_layout_generate_button")
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_generate_button.addItem(spacer_item1)
        self.generate_graph = QtWidgets.QPushButton(self.graph_grid_frame)
        self.generate_graph.setObjectName("generate_graph")
        self.generate_graph.setText("Generate")
        self.horizontal_layout_generate_button.addWidget(self.generate_graph)
        self.vertical_layout_graph_right.addLayout(self.horizontal_layout_generate_button)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_right, 0, 4, 1, 1)

        # left side

        # graph options (placeholder buttons)
        self.graph_options = QtWidgets.QGridLayout()
        self.graph_options.setObjectName("graph_options")

        self.place_holder_button1 = QtWidgets.QPushButton(self.graph_grid_frame)
        self.place_holder_button1.setObjectName("place_holder_button1")
        self.place_holder_button1.setText("Example button 1")
        self.graph_options.addWidget(self.place_holder_button1, 0, 0, 1, 1)

        self.place_holder_button2 = QtWidgets.QPushButton(self.graph_grid_frame)
        self.place_holder_button2.setObjectName("place_holder_button2")
        self.place_holder_button2.setText("Example button 2")
        self.graph_options.addWidget(self.place_holder_button2, 0, 1, 1, 1)

        self.place_holder_button3 = QtWidgets.QPushButton(self.graph_grid_frame)
        self.place_holder_button3.setObjectName("place_holder_button3")
        self.place_holder_button3.setText("Example button 3")
        self.graph_options.addWidget(self.place_holder_button3, 1, 0, 1, 1)

        self.place_holder_button4 = QtWidgets.QPushButton(self.graph_grid_frame)
        self.place_holder_button4.setObjectName("place_holder_button4")
        self.place_holder_button4.setText("Example button 4")
        self.graph_options.addWidget(self.place_holder_button4, 1, 1, 1, 1)

        spacer_item2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.graph_options.addItem(spacer_item2, 2, 1, 1, 1)

        spacer_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.graph_options.addItem(spacer_item3, 2, 0, 1, 1)

        self.gridLayout_4.addLayout(self.graph_options, 0, 3, 1, 1)


        # graph types (scatter/bar/example button)
        self.vertical_layout_graph_left = QtWidgets.QWidget(self.graph_grid_frame)
        self.vertical_layout_graph_left.setObjectName("vertical_layout_graph_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.vertical_layout_graph_left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scatter_plot_radio = QtWidgets.QRadioButton(self.vertical_layout_graph_left)
        self.scatter_plot_radio.setObjectName("scatter_plot_radio")
        self.scatter_plot_radio.setText("Scatter Plot")

        self.verticalLayout.addWidget(self.scatter_plot_radio)
        self.bar_graph_radio = QtWidgets.QRadioButton(self.vertical_layout_graph_left)
        self.bar_graph_radio.setObjectName("bar_graph_radio")
        self.bar_graph_radio.setText("Bar Graph")
        self.verticalLayout.addWidget(self.bar_graph_radio)

        self.example_button = QtWidgets.QCheckBox(self.vertical_layout_graph_left)
        self.example_button.setObjectName("example_button")
        self.example_button.setText("Graph Options Example button")
        self.verticalLayout.addWidget(self.example_button)

        spacer_item4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item4)
        self.gridLayout_4.addWidget(self.vertical_layout_graph_left, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.graph_grid_frame, 0, 0, 1, 1)

        # Connect the signal handlers
        self.check_all_box_2.stateChanged.connect(self.toggleAllCheckboxes)
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
