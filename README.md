# Data Cleaning Application

A Streamlit-based web application for cleaning and preprocessing numerical data in CSV files.

## Features

### 1. Data Upload
- Supports CSV file format
- Preview functionality for uploaded datasets
- Session state management for consistent data handling

### 2. Data Cleaning Operations

#### Empty Cell Handling
- **Remove Rows**: Delete rows containing missing values
- **Replace Values**: Multiple options for filling missing values
  - Fill with specific value
  - Forward fill
  - Backward fill
- **Replace Specific Columns**: Target specific columns for value replacement
- **Aggregation-based Filling**: Fill missing values using
  - Mean
  - Median
  - Mode

#### Duplicate Management
- Detect duplicate rows
- Remove duplicates with single click
- Preview updated dataset after duplicate removal

### 3. User Interface Features
- Interactive selection menus
- Progress indicators
- Success/warning messages
- Error handling with user-friendly messages
- Download processed data as CSV
- Reset functionality to restore original data

## Usage Instructions

1. **Upload Data**
   - Click "Browse files" to upload your CSV file
   - Use "Preview dataset" button to view your data

2. **Clean Data**
   - Select cleaning operation from the dropdown
   - Choose specific options for the selected operation
   - Click "Apply Changes" to execute the operation

3. **Handle Duplicates**
   - Use "Check & Remove Duplicates" to find and remove duplicate rows
   - View the number of duplicates found
   - See preview of cleaned dataset

4. **Save Results**
   - Download processed data using the "💾 Download Processed Data" button
   - Reset all changes if needed using "Reset All Changes"

## Requirements
- Python 3.x
- Streamlit
- Pandas

## Limitations
- Currently supports only numerical data cleaning
- CSV file format only
- Operations are performed in-memory

## Error Handling
- Input validation for numeric values
- Graceful error handling with user notifications
- Protection against invalid operations

## Data Persistence
- Session state management for consistent data handling
- Changes persist until manual reset or session end

## Best Practices
1. Preview data before applying operations
2. Use the reset function if you need to start over
3. Download processed data after completing all operations
4. Check the dataset size indicator for operation confirmation

## Note
This application is designed for numerical data preprocessing and may not handle text or categorical data appropriately.


## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
