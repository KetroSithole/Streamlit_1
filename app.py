import pandas as pd
import streamlit as st

# Add CSS to set background color to white
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load Excel file into DataFrame
excel_file = pd.read_excel('file1.xlsx')

excel_file2 = pd.read_excel('file2.xlsx')

# Display data on Streamlit
st.write(excel_file)
st.write(excel_file2)