from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QColor, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import os
import dask.dataframe as dd


class CSVTableModel(QAbstractTableModel):
    """
    Custom Table Model for displaying CSV data.
    """
    def __init__(self, data):
        """
        Initializes the CSVTableModel.

        Args:
            data (pd.DataFrame): The data to be displayed in the table.
        """
        super().__init__()
        self.data = data

    def rowCount(self, parent=None):
        """
        Returns the number of rows in the table.

        Args:
            parent: The parent QModelIndex.

        Returns:
            int: The number of rows in the table.
        """
        return len(self.data)

    def columnCount(self, parent=None):
        """
        Returns the number of columns in the table.

        Args:
            parent: The parent QModelIndex.

        Returns:
            int: The number of columns in the table.
        """
        return len(self.data.columns)

    def data(self, index, role=Qt.DisplayRole):
        """
        Returns the data to be displayed at the specified index.

        Args:
            index (QModelIndex): The index of the data.
            role (int): The role of the data.

        Returns:
            QVariant: The data to be displayed at the specified index.
        """
        if role == Qt.DisplayRole:
            value = self.data.iloc[index.row(), index.column()]
            return str(value)
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        return QVariant()

    def getValue(self, row, column):
        """
        Returns the value at the specified row and column.

        Args:
            row (int): The row index.
            column (int): The column index.

        Returns:
            object: The value at the specified row and column.
        """
        return self.data.iloc[row, column]

    def getRowData(self, row):
        """
        Returns the data for the specified row.

        Args:
            row (int): The row index.

        Returns:
            pd.Series: The data for the specified row.
        """
        return self.data.iloc[row]

    def getColumnData(self, column):
        """
        Returns the data for the specified column.

        Args:
            column (int): The column index.

        Returns:
            pd.Series: The data for the specified column.
        """
        return self.data.iloc[:, column]


def browseFile():
    """
    Opens a file dialog and allows the user to browse for a CSV file.

    Returns:
        str: The selected CSV file path.
    """
    file_dialog = QFileDialog()
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    filename, _ = file_dialog.getOpenFileName(
        None, "Open CSV file", "", "CSV Files (*.csv)", options=options
    )
    directory = os.path.dirname(filename) if filename else ""
    file_dialog.setDirectory(directory)
    return filename


def loadCSVFile(filename):
    """
    Loads a CSV file using Dask and returns the computed DataFrame.

    Args:
        filename (str): The path of the CSV file to load.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    if filename:
        try:
            dask_df = dd.read_csv(filename, assume_missing=True)
            return dask_df.compute()
        except Exception as e:
            print(f"Error: {e}")
    return None


def exportCSVFile(filename, data):
    """
    Exports DataFrame data to a CSV file.

    Args:
        filename (str): The path of the CSV file to export.
        data (pd.DataFrame): The DataFrame to export.
    """
    try:
        if filename:
            data.to_csv(filename, index=False)
            print("File has been exported")
        else:
            print("No file selected.")
    except Exception as e:
        print(f"Error while exporting CSV: {str(e)}")
