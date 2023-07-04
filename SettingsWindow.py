from PyQt5 import QtCore, QtWidgets, QtGui


class SettingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingWindow, self).__init__()
        self.topLayout = None
        self.leftLayout = None
        self.mainLayout = None
        self.divider = None
        self.stackedWidget = None
        self.pushButton = None
        self.advancedSettingsButton = None
        self.basicSettingsButton = None
        self.setObjectName("SettingWindow")
        self.setFixedSize(500, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.setCentralWidget(self.centralwidget)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.settings_changed = False
        self.init_ui()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("SettingWindow", "Settings"))
        self.pushButton.setText(translate("SettingWindow", "Close"))

    def init_ui(self):
        # Create Widgets
        self.basicSettingsButton = QtWidgets.QPushButton("Basic Settings")
        self.advancedSettingsButton = QtWidgets.QPushButton("Advanced Settings")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)

        # Create Divider
        self.divider = QtWidgets.QFrame()
        self.divider.setFrameShape(QtWidgets.QFrame.VLine)
        self.divider.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Layout Management
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.topLayout = QtWidgets.QHBoxLayout()
        self.leftLayout = QtWidgets.QVBoxLayout()

        # Add widgets to the layout
        self.leftLayout.addWidget(self.basicSettingsButton)
        self.leftLayout.addWidget(self.advancedSettingsButton)
        self.topLayout.addLayout(self.leftLayout)
        self.topLayout.addWidget(self.divider)
        self.topLayout.addWidget(self.stackedWidget)
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addWidget(self.pushButton)

        # Connect Buttons
        self.basicSettingsButton.clicked.connect(lambda: self.change_settings(0))
        self.advancedSettingsButton.clicked.connect(lambda: self.change_settings(1))
        self.pushButton.clicked.connect(self.close_window)

    def change_settings(self, index):
        widget = QtWidgets.QLabel('Default Settings')  # default widget
        if index == 0:  # Basic Settings
            widget = QtWidgets.QLabel('Basic Settings')
        elif index == 1:  # Advanced Settings
            widget = QtWidgets.QLabel('Advanced Settings')
        while self.stackedWidget.count() > 0:
            self.stackedWidget.removeWidget(self.stackedWidget.widget(0))
        self.stackedWidget.addWidget(widget)
        self.settings_changed = True
        self.check_changes()

    def check_changes(self):
        if not self.settings_changed:
            self.pushButton.setText("Close")
        else:
            self.pushButton.setText("Save")

    def close_window(self):
        if self.pushButton.text() == "Close":
            self.close()

    def closeEvent(self, event):
        event.accept()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    setting_window = SettingWindow()
    setting_window.show()
    sys.exit(app.exec_())
