import streamlit as st

st.set_page_config(
    page_title = "Meteo Dashboard",
    page_icon = "⛅"
)

with st.spinner("Loading page..."):
    pg = st.navigation(
        [st.Page("overview.py", title = "Overview", icon = ":material/bar_chart:", default = True), 
         st.Page("measurements.py", title = "Measurements", icon = ":material/thermometer:")], position = "top")
    pg.run()