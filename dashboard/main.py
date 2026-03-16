import streamlit as st

st.set_page_config(
    page_title = "Meteo Dashboard",
    page_icon = "⛅"
)

with st.spinner("Loading page..."):
    pg = st.navigation([st.Page("overview.py"), st.Page("measurements.py")], position = "top")
    pg.run()