import streamlit as st
from utils.auth import login

st.set_page_config(page_title="FinSightx", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    st.sidebar.success("✅ Logged in")
    st.sidebar.markdown("### Navigation")
    st.sidebar.page_link("pages/1_Dashboard.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/2_Chatbot.py", label="🤖 Chatbot")
    st.sidebar.page_link("pages/3_Placeholder.py", label="📝 Placeholder")
