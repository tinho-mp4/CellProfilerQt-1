import matplotlib.pyplot as plt
import umap
from PyQt5 import QtWidgets, QtCore
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from XaxisWindow import *


class GraphPage(QtWidgets.QWidget):
    def __init__(self):
        super(GraphPage, self).__init__()
        self.search_text = None
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.perform_search)
        self.setEnabled(True)
        self.setObjectName("graph_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graph_grid_frame = QtWidgets.QFrame(self)
        self.graph_grid_frame.setObjectName("graph_grid_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.graph_grid_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")


        # left side
        self.vertical_layout_graph_left = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_left.setObjectName("verticalLayout_4")

        self.scatter_plot_radio = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.scatter_plot_radio.setObjectName("scatter_plot_radio")
        self.scatter_plot_radio.setText("Scatter Plot")
        self.vertical_layout_graph_left.addWidget(self.scatter_plot_radio)

        self.bar_graph_radio = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.bar_graph_radio.setObjectName("bar_graph_radio")
        self.bar_graph_radio.setText("Bar Graph")
        self.vertical_layout_graph_left.addWidget(self.bar_graph_radio)

        self.x_axis_button = QtWidgets.QPushButton(self.graph_grid_frame)
        self.x_axis_button.setObjectName("x_axis_button")
        self.x_axis_button.setText("X-Axis")
        self.vertical_layout_graph_left.addWidget(self.x_axis_button)

        self.y_axis_button = QtWidgets.QPushButton(self.graph_grid_frame)
        self.y_axis_button.setObjectName("y_axis_button")
        self.y_axis_button.setText("Y-Axis")
        self.vertical_layout_graph_left.addWidget(self.y_axis_button)




        # right side

        self.vertical_layout_graph_right = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_right.setObjectName("vertical_layout_graph_right")

        # search bar / check box area
        self.check_all_horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.check_all_horizontal_layout_2.setObjectName("check_all_horizontal_layout_2")
        self.check_all_box_2 = QtWidgets.QCheckBox(self.graph_grid_frame)
        self.check_all_box_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.check_all_box_2.setObjectName("Check_all_box_2")
        self.check_all_box_2.setText("Check All")
        self.check_all_horizontal_layout_2.addWidget(self.check_all_box_2)
        self.searchbar_2 = QtWidgets.QLineEdit(self.graph_grid_frame)
        self.searchbar_2.setObjectName("searchbar_2")
        self.check_all_horizontal_layout_2.addWidget(self.searchbar_2)
        self.vertical_layout_graph_right.addLayout(self.check_all_horizontal_layout_2)

        # scroll area
        self.scrollArea_2 = QtWidgets.QScrollArea(self.graph_grid_frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 662, 178))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.vertical_layout_graph_right.addWidget(self.scrollArea_2)


        self.horizontal_layout_gernerate_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_gernerate_button.setObjectName("horizontal_layout_gernerate_button")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_gernerate_button.addItem(spacerItem2)

        # generate button
        self.generate_graph = QtWidgets.QPushButton(self.graph_grid_frame)
        self.generate_graph.setObjectName("generate_graph")
        self.generate_graph.setText("Generate")
        self.horizontal_layout_gernerate_button.addWidget(self.generate_graph)


        # left side PCA.. Options
        self.graph_options = QtWidgets.QGridLayout()
        self.graph_options.setObjectName("graph_options")

        self.PCA_radio_button = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.PCA_radio_button.setObjectName("PCA_radio_button")
        self.PCA_radio_button.setText("PCA")
        self.graph_options.addWidget(self.PCA_radio_button, 0, 0, 1, 1)

        self.tSNE_radio_button = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.tSNE_radio_button.setObjectName("tSNE_radio_button")
        self.tSNE_radio_button.setText("t-SNE")
        self.graph_options.addWidget(self.tSNE_radio_button, 0, 1, 1, 1)

        self.UMAP_radio_button = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.UMAP_radio_button.setObjectName("UMAP_radio_button")
        self.UMAP_radio_button.setText("UMAP")
        self.graph_options.addWidget(self.UMAP_radio_button, 1, 0, 1, 1)

        self.LDA_radio_button = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.LDA_radio_button.setObjectName("LDA_radio_button")
        self.LDA_radio_button.setText("LDA")
        self.graph_options.addWidget(self.LDA_radio_button, 1, 1, 1, 1)



        # spacers
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.vertical_layout_graph_left.addItem(spacerItem1)
        self.graph_options.addItem(spacerItem3, 2, 1, 1, 1)
        self.graph_options.addItem(spacerItem4, 2, 0, 1, 1)

        # layouts
        self.gridLayout_4.addLayout(self.graph_options, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.graph_grid_frame, 0, 0, 1, 1)
        self.vertical_layout_graph_right.addLayout(self.horizontal_layout_gernerate_button)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_right, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_left, 0, 0, 1, 1)

        # Connect the signal handlers
        self.check_all_box_2.stateChanged.connect(self.toggleAllCheckboxes)
        self.searchbar_2.textChanged.connect(self.handleSearch)
        self.generate_graph.clicked.connect(self.generate_graph_handler)
        self.x_axis_button.clicked.connect(lambda: self.x_axis_handler())

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
        self.search_text = text
        self.timer.stop()
        self.timer.start(500)

    def perform_search(self):
        text = self.search_text.lower()
        for checkbox in self.checkboxes:
            checkbox.setVisible(text in checkbox.text().lower())

    def generate_graph_handler(self):
        selected_columns = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                selected_columns.append(checkbox.text())

        graph_type = "scatter" if self.scatter_plot_radio.isChecked() else "bar"

        dimensionality_reduction = ""
        if self.PCA_radio_button.isChecked():
            dimensionality_reduction = "PCA"
        elif self.tSNE_radio_button.isChecked():
            dimensionality_reduction = "t-SNE"
        elif self.UMAP_radio_button.isChecked():
            dimensionality_reduction = "UMAP"

        # Perform the graph generation using the selected columns and options
        self.generate_graph_with_columns(selected_columns, graph_type, dimensionality_reduction)

    def generate_graph_with_columns(self, columns, graph_type, dimensionality_reduction):
        # Perform the graph generation using the selected columns and options
        data = self.data[columns]  # Retrieve the selected columns from the loaded data

        if dimensionality_reduction == "PCA":
            reducer = PCA(n_components=2)
        elif dimensionality_reduction == "t-SNE":
            reducer = TSNE(n_components=2)
        elif dimensionality_reduction == "UMAP":
            reducer = umap.UMAP()
        else:
            return

        reduced_data = reducer.fit_transform(data)

        if graph_type == "scatter":
            plt.scatter(reduced_data[:, 0], reduced_data[:, 1])
            plt.xlabel("Component 1")
            plt.ylabel("Component 2")
            plt.title("Scatter Plot")
            plt.show()
        elif graph_type == "bar":
            plt.bar(range(len(columns)), reduced_data)
            plt.xlabel("Columns")
            plt.ylabel("Values")
            plt.title("Bar Chart")
            plt.xticks(range(len(columns)), columns, rotation=90)
            plt.show()

    def x_axis_handler(self):
        self.x_axis_window = XaxisWindow()
        self.x_axis_window.show()


