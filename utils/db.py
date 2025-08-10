import pandas as pd
import pyodbc
import streamlit as st

def get_connection():
    try:
        conn_str =  f"""
            DRIVER=ODBC Driver 18 for SQL Server;
            SERVER=l23jvmddsbrerl5c25nljc52oq-3dyzqrdrcf7uxgalftx4qvmqza.datawarehouse.fabric.microsoft.com;
            DATABASE={st.secrets.database};
            UID={st.secrets.username};
            PWD={st.secrets.password};
            Encrypt=yes;
            TrustServerCertificate=no;
        """
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

