import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("superstore.csv")

st.title("Sales & Revenue Dashboard")

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

st.write("Total Sales:", total_sales)
st.write("Total Profit:", total_profit)

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()

st.subheader("Sales by Category")
st.bar_chart(category_sales)
st.subheader("Top 5 Products")

top_products = filtered_df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

st.bar_chart(top_products)
st.subheader("Profit by Category")

profit_category = filtered_df.groupby('Category')['Profit'].sum()

st.bar_chart(profit_category)
st.subheader("Key Insights")

st.write("1. The highest sales come from:", top_products.index[0])
st.write("2. Total Profit:", total_profit)
st.write("3. Selected Region:", region)
one of [Index(['Central', 'Central', 'Central', 'Central', 'East', 'South', 
'South',\n       'South', 'South', 'South',\n       ...\n       'East', 'East', 'East', 
'Central', 'West', 'East', 'West', 'West',\n       'East', 'East'],\n      dtype='str', 
length=10194)] are in the [columns]"
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", total_sales)

with col2:
    st.metric("Total Profit", total_profit)
    profit_margin = (total_profit / total_sales) * 100

st.metric("Profit Margin (%)", round(profit_margin, 2))
st.title("Sales & Revenue Dashboard")
st.markdown("Interactive analysis of sales, profit, and performance")
df['Order Date'] = pd.to_datetime(df['Order Date'])

date = st.sidebar.date_input("Select Date Range", [])

if len(date) == 2:
    filtered_df = df[(df['Order Date'] >= str(date[0])) & (df['Order Date'] <= str(date[1]))]