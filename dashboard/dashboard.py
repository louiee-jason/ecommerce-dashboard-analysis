import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('clean_data.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

st.title("E-Commerce Dashboard")

# filter
st.sidebar.header("Filter")
state = st.sidebar.selectbox("Select State", ["All"] + list(df['customer_state'].unique()))

if state != "All":
    df = df[df['customer_state'] == state]

# metrics
total_revenue = int(df['payment_value'].sum())
total_orders = df['order_id'].nunique()

col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"{total_revenue:,}")
col2.metric("Total Orders", total_orders)

# trend
st.subheader("Monthly Revenue Trend")

monthly = df.groupby('order_month')['payment_value'].sum().reset_index()

fig, ax = plt.subplots()
ax.plot(monthly['order_month'], monthly['payment_value'])
plt.xticks(rotation=45)
st.pyplot(fig)

# category
st.subheader("Top Product Categories")

category = df.groupby('product_category_name')['payment_value'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(category.index, category.values)
ax.invert_yaxis()
st.pyplot(fig)

# payment
st.subheader("Payment Distribution")

payment = df['payment_type'].value_counts()

fig, ax = plt.subplots()
ax.pie(payment, labels=payment.index, autopct='%1.1f%%')
st.pyplot(fig)