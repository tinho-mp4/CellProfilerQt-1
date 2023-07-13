import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import XYaxisWindow


class PlotWindow(QMainWindow):
    def __init__(self, title, parent=None, position=None):
        super(PlotWindow, self).__init__(parent, Qt.Window)
        self.setWindowTitle(title)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        if position is not None:
            self.move(position)


class GraphCanvas(FigureCanvas):
    def __init__(self, fig):
        super(GraphCanvas, self).__init__(fig)
        self.setParent(None)
        self.figure = fig
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class GraphWindow(QtWidgets.QWidget):
    def __init__(self):
        super(GraphWindow, self).__init__()
        self.graph_canvas = GraphCanvas(Figure())
        self.graph_layout = QtWidgets.QVBoxLayout(self)
        self.graph_layout.addWidget(self.graph_canvas)


class GraphPage(QtWidgets.QWidget):
    def __init__(self):
        super(GraphPage, self).__init__()
        self.bar_chart_data = None
        self.xy_axis_window = XYaxisWindow.XYaxisWindow()
        self.x_axis_data = []
        self.y_axis_data = []
        self.data_frame = None
        self.data_columns = None
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

        # Left Side
        self.vertical_layout_graph_left = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_left.setObjectName("verticalLayout_4")

        self.scatter_plot_radio = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.scatter_plot_radio.setObjectName("scatter_plot_radio")
        self.scatter_plot_radio.setText("Scatter Plot")
        self.scatter_plot_radio.setChecked(True)
        self.vertical_layout_graph_left.addWidget(self.scatter_plot_radio)

        self.bar_graph_radio = QtWidgets.QRadioButton(self.graph_grid_frame)
        self.bar_graph_radio.setObjectName("bar_graph_radio")
        self.bar_graph_radio.setText("Bar Graph")
        self.vertical_layout_graph_left.addWidget(self.bar_graph_radio)

        self.xy_axis_button = QtWidgets.QPushButton(self.graph_grid_frame)
        self.xy_axis_button.setObjectName("xy_axis_button")
        self.xy_axis_button.setText("Setup X/Y Axis")
        self.vertical_layout_graph_left.addWidget(self.xy_axis_button)

        # Right Side
        self.vertical_layout_graph_right = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_right.setObjectName("vertical_layout_graph_right")

        # Search Bar / Check Box Area
        self.check_all_horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.check_all_horizontal_layout_2.setObjectName("check_all_horizontal_layout_2")
        self.check_all_box_2 = QtWidgets.QCheckBox(self.graph_grid_frame)
        self.check_all_box_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.check_all_box_2.setObjectName("Check_all_box_2")
        self.check_all_box_2.setText("Check All")
        self.check_all_box_2.setChecked(True)
        self.check_all_horizontal_layout_2.addWidget(self.check_all_box_2)
        self.searchbar_2 = QtWidgets.QLineEdit(self.graph_grid_frame)
        self.searchbar_2.setObjectName("searchbar_2")
        self.check_all_horizontal_layout_2.addWidget(self.searchbar_2)
        self.vertical_layout_graph_right.addLayout(self.check_all_horizontal_layout_2)

        # Scroll Area
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

        self.horizontal_layout_generate_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_generate_button.setObjectName("horizontal_layout_generate_button")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_generate_button.addItem(spacerItem2)

        # Generate Button
        self.generate_graph = QtWidgets.QPushButton(self.graph_grid_frame)
        self.generate_graph.setObjectName("generate_graph")
        self.generate_graph.setText("Generate")
        self.generate_graph.setEnabled(False)
        self.horizontal_layout_generate_button.addWidget(self.generate_graph)

        # Left Side PCA.. Options
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

        # Spacers
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.vertical_layout_graph_left.addItem(spacerItem1)
        self.graph_options.addItem(spacerItem3, 2, 1, 1, 1)
        self.graph_options.addItem(spacerItem4, 2, 0, 1, 1)

        self.graph_type_button_group = QButtonGroup(self)
        self.dimensionality_button_group = QButtonGroup(self)

        self.graph_type_button_group.addButton(self.scatter_plot_radio)
        self.graph_type_button_group.addButton(self.bar_graph_radio)

        self.dimensionality_button_group.addButton(self.PCA_radio_button)
        self.dimensionality_button_group.addButton(self.tSNE_radio_button)
        self.dimensionality_button_group.addButton(self.UMAP_radio_button)
        self.dimensionality_button_group.addButton(self.LDA_radio_button)

        # Layouts
        self.gridLayout_4.addLayout(self.graph_options, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.graph_grid_frame, 0, 0, 1, 1)
        self.vertical_layout_graph_right.addLayout(self.horizontal_layout_generate_button)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_right, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_left, 0, 0, 1, 1)

        # Signal Handlers
        self.check_all_box_2.stateChanged.connect(self.toggleAllCheckboxes)
        self.searchbar_2.textChanged.connect(self.handleSearch)
        self.generate_graph.clicked.connect(self.generate_graph_handler)
        self.xy_axis_button.clicked.connect(self.xy_axis_handler)

        self.checkboxes = []
        # self.graph_window = GraphWindow()

    def toggleGraphType(self):
        self.PCA_radio_button.setEnabled(self.scatter_plot_radio.isChecked())
        self.tSNE_radio_button.setEnabled(self.scatter_plot_radio.isChecked())
        self.UMAP_radio_button.setEnabled(self.scatter_plot_radio.isChecked())
        self.LDA_radio_button.setEnabled(self.scatter_plot_radio.isChecked())

    def toggleDimensionalityScaling(self):
        self.scatter_plot_radio.setEnabled(
            self.PCA_radio_button.isChecked()
            or self.tSNE_radio_button.isChecked()
            or self.UMAP_radio_button.isChecked()
            or self.LDA_radio_button.isChecked())

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
        if len(self.search_text) > 2:
            self.timer.start(1000)

    def perform_search(self):
        text = self.search_text.lower()
        for checkbox in self.checkboxes:
            checkbox.setVisible(text in checkbox.text().lower())

    def generate_graph_handler(self):

        # redundant code?

        # selected_columns = []
        # for checkbox in self.checkboxes:
        #     if checkbox.isChecked():
        #         selected_columns.append(checkbox.text())
        #
        # graph_type = "scatter" if self.scatter_plot_radio.isChecked() else "bar"
        #
        # dimensionality_reduction = ""
        # if self.PCA_radio_button.isChecked():
        #     dimensionality_reduction = "PCA"
        # elif self.tSNE_radio_button.isChecked():
        #     dimensionality_reduction = "t-SNE"
        # elif self.UMAP_radio_button.isChecked():
        #     dimensionality_reduction = "UMAP"
        #
        # self.generate_graph_with_columns(selected_columns, graph_type, dimensionality_reduction)

        self.x_axis_data = self.xy_axis_window.getxAxisData()
        self.y_axis_data = self.xy_axis_window.getyAxisData()
        self.bar_chart_data = self.xy_axis_window.getBarChartColumnData()

        # display scatter or bar chart
        if self.scatter_plot_radio.isChecked():
            graphWindow = PlotWindow('Plot 1', self)
            graphWindow.move(0, 0)
            ax = graphWindow.figure.add_subplot(111)
            ax.plot(self.x_axis_data, self.y_axis_data, 'o')
            graphWindow.show()
        else:
            graphWindow = PlotWindow('Plot 1', self)
            graphWindow.move(0, 0)
            ax = graphWindow.figure.add_subplot(111)
            ax.bar(np.arange(len(self.bar_chart_data)), self.bar_chart_data)
            graphWindow.show()




    def generate_graph_with_columns(self, columns, graph_type, dimensionality_reduction):
        data = self.data_frame[columns]

        if dimensionality_reduction == "PCA":
            reducer = PCA(n_components=2)
        elif dimensionality_reduction == "t-SNE":
            reducer = TSNE(n_components=2)
        elif dimensionality_reduction == "UMAP":
            reducer = umap.UMAP()
        else:
            return

        reduced_data = reducer.fit_transform(data)

        self.graph_window.graph_canvas.figure.clear()

        if graph_type == "scatter":
            self.graph_window.graph_canvas.axes.scatter(reduced_data[:, 0], reduced_data[:, 1])
            self.graph_window.graph_canvas.axes.set_xlabel("Component 1")
            self.graph_window.graph_canvas.axes.set_ylabel("Component 2")
            self.graph_window.graph_canvas.axes.set_title("Scatter Plot")

        elif graph_type == "bar":
            self.graph_window.graph_canvas.axes.bar(range(len(columns)), reduced_data)
            self.graph_window.graph_canvas.axes.set_xlabel("Columns")
            self.graph_window.graph_canvas.axes.set_ylabel("Values")
            self.graph_window.graph_canvas.axes.set_title("Bar Chart")
            self.graph_window.graph_canvas.axes.set_xticks(range(len(columns)))
            self.graph_window.graph_canvas.axes.set_xticklabels(columns, rotation=90)

        self.graph_window.graph_canvas.draw()
        self.graph_window.show()

    def update_graph(self):
        x_columns = self.xy_axis_window.getxAxisData()
        y_columns = self.xy_axis_window.getyAxisData()

        if x_columns and y_columns:
            graph_type = "scatter" if self.scatter_plot_radio.isChecked() else "bar"

            if self.PCA_radio_button.isChecked() \
                    or self.tSNE_radio_button.isChecked() or self.UMAP_radio_button.isChecked():
                dimensionality_reduction = ""
                if self.PCA_radio_button.isChecked():
                    dimensionality_reduction = "PCA"
                elif self.tSNE_radio_button.isChecked():
                    dimensionality_reduction = "t-SNE"
                elif self.UMAP_radio_button.isChecked():
                    dimensionality_reduction = "UMAP"

                # Declare the reducer variable
                reducer = None

                # Perform dimensionality reduction if a method is selected
                if dimensionality_reduction == "PCA":
                    reducer = PCA(n_components=2)
                elif dimensionality_reduction == "t-SNE":
                    reducer = TSNE(n_components=2)
                elif dimensionality_reduction == "UMAP":
                    reducer = umap.UMAP()

                if reducer is not None:
                    # Reduce the data to 2 dimensions
                    data = self.data_frame[x_columns + y_columns]
                    reduced_data = reducer.fit_transform(data)
                    x_data = reduced_data[:, 0]
                    y_data = reduced_data[:, 1]
                else:
                    # Use original data without dimensionality reduction
                    x_data = self.data_frame[x_columns].values
                    y_data = self.data_frame[y_columns].values
            else:
                # Use original data without dimensionality reduction
                x_data = self.data_frame[x_columns].values
                y_data = self.data_frame[y_columns].values

            self.graph_window.graph_canvas.figure.clear()

            if graph_type == "scatter":
                self.graph_window.graph_canvas.axes.scatter(x_data, y_data)
                self.graph_window.graph_canvas.axes.set_xlabel("X Axis")
                self.graph_window.graph_canvas.axes.set_ylabel("Y Axis")
                self.graph_window.graph_canvas.axes.set_title("Scatter Plot")

            elif graph_type == "bar":
                x_ticks = np.arange(len(x_columns))
                self.graph_window.graph_canvas.axes.bar(x_ticks, y_data)
                self.graph_window.graph_canvas.axes.set_xlabel("X Axis")
                self.graph_window.graph_canvas.axes.set_ylabel("Y Axis")
                self.graph_window.graph_canvas.axes.set_title("Bar Chart")
                self.graph_window.graph_canvas.axes.set_xticks(x_ticks)
                self.graph_window.graph_canvas.axes.set_xticklabels(x_columns, rotation=90)

            self.graph_window.graph_canvas.draw()

    def setupXyWindow(self):
        self.xy_axis_window.set_table_data_frame(self.data_frame)
        self.xy_axis_window.setGenerateButton(self.generate_graph)
        for column in self.data_columns:
            self.xy_axis_window.xAxisColumn_comboBox.addItemToComboBox(column)
            self.xy_axis_window.xAxisColumn2_comboBox.addItemToComboBox(column)
            self.xy_axis_window.yAxis_comboBox.addItemToComboBox(column)
            self.xy_axis_window.barChartColumn_combobox.addItemToComboBox(column)

    def xy_axis_handler(self):
        if self.scatter_plot_radio.isChecked():
            self.xy_axis_window.displayPage(1)
        elif self.bar_graph_radio.isChecked():
            self.xy_axis_window.displayPage(2)
        # Load saved data if available
        self.xy_axis_window.load_saved_data()
        self.xy_axis_window.show()

    def handle_x_axis_data(self):
        self.x_axis_data = self.xy_axis_window.getxAxisData()

    def set_table_data_columns(self, columns):
        self.data_columns = columns

    def set_table_data_frame(self, data_frame):
        self.data_frame = data_frame
