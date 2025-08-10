import pandas as pd
import pymssql
import streamlit as st

def get_connection():
    """
    Establish connection to Microsoft Fabric Data Warehouse
    using Active Directory Password authentication.
    """
    try:
        # Load secrets
        server = st.secrets["fabric"]["server"]
        database = "l23jvmddsbrerl5c25nljc52oq-3dyzqrdrcf7uxgalftx4qvmqza.datawarehouse.fabric.microsoft.com" #st.secrets["fabric"]["database"]
        username = st.secrets["fabric"]["username"]
        password = st.secrets["fabric"]["password"]
        conn = pymssql.connect(
            server=server,
            user=username,
            password=password,
            database=database,
            as_dict=False  # or True if you want dict rows
        )
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

