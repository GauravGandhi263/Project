import pandas as pd


data1 = pd.read_csv("Details.csv",encoding="utf-8-sig")
data2 = pd.read_csv("Orders.csv",encoding="utf-8-sig")

data1.columns = data1.columns.str.strip().str.lower()
data2.columns = data2.columns.str.strip().str.lower()


print(data1.columns)
print(data2.columns)


data2_selective = data2[['id', 'order date', 'customername', 'state', 'city']]
merged_data = pd.merge(data1, data2_selective, on="id", how="left")
merged_data['order date']= pd.to_datetime(merged_data['order date'], format='mixed')
merged_data['month'] = merged_data['order date'].dt.month_name()
merged_data['quantity'] = pd.to_numeric(merged_data['quantity'], errors='coerce')
merged_data['amount'] = pd.to_numeric(merged_data['amount'], errors='coerce')
merged_data['profit'] = pd.to_numeric(merged_data['profit'], errors='coerce')

merged_data['category'] = merged_data['category'].astype('category')
merged_data['sub-category'] = merged_data['sub-category'].astype('category')
merged_data['paymentmode'] = merged_data['paymentmode'].astype('category')



# Formatting Date to Indian Style (dd-mm-yyyy)
merged_data['order date'] = merged_data['order date'].dt.strftime('%d-%m-%Y')

merged_data['Total_Sales'] = merged_data['quantity'] * merged_data['amount']

# --- Analysis: Pivot Tables ---

print("\n" + "="*30)
print("     ANALYSIS RESULTS")
print("="*30)

# 1. Top Payment Mode
top_payment = merged_data.groupby('paymentmode')['Total_Sales'].sum().sort_values(ascending=False)
print("\n--- Sales by Payment Mode ---")
print(top_payment)

# 2. Top 10 Cities with most Sales and Quantity
top_cities = merged_data.groupby('city').agg({'Total_Sales': 'sum', 'quantity': 'sum'}).sort_values(by='Total_Sales', ascending=False).head(10)
print("\n--- Top 10 Cities (Sales & Quantity) ---")
print(top_cities)

# 3. Top 5 States with most Sales and Quantity
top_states = merged_data.groupby('state').agg({'Total_Sales': 'sum', 'quantity': 'sum'}).sort_values(by='Total_Sales', ascending=False).head(5)
print("\n--- Top 5 States (Sales & Quantity) ---")
print(top_states)

# 4. Top 5 Months with most Sales
top_months = merged_data.groupby('month')['Total_Sales'].sum().sort_values(ascending=False).head(5)
print("\n--- Top 5 Months by Sales ---")
print(top_months)

# 5. Top Sales for each Category and Sub-category
category_analysis = merged_data.groupby(['category', 'sub-category'])['Total_Sales'].sum().reset_index()
# Sort within each category by Total_Sales
category_analysis = category_analysis.sort_values(by=['category', 'Total_Sales'], ascending=[True, False])
print("\n--- Category & Sub-Category Sales ---")
print(category_analysis)

# --- Final Export: TWO-SHEET EXCEL REPORT ---

# 1. Save main data to CSV (Indian Date format preserved)
merged_data.to_csv("Cleaned_Data.csv", index=False)

# 2. Save everything to a single Excel file with strictly TWO sheets
with pd.ExcelWriter("Final_Report.xlsx", engine='openpyxl') as writer:
    # Sheet 1: Main Cleaned Data
    merged_data.to_excel(writer, sheet_name='Cleaned Data', index=False)
    
    # Sheet 2: Analysis Results (Stacking all tables)
    # Each table starts with a label for clarity
    
    # Starting at Row 0: Top Payment Modes
    pd.Series(["--- TOP PAYMENT MODES ---"]).to_excel(writer, sheet_name='Analysis Results', index=False, header=False, startrow=0)
    top_payment.to_frame().to_excel(writer, sheet_name='Analysis Results', startrow=1)
    
    # Starting at Row 9: Top 10 Cities
    pd.Series(["--- TOP 10 CITIES ---"]).to_excel(writer, sheet_name='Analysis Results', index=False, header=False, startrow=9)
    top_cities.to_excel(writer, sheet_name='Analysis Results', startrow=10)
    
    # Starting at Row 23: Top 5 States
    pd.Series(["--- TOP 5 STATES ---"]).to_excel(writer, sheet_name='Analysis Results', index=False, header=False, startrow=23)
    top_states.to_excel(writer, sheet_name='Analysis Results', startrow=24)
    
    # Starting at Row 32: Top 5 Months
    pd.Series(["--- TOP 5 MONTHS ---"]).to_excel(writer, sheet_name='Analysis Results', index=False, header=False, startrow=31)
    top_months.to_frame().to_excel(writer, sheet_name='Analysis Results', startrow=32)
    
    # Starting at Row 40: Category Analysis
    pd.Series(["--- CATEGORY & SUB-CATEGORY ANALYSIS ---"]).to_excel(writer, sheet_name='Analysis Results', index=False, header=False, startrow=40)
    category_analysis.to_excel(writer, sheet_name='Analysis Results', index=False, startrow=41)

print("\n" + "="*50)
print("SUCCESS: Cleaned data saved to 'Cleaned_Data.csv'")
print("SUCCESS: TWO-SHEET report saved to 'Final_Report.xlsx'")
print("="*50)










