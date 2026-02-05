# Excel Data Consolidation Using Power Query

## Project Overview
This project combines data from **four Excel workbooks into a single master file** using **Power Query’s Append function**.  
The solution is automated using a **folder-based connection**, allowing the master dataset to update automatically whenever new data files are added to the folder.

## Key Features
- Combines multiple Excel files into one dataset
- Uses Power Query Append functionality
- Automated folder connection for dynamic updates
- No manual data handling required

## How It Works
1. Four source Excel files are stored in a single folder  
2. Power Query connects to the folder and loads all files  
3. Data from each file is appended into one table  
4. Refreshing the query updates the master sheet automatically when new data is added

## Screenshots

### Four Excel Files
![Image](images/source_file_1.png)

### Final Consolidated Output
![Final Output](images/final_output.png)

## Tools Used
- Microsoft Excel
- Power Query (Append & Folder Connector)

## How to Update Data
1. Add or replace Excel files in the source folder  
2. Open the master Excel file  
3. Click **Refresh All**  
4. The consolidated data updates automatically

## Notes
- All source files must follow the same structure for successful appending
- Image paths assume screenshots are stored in an `images` folder
