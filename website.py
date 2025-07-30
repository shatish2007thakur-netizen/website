# Filename: app.py

import streamlit as st

st.title("Simple Calculator")
# Input numbers
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Select operation
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate on button click
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2

    st.success(f"Result: {result}")
