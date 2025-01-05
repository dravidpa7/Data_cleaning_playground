# Data Cleaning Web App

## Overview
This Streamlit application allows you to clean and process numerical data in a CSV file. You can upload a dataset, preview it, and perform various cleaning operations such as removing empty rows, replacing missing values, handling duplicates, and more. The processed dataset can be downloaded as a CSV file.

---

## Features
1. Upload and preview your dataset.
2. Remove rows with missing values.
3. Replace missing values with:
   - Custom values.
   - Forward or backward fill.
   - Aggregation (mean, median, mode).
4. Handle missing values in specific columns.
5. Remove duplicate rows.
6. Download the cleaned dataset.
7. Reset all changes to the original dataset.

---

## Installation
Follow these steps to set up and run the app on your local machine:

### Prerequisites
- Python 3.7 or later installed.
- `pip` package manager installed.

### Steps
1. Clone or download the repository containing the code.
2. Open a terminal and navigate to the directory containing the code.
3. Install the required Python libraries using:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the App
1. In the terminal, navigate to the directory containing the app.
2. Run the following command:
   ```bash
   streamlit run app.py
   ```
3. The app will open in your default web browser.

### Using the App
1. **Upload a Dataset**:
   - Click "Choose a CSV file" to upload your dataset.
2. **Preview the Dataset**:
   - Click "Preview dataset" to view the contents of your uploaded file.
3. **Perform Cleaning Operations**:
   - Use the options provided to clean the dataset (e.g., remove empty rows, replace missing values, remove duplicates).
4. **Download the Processed Dataset**:
   - Click the "Download Processed Data" button to download the cleaned dataset as a CSV file.
5. **Reset the Dataset**:
   - Use the "Reset All Changes" button to revert the dataset to its original state.

---

## Notes
- This application is designed to handle numerical data only.
- Ensure your dataset is in CSV format before uploading.
- All processing actions are logged in the app for better transparency.

---

## Support
For any issues or suggestions, please contact the developer or raise an issue in the repository.

