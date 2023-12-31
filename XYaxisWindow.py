from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter, QMessageBox


class AutoCompletingComboBox(QComboBox):
    """
    Custom combo box class that supports auto-completion and editing.
    """

    def __init__(self, parent=None):
        """
        Initializes the AutoCompletingComboBox.

        Args:
            parent (QWidget): The parent widget.
        """
        super().__init__(parent)
        self.setEditable(True)
        self.lineEdit().setAlignment(Qt.AlignLeft)
        self.setCompleter(QCompleter(self.model()))
        self.lineEdit().setCompleter(self.completer())
        self.setInsertPolicy(QComboBox.NoInsert)

    def addItemToComboBox(self, item):
        """
        Adds an item to the combo box.

        Args:
            item: The item to add to the combo box.
        """
        super().addItem(item)
        self.completer().setModel(self.model())


class XYaxisWindow(QtWidgets.QMainWindow):
    """
    QMainWindow subclass for XY Axis Window.
    """

    def __init__(self):
        """
        Initializes the XYaxisWindow.
        """
        super(XYaxisWindow, self).__init__()
        self.savedSelectedBarColumn = None
        self.generate_button = None
        self.savedSelectedYColumn = None
        self.savedSelectedXColumn2 = None
        self.savedSelectedXColumn = None
        self.rows = None
        self.saveBarChart_button = None
        self.saveHistogramButton_layout = None
        self.saveButton_layout = None
        self.save_button = None
        self.xAxisData = []
        self.yAxisData = []
        self.barChartColumnData = []
        self.items = set()
        self.data_frame = None
        self.barChartColumn_combobox = None
        self.barColumn_label = None
        self.horizontal_layout = None
        self.vertical_layout = None
        self.gridLayout_3 = None
        self.bar_chart_page = None
        self.yAxis_comboBox = None
        self.selectColumn_label = None
        self.yAxis_layout = None
        self.yAxis_line2 = None
        self.yAxis_label = None
        self.yAxis_line = None
        self.xAxisColumn2_label = None
        self.xAxisColumn2_layout = None
        self.xAxisColumn2_comboBox = None
        self.xAxisValues_comboBox = None
        self.xAxisValues_label = None
        self.xAxisValues_layout = None
        self.xAxisColumn_label = None
        self.xAxisColumn_comboBox = None
        self.xAxisColumn_layout = None
        self.scatterplot_main_layout = None
        self.gridLayout_2 = None
        self.scatter_plot_page = None
        self.xAxis_label = None
        self.xAxis_line = None
        self.stackedWidget = None
        self.gridLayout = None
        self.setObjectName("xyAxisWindow")
        self.resize(490, 209)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setupUi()
        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setupUi(self):
        """
        Sets up the user interface for the XYaxisWindow.
        """
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")

        # scatter plot page
        self.scatter_plot_page = QtWidgets.QWidget()
        self.scatter_plot_page.setObjectName("scatter_plot_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scatter_plot_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scatterplot_main_layout = QtWidgets.QVBoxLayout()
        self.scatterplot_main_layout.setObjectName("scatter_plot_main_layout")

        # X-Axis
        self.xAxis_label = QtWidgets.QLabel(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.xAxis_label.sizePolicy().hasHeightForWidth())
        self.xAxis_label.setSizePolicy(sizePolicy)
        self.xAxis_label.setAlignment(QtCore.Qt.AlignCenter)
        self.xAxis_label.setObjectName("xAxis_label")
        self.scatterplot_main_layout.addWidget(self.xAxis_label)

        self.xAxis_line = QtWidgets.QFrame(self.scatter_plot_page)
        self.xAxis_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.xAxis_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.xAxis_line.setObjectName("xAxis_line")
        self.scatterplot_main_layout.addWidget(self.xAxis_line)

        self.xAxisColumn_layout = QtWidgets.QHBoxLayout()
        self.xAxisColumn_layout.setObjectName("xAxisColumn_layout")
        self.xAxisColumn_label = QtWidgets.QLabel(self.scatter_plot_page)
        self.xAxisColumn_label.setObjectName("xAxisColumn_label")
        self.xAxisColumn_layout.addWidget(self.xAxisColumn_label)

        self.xAxisColumn_comboBox = AutoCompletingComboBox(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.xAxisColumn_comboBox.sizePolicy().hasHeightForWidth())
        self.xAxisColumn_comboBox.setSizePolicy(sizePolicy)
        self.xAxisColumn_comboBox.setObjectName("xAxisColumn_comboBox")
        self.xAxisColumn_layout.addWidget(self.xAxisColumn_comboBox)

        self.scatterplot_main_layout.addLayout(self.xAxisColumn_layout)
        self.xAxisValues_layout = QtWidgets.QHBoxLayout()
        self.xAxisValues_layout.setObjectName("xAxisValues_layout")
        self.xAxisValues_label = QtWidgets.QLabel(self.scatter_plot_page)
        self.xAxisValues_label.setObjectName("xAxisValues_label")
        self.xAxisValues_layout.addWidget(self.xAxisValues_label)

        self.xAxisValues_comboBox = AutoCompletingComboBox(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.xAxisValues_comboBox.sizePolicy().hasHeightForWidth())
        self.xAxisValues_comboBox.setSizePolicy(sizePolicy)
        self.xAxisValues_comboBox.setObjectName("xAxisValues_comboBox")
        self.xAxisValues_layout.addWidget(self.xAxisValues_comboBox)
        self.scatterplot_main_layout.addLayout(self.xAxisValues_layout)

        self.xAxisColumn2_layout = QtWidgets.QHBoxLayout()
        self.xAxisColumn2_layout.setObjectName("xAxisColumn2_layout")
        self.xAxisColumn2_label = QtWidgets.QLabel(self.scatter_plot_page)
        self.xAxisColumn2_label.setObjectName("xAxisColumn2_label")
        self.xAxisColumn2_layout.addWidget(self.xAxisColumn2_label)

        self.xAxisColumn2_comboBox = AutoCompletingComboBox(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.xAxisColumn2_comboBox.sizePolicy().hasHeightForWidth())
        self.xAxisColumn2_comboBox.setSizePolicy(sizePolicy)
        self.xAxisColumn2_comboBox.setObjectName("xAxisColumn2_combobox")
        self.xAxisColumn2_layout.addWidget(self.xAxisColumn2_comboBox)

        self.scatterplot_main_layout.addLayout(self.xAxisColumn2_layout)

        # Y-axis
        self.yAxis_label = QtWidgets.QLabel(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.yAxis_label.sizePolicy().hasHeightForWidth())
        self.yAxis_label.setSizePolicy(sizePolicy)
        self.yAxis_label.setAlignment(QtCore.Qt.AlignCenter)
        self.yAxis_label.setObjectName("yAxis_label")
        self.scatterplot_main_layout.addWidget(self.yAxis_label)

        self.yAxis_line = QtWidgets.QFrame(self.scatter_plot_page)
        self.yAxis_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.yAxis_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yAxis_line.setObjectName("yAxis_line")
        self.scatterplot_main_layout.addWidget(self.yAxis_line)

        self.yAxis_layout = QtWidgets.QHBoxLayout()
        self.yAxis_layout.setObjectName("yAxis_layout")
        self.selectColumn_label = QtWidgets.QLabel(self.scatter_plot_page)
        self.selectColumn_label.setObjectName("selectColumn_label")
        self.yAxis_layout.addWidget(self.selectColumn_label)

        self.yAxis_comboBox = AutoCompletingComboBox(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.yAxis_comboBox.sizePolicy().hasHeightForWidth())
        self.yAxis_comboBox.setSizePolicy(sizePolicy)
        self.yAxis_comboBox.setObjectName("yAxis_comboBox")
        self.yAxis_layout.addWidget(self.yAxis_comboBox)

        self.scatterplot_main_layout.addLayout(self.yAxis_layout)
        self.gridLayout_2.addLayout(self.scatterplot_main_layout, 0, 0, 1, 1)

        self.saveButton_layout = QtWidgets.QHBoxLayout()
        self.saveButton_layout.setObjectName("saveButton_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.saveButton_layout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.scatter_plot_page)
        self.save_button.setObjectName("save_button")
        self.saveButton_layout.addWidget(self.save_button)
        self.scatterplot_main_layout.addLayout(self.saveButton_layout)
        self.gridLayout_2.addLayout(self.scatterplot_main_layout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.scatter_plot_page)

        self.stackedWidget.addWidget(self.scatter_plot_page)

        # Histogram page
        self.bar_chart_page = QtWidgets.QWidget()
        self.bar_chart_page.setObjectName("histogram_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.bar_chart_page)

        self.gridLayout_3.setObjectName("gridLayout_3")

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.barColumn_label = QtWidgets.QLabel(self.bar_chart_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.barColumn_label.sizePolicy().hasHeightForWidth())
        self.barColumn_label.setSizePolicy(sizePolicy)
        self.barColumn_label.setObjectName("histogramColumn_label")
        self.horizontal_layout.addWidget(self.barColumn_label)

        self.barChartColumn_combobox = AutoCompletingComboBox(self.bar_chart_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.barChartColumn_combobox.sizePolicy().hasHeightForWidth())
        self.barChartColumn_combobox.setSizePolicy(sizePolicy)
        self.barChartColumn_combobox.setObjectName("histogramColumn_combobox")
        self.horizontal_layout.addWidget(self.barChartColumn_combobox)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.saveHistogramButton_layout = QtWidgets.QHBoxLayout()
        self.saveHistogramButton_layout.setObjectName("saveHistogramButton_layout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.saveHistogramButton_layout.addItem(spacerItem1)
        self.saveBarChart_button = QtWidgets.QPushButton(self.bar_chart_page)
        self.saveBarChart_button.setObjectName("saveHistogram_button")
        self.saveHistogramButton_layout.addWidget(self.saveBarChart_button)
        self.vertical_layout.addLayout(self.saveHistogramButton_layout)

        self.gridLayout_3.addLayout(self.vertical_layout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.bar_chart_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.save_button.clicked.connect(self.saveButtonHandler)
        self.xAxisColumn_comboBox.activated.connect(self.fillValuesComboBox)
        self.saveBarChart_button.clicked.connect(self.saveBarChartHandler)
        self.stackedWidget.setCurrentIndex(0)

    def translateUi(self):
        """
        Retranslate the UI components to the specified main window.

        """
        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("xyAxisWindow", "Graph Axis Setup"))
        self.xAxis_label.setText(translate("xyAxisWindow", "X Axis"))
        self.xAxisColumn_label.setText(translate("xyAxisWindow", "Column to sample: "))
        self.xAxisValues_label.setText(translate("xyAxisWindow", "select values of: "))
        self.xAxisColumn2_label.setText(translate("xyAxisWindow", "Displaying values of column: "))
        self.yAxis_label.setText(translate("xyAxisWindow", "Y Axis"))
        self.selectColumn_label.setText(translate("xyAxisWindow", "Select Column:"))
        self.save_button.setText(translate("xyAxisWindow", "Save"))
        self.barColumn_label.setText(translate("xyAxisWindow", "Select column:"))
        self.saveBarChart_button.setText(translate("xyAxisWindow", "Save"))

    def set_table_dataframe(self, data):
        """
        Sets the data frame for the table.

        Args:
            data (pd.DataFrame): The data frame for the table.
        """
        self.data_frame = data

    def fillValuesComboBox(self):
        """
        Fills the values combo box based on the selected column.
        """
        self.xAxisValues_comboBox.clear()
        self.items.clear()

        # Get the selected text from the combo box
        text = self.xAxisColumn_comboBox.currentText()

        # Get the column values for the selected text
        column_values = self.data_frame[text]

        # Add unique values to the combo box
        for value in column_values:
            if value not in self.items:
                self.items.add(value)
                self.xAxisValues_comboBox.addItemToComboBox(str(value))

    def saveButtonHandler(self):
        """
        Handles the save button click event.
        """
        # Check if required fields are empty
        if (self.xAxisColumn_comboBox.currentText() == "" or
                self.xAxisColumn2_comboBox.currentText() == "" or
                self.yAxis_comboBox.currentText() == ""):
            QMessageBox.warning(self, "Warning", "Please input data before saving.")
            return

        # Retrieve the selected rows based on user input
        self.rows = self.data_frame.index[
            self.data_frame[self.xAxisColumn_comboBox.currentText()] == self.xAxisValues_comboBox.currentText()]

        # Retrieve X-axis data
        for row in self.rows:
            self.xAxisData.append(
                self.data_frame.at[self.data_frame.index[row], str(self.xAxisColumn2_comboBox.currentText())])

        # Retrieve Y-axis data
        for row in self.rows:
            self.yAxisData.append(
                self.data_frame.at[self.data_frame.index[row], str(self.yAxis_comboBox.currentText())])

        # Save selected column values
        self.savedSelectedXColumn = str(self.xAxisColumn_comboBox.currentText())
        self.savedSelectedXColumn2 = str(self.xAxisColumn2_comboBox.currentText())
        self.savedSelectedYColumn = str(self.yAxis_comboBox.currentText())

        # Enable generate button
        self.generate_button.setEnabled(True)
        self.close()

    def saveBarChartHandler(self):
        """
        Handles the save button click event for the bar chart.
        """
        if self.barChartColumn_combobox.currentText() == "":
            QMessageBox.warning(self, "Warning", "Please input data before saving.")
            return

        self.barChartColumnData = self.data_frame[str(self.barChartColumn_combobox.currentText())].tolist()
        self.generate_button.setEnabled(True)
        self.savedSelectedBarColumn = str(self.barChartColumn_combobox.currentText())
        self.close()

    def loadSavedData(self):
        """
        Loads the saved data into the UI components.
        """
        self.xAxisColumn_comboBox.setCurrentText(self.savedSelectedXColumn)
        self.xAxisColumn2_comboBox.setCurrentText(self.savedSelectedXColumn2)
        self.yAxis_comboBox.setCurrentText(self.savedSelectedYColumn)
        self.close()

    def getxAxisData(self):
        """
        Returns the X-axis data.

        Returns:
            list: The X-axis data.
        """
        return self.xAxisData

    def getyAxisData(self):
        """
        Returns the Y-axis data.

        Returns:
            list: The Y-axis data.
        """
        return self.yAxisData

    def displayPage(self, state):
        """
        Sets the current index of the stackedWidget based on the state.

        Args:
            state (int): The state of the page to display.
        """
        if state == 1:
            self.stackedWidget.setCurrentIndex(0)
        elif state == 2:
            self.stackedWidget.setCurrentIndex(1)

    def getBarChartColumnData(self):
        """
        Returns the data for the bar chart column.

        Returns:
            list: The data for the bar chart column.
        """
        return self.barChartColumnData

    def getRows(self):
        """
        Returns the selected rows.

        Returns:
            list: The selected rows.
        """
        return self.rows

    def setGenerateButton(self, button):
        """
        Sets the generate button.

        Args:
            button (QPushButton): The generate button.
        """
        self.generate_button = button
