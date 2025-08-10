import pandas as pd
import pyodbc
import streamlit as st

def get_connection():
    """
    Establish connection to Microsoft Fabric Data Warehouse
    using Active Directory Password authentication.
    """
    try:
        # Load secrets
        server = st.secrets["server"]
        database = st.secrets["database"]
        username = st.secrets["username"]
        password = st.secrets["password"]
        driver = "{ODBC Driver 18 for SQL Server}"

        connection_string = (
            f"DRIVER={driver};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            "Authentication=ActiveDirectoryPassword;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"  # Recommended: set to 'no' and ensure TLS
        )
        print('this is the connstring:',connection_string)
        conn = pyodbc.connect(connection_string)
        st.success("✅ Connected to Fabric Warehouse!", icon="✅")
        return conn

    except Exception as e:
        st.error(f"❌ Failed to connect to Fabric: {str(e)}", icon="🚨")
        st.info("💡 Check: Server name, credentials, SQL endpoint enabled in Fabric, and ODBC Driver 18.")
        st.exception(e)
        return None

def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

