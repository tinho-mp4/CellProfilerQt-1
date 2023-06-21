import pandas as pd
from PyQt5.QtWidgets import QFileDialog
import dask.dataframe as dd


def browse_file():
    file_dialog = QFileDialog()
    filename, _ = file_dialog.getOpenFileName(None, "Open CSV file", "", "CSV Files (*.csv)")
    return filename


def load_csv_file(filename):
    if filename:
        try:
            data = dd.read_csv(filename, assume_missing=True)
            return data.compute()
        except Exception as e:
            print(f"Error: {e}")
    return None
