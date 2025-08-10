# app.py
import streamlit as st
import pandas as pd
import numpy as np

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="FinSight",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# Title & Intro
# -----------------------
st.title("📊 FinSight – Financial Insights Dashboard")
st.markdown("""
Welcome to **FinSight**, your interactive platform for exploring and analyzing financial data.
Upload your dataset, and we'll help you visualize trends, performance metrics, and actionable insights.
""")

# -----------------------
# File Upload
# -----------------------
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # -----------------------
    # Basic Stats
    # -----------------------
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # -----------------------
    # Column Selector
    # -----------------------
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_columns:
        selected_col = st.selectbox("Select a column to visualize", numeric_columns)
        st.line_chart(df[selected_col])
    else:
        st.warning("No numeric columns found to visualize.")

else:
    st.info("Please upload a CSV or Excel file to get started.")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
