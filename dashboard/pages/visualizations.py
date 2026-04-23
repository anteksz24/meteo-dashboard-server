import streamlit as st
from utils.formatter import Formatter
from utils.constants import MeteoConstants
from utils.fetcher import StaticMeasurementsFetcher
from charts.chart_builder import ChartBuilder
from charts.config import ChartConfig
from datetime import datetime, timedelta

formatter = Formatter()

def render_chart_ui():
    if "start_date" not in st.session_state:
        st.session_state["start_date"] = datetime.today() - timedelta(days = 1)
        
    parameters = st.multiselect(
        label = "Parameters",
        options = formatter.remove_parameters_from_parameter_list(list(MeteoConstants.CONSTS_INFO.keys()), ["id", "datetime", "datetime_bin"]),
        format_func = lambda x: MeteoConstants.CONSTS_INFO[x]["description"]
    )
    start_date = st.datetime_input(label = "Start date", key = "start_date")
    end_date = st.datetime_input(label = "End date")
    advanced_options = st.expander(label = "Advanced options")
    with advanced_options:
        y_axis_zero = st.checkbox(label = "Start Y axis at 0 value", value = False)
        average = st.checkbox(label = "Use average data at set intervals", value = True)
        interval = st.number_input(label = "Interval (minutes)", value = 5, min_value = 1, disabled = not average)

    if st.button("Generate chart", disabled = not parameters):
        with st.spinner("Generating chart..."):
            config = ChartConfig(
                parameters = parameters,
                start_date = start_date,
                end_date = end_date,
                average = average,
                interval = interval,
                y_axis_zero = y_axis_zero
            )
            fetcher = StaticMeasurementsFetcher(endpoint_name = "range" if not average else "average", start_date = start_date, end_date = end_date, interval = interval)
            chart = ChartBuilder(fetcher, formatter).build_chart(config)
            st.altair_chart(chart)

render_chart_ui()