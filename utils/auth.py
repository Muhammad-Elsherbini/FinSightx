import streamlit as st
import pandas as pd

def load_users():
    return pd.read_csv("data/users.csv")

def login():
    st.title("🔐 Login")
    users = load_users()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if ((users['username'] == username) & (users['password'] == password)).any():
            st.session_state["logged_in"] = True
            #st.experimental_rerun()
        else:
            st.error("Invalid credentials")

