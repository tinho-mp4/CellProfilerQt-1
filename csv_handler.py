import pandas as pd
from PyQt5.QtWidgets import QFileDialog


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



