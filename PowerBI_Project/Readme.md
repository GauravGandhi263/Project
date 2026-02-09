![Power BI Dashboard Preview](PASTE_YOUR_IMAGE_LINK_HERE)

# 📊 Power BI Interactive Dashboard Project

## 📌 Project Overview
This project showcases an end-to-end **Power BI data analysis and visualization workflow**, starting from raw data to a fully **interactive and insight-driven dashboard**.  
The focus of this project is on **data cleaning, transformation, modeling, calculations, and storytelling through visuals** using **Power BI and Power Query**.

The dashboard enables users to explore data dynamically, uncover trends, and make data-driven decisions through intuitive filters and KPIs.

---

## 🛠 Tools & Technologies Used
- **Power BI Desktop**
- **Power Query (M Language)**
- **DAX (Data Analysis Expressions)**
- **Excel / CSV / Database (Data Source)**
- **GitHub (Version Control & Documentation)**

---

## 🔄 Data Cleaning & Transformation (Power Query)
Raw data often comes with inconsistencies, errors, and unnecessary fields. Below is a **step-by-step breakdown** of how the data was cleaned and prepared using **Power Query**:

### 1️⃣ Data Import
- Loaded raw data from the source into Power BI
- Verified data types for each column (Text, Number, Date, etc.)

### 2️⃣ Removing Unnecessary Columns
- Removed irrelevant or duplicate columns
- Kept only fields required for analysis and reporting

### 3️⃣ Handling Missing & Null Values
- Identified missing or null values
- Replaced nulls with appropriate defaults (e.g., 0, "Unknown")
- Removed rows where critical data was missing

### 4️⃣ Data Type Standardization
- Converted columns to correct data types
- Ensured date fields follow a consistent format
- Converted numeric fields from text where necessary

### 5️⃣ Cleaning Text Data
- Trimmed leading and trailing spaces
- Removed extra spaces and special characters
- Standardized text formatting (uppercase/lowercase)

### 6️⃣ Removing Duplicates
- Identified duplicate records
- Removed duplicates to maintain data accuracy

### 7️⃣ Creating Custom Columns
- Created calculated columns using Power Query
- Extracted values (year, month, category, etc.)
- Merged or split columns when needed

### 8️⃣ Filtering & Data Validation
- Filtered out invalid or outlier values
- Validated data consistency after transformations

---

## 🧠 Data Modeling
- Built relationships between tables using **star schema**
- Defined **primary and foreign keys**
- Optimized model for performance and accurate calculations

---

## 📐 Calculations & Measures (DAX)
Created dynamic measures to support analysis and KPIs, including:

- Total metrics (Sales, Revenue, Quantity, etc.)
- Average and percentage calculations
- Time intelligence measures (YTD, MTD, YoY)
- Growth rate and variance calculations
- Conditional logic using `IF`, `SWITCH`, and `CALCULATE`

These measures allow the dashboard to respond dynamically to filters and slicers.

---

## 📊 Dashboard Design & Visualization
The dashboard was designed with **clarity, usability, and interactivity** in mind:

### Key Features:
- Interactive slicers (Date, Category, Region, etc.)
- KPI cards for quick performance insights
- Bar, line, and pie charts for trend analysis
- Drill-through and cross-filtering
- Consistent color theme and layout for readability

### User Experience Focus:
- Easy navigation
- Minimal clutter
- Business-focused insights at a glance

---

## 🚀 Key Insights Delivered
- Identification of trends and patterns
- Performance comparison across dimensions
- Data-driven decision support
- Clear visibility into key metrics

---

## 📂 Project Structure
```text
├── Power BI (.pbix) File
├── Dashboard Images
└── README.md
