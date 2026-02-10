# Power BI ETL with Power Query 🚀

![Before ETL](./images/before-etl.png)
![After ETL](./images/after-etl.png)

> **Before & After:** Raw, inconsistent data transformed into a clean, analytics-ready model using **Power Query** in **Power BI**.

---

## 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load)** workflow built entirely in **Power Query**.  
The goal was simple: take messy, real-world data and turn it into something reliable, readable, and ready for reporting.

Power Query was used as the primary transformation engine to automate data cleaning and reshaping before loading it into Power BI for analysis.

---

## 🔄 ETL Process Breakdown

### 🧲 Extract
- Imported raw source data into **Power BI**
- Identified common data quality issues such as inconsistent formats, null values, and wide tables

### 🛠 Transform (Power Query Magic ✨)
The following transformations were applied:

- **Cleaned inconsistent date formats**  
  Standardized mixed date values into a single, usable date format

- **Removed null and empty values**  
  Ensured cleaner aggregates and avoided misleading visuals

- **Capitalized name fields**  
  Improved readability and consistency for reporting and dashboards

- **Unpivoted columns**  
  Converted wide, column-heavy data into a normalized, long format  
  → making the dataset more flexible and analytics-friendly

Each step was built using **Power Query’s M transformations**, making the process fully repeatable and refresh-safe.

### 📥 Load
- Loaded the transformed dataset into Power BI
- Data is now structured, clean, and optimized for visualization and analysis

---

## 🖼 Before vs After

| Before ETL | After ETL |
|-----------|----------|
| Inconsistent dates | Standardized date format |
| Null values | Clean, validated rows |
| Mixed-case names | Properly capitalized text |
| Wide table structure | Normalized, unpivoted data |

(See screenshots at the top 👆)

---

## 🧰 Tools Used

- **Power BI**
- **Power Query (M Language)**
- Data cleaning & transformation techniques

---

## 🎯 Key Takeaways

- Power Query is a powerful ETL tool, not just a prep step
- Clean data dramatically improves reporting quality
- Proper unpivoting unlocks more flexible analysis and visuals
- Repeatable transformations = scalable analytics

---

## 📂 How to Use

1. Open the `.pbix` file in Power BI  
2. Review the **Power Query Editor** steps
3. Refresh data to re-run the ETL pipeline

---

## 📸 Screenshots

Replace the image paths at the top of this README with your own:

