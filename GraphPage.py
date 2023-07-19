import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

import XYaxisWindow


class PlotWindow(QMainWindow):
    """
    A window for displaying a plot.
    """

    def __init__(self, title, parent=None, position=None):
        """
        Initializes the PlotWindow.

        Args:
            title (str): The title of the window.
            parent (QWidget): The parent widget.
            position (QPoint): The position of the window.
        """
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


def applyClustering(data):
    """
    Applies clustering to the data.

    Args:
        data (np.ndarray): The data to be clustered.

    Returns:
        np.ndarray: The clustered data.
    """
    # Apply clustering algorithm (e.g., KMeans) to the data
    kmeans = KMeans(n_clusters=3)  # Adjust the number of clusters as needed
    clusters = kmeans.fit_predict(data)

    return clusters


class GraphPage(QtWidgets.QWidget):
    """
    A class representing a graphical page for displaying and interacting with graphs.
    """

    def __init__(self):
        """
         Initializes the GraphPage.
         """
        super(GraphPage, self).__init__()
        self.graph_window = None
        self.bar_chart_data = None
        self.xy_axis_window = XYaxisWindow.XYaxisWindow()
        self.x_axis_data = []
        self.y_axis_data = []
        self.data_frame = None
        self.data_columns = None
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

        self.scatter_plot_radio.clicked.connect(self.toggleGraphType)
        self.bar_graph_radio.clicked.connect(self.toggleGraphType)

        self.xy_axis_button = QtWidgets.QPushButton(self.graph_grid_frame)
        self.xy_axis_button.setObjectName("xy_axis_button")
        self.xy_axis_button.setText("Setup X/Y Axis")
        self.vertical_layout_graph_left.addWidget(self.xy_axis_button)
        # left side spacer
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_graph_left.addItem(spacerItem1)

        self.gridLayout_4.addLayout(self.vertical_layout_graph_left, 0, 0, 1, 1)

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

        # graph options spacers
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.graph_options.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.graph_options.addItem(spacerItem3, 2, 0, 1, 1)

        self.gridLayout_4.addLayout(self.graph_options, 0, 2, 1, 1)

        # Right Side
        self.vertical_layout_graph_right = QtWidgets.QVBoxLayout()
        self.vertical_layout_graph_right.setObjectName("vertical_layout_graph_right")

        # cluster button setup
        self.cluster_horizontal_layout = QtWidgets.QHBoxLayout()
        self.cluster_horizontal_layout.setObjectName("cluster_horizontal_layout")

        self.cluster = QtWidgets.QCheckBox(self.graph_grid_frame)
        self.cluster.setObjectName("cluster")
        self.cluster.setText("Cluster")
        self.cluster_horizontal_layout.addWidget(self.cluster)
        self.vertical_layout_graph_right.addLayout(self.cluster_horizontal_layout)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_graph_right.addItem(spacerItem4)

        self.horizontal_layout_generate_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_generate_button.setObjectName("horizontal_layout_generate_button")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_generate_button.addItem(spacerItem5)

        # Generate Button
        self.generate_graph = QtWidgets.QPushButton(self.graph_grid_frame)
        self.generate_graph.setObjectName("generate_graph")
        self.generate_graph.setText("Generate")
        self.generate_graph.setEnabled(False)
        self.horizontal_layout_generate_button.addWidget(self.generate_graph)
        self.vertical_layout_graph_right.addLayout(self.cluster_horizontal_layout)

        self.graph_type_button_group = QButtonGroup(self)
        self.dimensionality_button_group = QButtonGroup(self)

        self.graph_type_button_group.addButton(self.scatter_plot_radio)
        self.graph_type_button_group.addButton(self.bar_graph_radio)

        self.dimensionality_button_group.addButton(self.PCA_radio_button)
        self.dimensionality_button_group.addButton(self.tSNE_radio_button)
        self.dimensionality_button_group.addButton(self.UMAP_radio_button)
        self.dimensionality_button_group.addButton(self.LDA_radio_button)

        self.vertical_layout_graph_right.addLayout(self.horizontal_layout_generate_button)
        self.gridLayout_4.addLayout(self.vertical_layout_graph_right, 0, 3, 1, 1)
        self.gridLayout_7.addWidget(self.graph_grid_frame, 0, 0, 1, 1)

        # Signal Handlers
        self.generate_graph.clicked.connect(self.generateGraphHandler)
        self.xy_axis_button.clicked.connect(self.xyAxisHandler)

        self.checkboxes = []

    def toggleGraphType(self):
        """
        Enables or disables radio buttons and checkboxes based on the selected graph type.
        """
        self.PCA_radio_button.setEnabled(self.scatter_plot_radio.isChecked())
        self.tSNE_radio_button.setEnabled(self.scatter_plot_radio.isChecked())
        self.UMAP_radio_button.setEnabled(self.scatter_plot_radio.isChecked())
        self.LDA_radio_button.setEnabled(self.scatter_plot_radio.isChecked())

        # Enable or disable the "Cluster" checkbox based on the selected graph type
        self.cluster.setEnabled(self.scatter_plot_radio.isChecked())

    def toggleDimensionalityScaling(self):
        """
        Enables or disables the scatter plot radio button based on the selected dimensionality scaling options.
        """
        self.scatter_plot_radio.setEnabled(
            self.PCA_radio_button.isChecked()
            or self.tSNE_radio_button.isChecked()
            or self.UMAP_radio_button.isChecked()
            or self.LDA_radio_button.isChecked())

    def generateGraphHandler(self):
        """
        Generates and displays the selected graph based on the user's inputs.
        """
        self.x_axis_data = self.xy_axis_window.getxAxisData()
        self.y_axis_data = self.xy_axis_window.getyAxisData()
        self.bar_chart_data = self.xy_axis_window.getBarChartColumnData()

        # Display scatter or bar chart based on the selected radio button
        if self.scatter_plot_radio.isChecked():
            # Create a scatter plot
            graphWindow = PlotWindow('Plot 1', self)
            graphWindow.move(0, 0)
            ax = graphWindow.figure.add_subplot(111)

            if self.cluster.isChecked():
                data = np.column_stack((self.x_axis_data, self.y_axis_data))
                clusters = self.applyClustering(data)
                ax.scatter(self.x_axis_data, self.y_axis_data, c=clusters)
            else:
                ax.plot(self.x_axis_data, self.y_axis_data, 'o')

            ax.set_xlabel(str(self.xy_axis_window.xAxisColumn2_comboBox.currentText()))
            ax.set_ylabel(str(self.xy_axis_window.yAxis_comboBox.currentText()))
            graphWindow.show()
        else:
            # Create a bar chart
            graphWindow = PlotWindow('Plot 1', self)
            graphWindow.move(0, 0)
            ax = graphWindow.figure.add_subplot(111)
            ax.bar(np.arange(len(self.bar_chart_data)), self.bar_chart_data)
            ax.set_xlabel("Well")
            ax.set_ylabel(self.xy_axis_window.barChartColumn_combobox.currentText())
            graphWindow.show()

    def applyClustering(self, data):
        """
        Applies clustering to the data.

        Args:
            data (np.ndarray): The data to be clustered.

        Returns:
            np.ndarray: The clustered data.
        """
        # Apply clustering algorithm (e.g., KMeans) to the data
        kmeans = KMeans(n_clusters=3, n_init=10)  # Adjust the number of clusters as needed
        clusters = kmeans.fit_predict(data)

        return clusters

    def setupXyWindow(self):
        """
        Sets up the XY Axis Window with data and options.
        """
        self.xy_axis_window.set_table_dataframe(self.data_frame)
        self.xy_axis_window.setGenerateButton(self.generate_graph)
        self.xy_axis_window.xAxisColumn_comboBox.clear()
        self.xy_axis_window.xAxisColumn2_comboBox.clear()
        self.xy_axis_window.yAxis_comboBox.clear()
        self.xy_axis_window.barChartColumn_combobox.clear()
        for column in self.data_columns:
            self.xy_axis_window.xAxisColumn_comboBox.addItemToComboBox(column)
            self.xy_axis_window.xAxisColumn2_comboBox.addItemToComboBox(column)
            self.xy_axis_window.yAxis_comboBox.addItemToComboBox(column)
            self.xy_axis_window.barChartColumn_combobox.addItemToComboBox(column)

    def xyAxisHandler(self):
        """
        Handles the action when the XY Axis button is clicked.
        """
        if self.scatter_plot_radio.isChecked():
            self.xy_axis_window.displayPage(1)
        elif self.bar_graph_radio.isChecked():
            self.xy_axis_window.displayPage(2)
        # Load saved data if available
        self.xy_axis_window.loadSavedData()
        self.xy_axis_window.show()

    def handleXAxisData(self):
        """
        Handles the X-axis data from the XY Axis Window.
        """
        self.x_axis_data = self.xy_axis_window.getxAxisData()

    def setTableDataColumns(self, columns):
        """
        Sets the columns of the table data.

        Args:
            columns (list): The list of column names.
        """
        self.data_columns = columns

    def setTableDataFrame(self, data_frame):
        """
        Sets the data frame of the table.

        Args:
            data_frame (pd.DataFrame): The data frame of the table.
        """
        self.data_frame = data_frame
