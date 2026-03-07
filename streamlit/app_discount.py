import streamlit as st
st.title("Welcome to Streamlit!")
amount = st.number_input("Enter the original price:", min_value=0.0, step=1.0)
discount = st.slider("Select a discount percentage:", 0, 50, 1)
if st.button("Calculate Discounted Price"):
    discounted_price = amount * (1 - discount / 100)
    st.write(f"The discounted price is: ${discounted_price:.2f}")