import streamlit as st
from utils.warnings import Warnings

warnings = Warnings()

st.set_page_config(
    page_title = "Meteo Dashboard",
    page_icon = "⛅"
)

with st.spinner("Loading page..."):
    pg = st.navigation(
        [st.Page("pages/overview.py", title = "Overview", icon = ":material/bar_chart:", default = True), 
         st.Page("pages/measurements.py", title = "Measurements", icon = ":material/thermometer:"),
         st.Page("pages/visualizations.py", title = "Visualizations", icon = ":material/area_chart:")], position = "top")
    if warnings.check_available_warnings():
        st.warning(warnings)
    pg.run()