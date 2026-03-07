import streamlit as st

# 1. Title + Description
st.title("Simple Sales Dashboard")
st.write("This dashboard provides a quick overview of monthly sales performance.")

# 2. A selectbox with months
months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month to view sales:", months)

# 3. A static dictionary of monthly sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000,
    "May": 1800,
    "June": 1300,
    "July": 1600,
    "August": 1700,
    "September": 1400,
    "October": 1900,
    "November": 1100,
    "December": 1200


}

# 4. Display selected month's sales using st.metric()
st.subheader(f"Sales Data for {selected_month}")
st.metric(label="Total Sales", value=f"${sales[selected_month]}")

# 5. Display a bar chart
st.subheader("Monthly Sales Trend")
# Passing the list of values directly as requested
st.bar_chart(list(sales.values()))