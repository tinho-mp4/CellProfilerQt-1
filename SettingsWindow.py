from PyQt5 import QtCore, QtWidgets


class SettingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingWindow, self).__init__()
        self.setObjectName("SettingWindow")
        self.setFixedSize(400, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def retranslateUi(self):
        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("SettingWindow", "Settings"))
        self.label.setText(translate("SettingWindow", "Basic Settings"))
        self.pushButton.setText(translate("SettingWindow", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    setting_window = SettingWindow()
    setting_window.show()
    sys.exit(app.exec_())
