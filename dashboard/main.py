import streamlit as st

with st.spinner("Loading page..."):
    pg = st.navigation([st.Page("measurements.py")], position = "top")
    pg.run()