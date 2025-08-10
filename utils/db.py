import pandas as pd
import pyodbc
import streamlit as st

def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={st.secrets['server']};"
        f"DATABASE={st.secrets['database']};"
        f"UID={st.secrets['username']};"
        f"PWD={st.secrets['password']};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    return pyodbc.connect(conn_str)

def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

