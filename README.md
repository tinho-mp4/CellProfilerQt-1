# CellProfiler

CellProfiler is a CellProfiler is a robust and user-friendly software tool that offers seamless interactions with .csv data tables for manipulation, transformation, and analysis. The software is equipped to handle tasks like data cleaning/pre-processing, and can conduct comprehensive analyses such as correlation plots and dimensional reduction like PCA for multi-variable visualization. Its GUI framework has been carefully designed to offer accessibility to users who prefer not to engage directly with algorithms, making complex data transformations accessible to a wider user base without requiring extensive coding knowledge. This document provides information on how to set up, use and contribute to CellProfiler.

## Features

- Reads .csv data tables
- Data cleaning and pre-processing (e.g., removing N/A entries, normalizing)
- Comprehensive analysis tools (correlation plots, dimensional reduction techniques like PCA)
- Easy-to-use, flexible GUI
- Designed for users with minimal coding knowledge

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Installation

Follow these steps to install and setup CellProfiler:

```bash
# Clone the repository
git clone https://github.com/Anush-Varma/CellProfiler.git

# Navigate to the directory
cd CellProfiler

# (Optional) Create a virtual environment
python3 -m venv venv

# Activate the virtual environment

# On Windows, use:
venv\Scripts\activate

# On Unix or MacOS, use:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Run the application
python main.py
