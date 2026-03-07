import streamlit as st
st.title("Product Management System")

st.sidebar.header("Add New Product")
product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Home & Kitchen", "Books", "Beauty"]
)

# Price number input
price = st.sidebar.number_input("Price", min_value=0.0, step=0.01)

# 2. When user clicks "Add Product"
if st.sidebar.button("Add Product"):
    if product_name:
        # Show a success message
        st.success(f"Product '{product_name}' added successfully!")
        
        # Show the product details in a clean format
        st.subheader("Product Details")
        st.markdown(f"""
        - **Name:** {product_name}
        - **Category:** {category}
        - **Price:** ${price:,.2f}
        """)
    else:
        st.error("Please enter a product name.")