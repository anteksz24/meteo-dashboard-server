import streamlit as st
from utils.warnings import Warnings

warnings = Warnings()

st.set_page_config(
    page_title = "Meteo Dashboard",
    page_icon = "⛅"
)

st.markdown("""
<style>
[data-testid="stStatusWidget"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html = True)

pg = st.navigation(
    [st.Page(page = "pages/overview.py", title = "Overview", icon = ":material/bar_chart:", default = True),
     st.Page(page = "pages/measurements.py", title = "Measurements", icon = ":material/thermometer:"),
     st.Page(page = "pages/visualizations.py", title = "Visualizations", icon = ":material/area_chart:"),
     st.Page(page = "pages/debug.py", title = "Debug", icon =":material/cable:", visibility = "hidden")], position ="top")

if warnings.check_available_warnings():
    st.warning(warnings)

pg.run()