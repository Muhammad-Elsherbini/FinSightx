import pandas as pd
import pyodbc
import streamlit as st

def get_connection():
    try:
        conn_str =  f"""
            DRIVER={st.secrets.connections.fabric.driver};
            SERVER={st.secrets.connections.fabric.server};
            DATABASE={st.secrets.connections.fabric.database};
            UID={st.secrets.connections.fabric.username};
            PWD={st.secrets.connections.fabric.password};
            Encrypt=yes;
            TrustServerCertificate=no;"""
        
        return pyodbc.connect(conn_str)
    except Exception as e:
        st.error(f"Connection failed: {str(e)}")
        print('error')
        return None
def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

