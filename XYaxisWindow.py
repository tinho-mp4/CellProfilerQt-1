from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter


class AutoCompletingComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.lineEdit().setAlignment(Qt.AlignLeft)
        self.setCompleter(QCompleter(self.model()))
        self.lineEdit().setCompleter(self.completer())
        self.setInsertPolicy(QComboBox.NoInsert)

    def addItemToComboBox(self, item):
        super().addItem(item)
        self.completer().setModel(self.model())


class XYaxisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(XYaxisWindow, self).__init__()
        self.xAxisData = []
        self.yAxisData = []
        self.items = set()
        self.data_frame = None
        self.histogramColumn_combobox = None
        self.histogramColumn_label = None
        self.horizontal_layout = None
        self.vertical_layout = None
        self.gridLayout_3 = None
        self.histogram_page = None
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
        self.yAxis_line = QtWidgets.QFrame(self.scatter_plot_page)
        self.yAxis_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.yAxis_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yAxis_line.setObjectName("yAxis_line")
        self.scatterplot_main_layout.addWidget(self.yAxis_line)

        self.yAxis_label = QtWidgets.QLabel(self.scatter_plot_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.yAxis_label.sizePolicy().hasHeightForWidth())
        self.yAxis_label.setSizePolicy(sizePolicy)
        self.yAxis_label.setAlignment(QtCore.Qt.AlignCenter)
        self.yAxis_label.setObjectName("yAxis_label")
        self.scatterplot_main_layout.addWidget(self.yAxis_label)

        self.yAxis_line2 = QtWidgets.QFrame(self.scatter_plot_page)
        self.yAxis_line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.yAxis_line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yAxis_line2.setObjectName("yAxis_line2")
        self.scatterplot_main_layout.addWidget(self.yAxis_line2)

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

        self.histogram_page = QtWidgets.QWidget()
        self.histogram_page.setObjectName("histogram_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.histogram_page)

        self.gridLayout_3.setObjectName("gridLayout_3")

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.histogramColumn_label = QtWidgets.QLabel(self.histogram_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.histogramColumn_label.sizePolicy().hasHeightForWidth())
        self.histogramColumn_label.setSizePolicy(sizePolicy)
        self.histogramColumn_label.setObjectName("histogramColumn_label")
        self.horizontal_layout.addWidget(self.histogramColumn_label)

        self.histogramColumn_combobox = AutoCompletingComboBox(self.histogram_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.histogramColumn_combobox.sizePolicy().hasHeightForWidth())
        self.histogramColumn_combobox.setSizePolicy(sizePolicy)
        self.histogramColumn_combobox.setObjectName("histogramColumn_combobox")
        self.horizontal_layout.addWidget(self.histogramColumn_combobox)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.saveHistogramButton_layout = QtWidgets.QHBoxLayout()
        self.saveHistogramButton_layout.setObjectName("saveHistogramButton_layout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.saveHistogramButton_layout.addItem(spacerItem1)
        self.saveHistogram_button = QtWidgets.QPushButton(self.histogram_page)
        self.saveHistogram_button.setObjectName("saveHistogram_button")
        self.saveHistogramButton_layout.addWidget(self.saveHistogram_button)
        self.vertical_layout.addLayout(self.saveHistogramButton_layout)

        self.gridLayout_3.addLayout(self.vertical_layout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.histogram_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)




        self.save_button.clicked.connect(self.saveScatterButtonHandler)
        self.saveHistogram_button.clicked.connect(self.saveHistogramButtonHandler)
        self.xAxisColumn_comboBox.activated.connect(self.fillValuesComboBox)





    def translateUi(self):
        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("xyAxisWindow", "Graph Axis Setup"))
        self.xAxis_label.setText(translate("xyAxisWindow", "X Axis"))
        self.xAxisColumn_label.setText(translate("xyAxisWindow", "From column: "))
        self.xAxisValues_label.setText(translate("xyAxisWindow", "select values of: "))
        self.xAxisColumn2_label.setText(translate("xyAxisWindow", "Displaying values of column: "))
        self.yAxis_label.setText(translate("xyAxisWindow", "Y Axis"))
        self.selectColumn_label.setText(translate("xyAxisWindow", "Select Column:"))
        self.save_button.setText(translate("xyAxisWindow", "Save"))
        self.histogramColumn_label.setText(translate("xyAxisWindow", "Select column:"))
        self.saveHistogram_button.setText(translate("xyAxisWindow", "Save"))


    def set_table_data_frame(self, data):
        self.data_frame = data


    def fillValuesComboBox(self):
        self.xAxisValues_comboBox.clear()
        self.items.clear()
        text = self.xAxisColumn_comboBox.currentText()
        column_values = self.data_frame[text]
        for value in column_values:
            if value not in self.items:
                self.items.add(value)
                self.xAxisValues_comboBox.addItemToComboBox(str(value))


    def saveHistogramButtonHandler(self):
        print("worked")

    def saveScatterButtonHandler(self):
        self.rows = self.data_frame.index[
            self.data_frame[self.xAxisColumn_comboBox.currentText()] == self.xAxisValues_comboBox.currentText()]
        for row in self.rows:
            self.xAxisData.append(
                self.data_frame.at[self.data_frame.index[row], str(self.xAxisColumn2_comboBox.currentText())])
        for row in self.rows:
            self.yAxisData.append(
                self.data_frame.at[self.data_frame.index[row], str(self.yAxis_comboBox.currentText())])
        self.close()

    def load_saved_data(self):
        for data in self.xAxisData:
            self.xAxisColumn2_comboBox.addItemToComboBox(str(data))

    def getxAxisData(self):
        return self.xAxisData

    def displayPage(self, state):
        if state == 1:
            self.stackedWidget.setCurrentIndex(0)
        elif state == 2:
            self.stackedWidget.setCurrentIndex(1)


    def getRows(self):
        return self.rows
