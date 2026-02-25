import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Executive Sales Dashboard", layout="wide")

# 2. Custom CSS for High Visibility & Compact Layout
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    div[data-testid="stMetric"] {
        background-color: #1e293b;
        padding: 10px 15px;
        border-radius: 8px;
        color: white !important;
    }
    div[data-testid="stMetric"] label { color: #f1f5f9 !important; font-weight: bold; }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] { color: #38bdf8 !important; }
    h1 { margin-top: -50px; color: #0f172a; font-size: 28px; }
    .stMarkdown { margin-bottom: -15px; }
</style>
""", unsafe_allow_html=True)

# 3. Load Data
@st.cache_data
def load_data():
    import os
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "Cleaned_Data.csv")
    df = pd.read_csv(data_path)
    df['order date'] = pd.to_datetime(df['order date'], dayfirst=True)
    return df

df = load_data()

# 4. Sidebar Slicers (Dropdown instead of Multiselect)
st.sidebar.title("📊 Filter Dashboard")
state_options = ["All"] + list(df['state'].unique())
state_sel = st.sidebar.selectbox("Select State", options=state_options)

cat_options = ["All"] + list(df['category'].unique())
cat_sel = st.sidebar.selectbox("Select Category", options=cat_options)

# Filter logic
filtered_df = df.copy()
if state_sel != "All":
    filtered_df = filtered_df[filtered_df['state'] == state_sel]
if cat_sel != "All":
    filtered_df = filtered_df[filtered_df['category'] == cat_sel]

# 5. Dashboard Header
st.title("🚀 Sales Performance Hub")

# 6. KPI Metrics (Compacted)
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Sales", f"₹{filtered_df['Total_Sales'].sum():,.0f}")
col2.metric("📦 Quantity", f"{filtered_df['quantity'].sum():,.0f}")
col3.metric("📈 Profit", f"₹{filtered_df['profit'].sum():,.0f}")
col4.metric("🛒 Avg Order", f"₹{filtered_df['Total_Sales'].mean():,.0f}")

# 7. Dashboard Content (Compact Heights for One-Page)
chart_height = 250

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    fig_cat = px.bar(filtered_df.groupby('category')['Total_Sales'].sum().reset_index(), 
                     x='category', y='Total_Sales', color='category',
                     height=chart_height, template="plotly_white", title="Sales by Category")
    fig_cat.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_cat, use_container_width=True)

with row1_col2:
    fig_payment = px.bar(filtered_df.groupby('paymentmode')['Total_Sales'].sum().reset_index(), 
                         x='paymentmode', y='Total_Sales', color='paymentmode',
                         height=chart_height, template="plotly_white", title="Sales by Payment")
    fig_payment.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_payment, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthly_sales = filtered_df.groupby('month')['Total_Sales'].sum().reindex(month_order).reset_index()
    fig_month = px.line(monthly_sales, x='month', y='Total_Sales', markers=True,
                        height=chart_height, template="plotly_white", title="Monthly Trend")
    fig_month.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_month, use_container_width=True)

with row2_col2:
    city_sales = filtered_df.groupby('city')['Total_Sales'].sum().sort_values(ascending=False).head(10).reset_index()
    fig_city = px.line(city_sales, x='city', y='Total_Sales', markers=True,
                       height=chart_height, template="plotly_white", title="Top Cities")
    fig_city.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_city, use_container_width=True)

# Sunburst in a container to save space
st.markdown("### 📊 Hierarchy Analysis")
fig_sun = px.sunburst(filtered_df, path=['category', 'sub-category'], values='Total_Sales',
                      color='Total_Sales', color_continuous_scale='Blues',
                      height=300, title="Category Depth")
fig_sun.update_layout(margin=dict(l=0, r=0, t=40, b=0))
st.plotly_chart(fig_sun, use_container_width=True)
