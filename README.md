# excel-to-pdf-reporting
A Python-based automation tool that converts raw Excel data into structured, print-ready PDF business reports.
# Automated Business Reporting Tool

A Python-based automation solution designed to streamline the process of extracting, analyzing, and reporting business data. This tool reads raw data from Excel files, performs statistical analysis, and automatically generates structured PDF reports.

## 📌 Problem & Solution

Manual data processing and reporting are time-consuming and prone to human error. This script automates the entire pipeline:
1. **Extraction:** Safely reads unorganized raw data from `.xlsx` files.
2. **Analysis:** Automatically calculates key statistical metrics across all numeric data columns.
3. **Reporting:** Generates a clean, standardized PDF document ready for management or client distribution.

### Business Value
* **Time Efficiency:** Reduces reporting tasks from hours to seconds.
* **Accuracy:** Eliminates manual copy-paste errors.
* **Scalability:** Capable of processing large datasets seamlessly.

## ⚙️ Features

* **Automated Data Mocking:** Includes a fallback mechanism that generates sample data if no source file is found, ensuring the script is always testable out-of-the-box.
* **Statistical Summaries:** Utilizes `pandas` to generate comprehensive descriptive statistics (count, mean, standard deviation, min/max).
* **Dynamic PDF Generation:** Uses `fpdf` to format and export the analyzed data into a readable document.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Libraries:** * `pandas` (Data manipulation and analysis)
  * `openpyxl` (Excel file handling)
  * `fpdf` (PDF document generation)

## 🚀 Quick Start

### Prerequisites
Ensure Python is installed on your system. Install the required dependencies using pip:

```bash
pip install pandas openpyxl fpdf
