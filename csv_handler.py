from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog
import pandas as pd


class CSVTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return len(self.data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self.data.iloc[index.row(), index.column()]
            return str(value)
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        return QVariant()

    def get_value(self, row, column):
        return self.data.iloc[row, column]

    def get_row_data(self, row):
        return self.data.iloc[row]

    def get_column_data(self, column):
        return self.data.iloc[:, column]


def browse_file():
    file_dialog = QFileDialog()
    filename, _ = file_dialog.getOpenFileName(None, "Open CSV file", "", "CSV Files (*.csv)")
    return filename


def load_csv_file(filename):
    if filename:
        try:
            data = pd.read_csv(filename)
            return data
        except Exception as e:
            print(f"Error: {e}")
    return None


def export_csv_file(filename, data):
    try:
        if filename:
            data.to_csv(filename, index=False)
            print("File has been exported")
        else:
            print("No file selected.")
    except Exception as e:
        print(f"Error while exporting CSV: {str(e)}")
