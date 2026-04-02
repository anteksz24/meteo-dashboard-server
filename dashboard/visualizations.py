import requests, sys, json, streamlit as st, pandas as pd, altair as alt
from utils.formatter import Formatter
from utils.constants import MeteoConstants
from utils.fetcher import Fetcher
from datetime import datetime, timedelta

formatter = Formatter()
fetcher = Fetcher()

def render_chart(parameters, start_date, end_date, average, interval, y_axis_zero):
    if not average:
        range_data = fetcher.fetch_data_from_api("range", start_date, end_date)
    else:
        range_data = fetcher.fetch_data_from_api("average", start_date, end_date, interval)
    timestamps = formatter.get_values(range_data, ["datetime"] if not average else ["datetime_bin"]).values
    measurements = formatter.get_values(range_data, parameters).values
    
    dataframe_values_dict = {"datetime": [timestamp[0] for timestamp in timestamps]}
    for parameter in range(len(parameters)):
        data_list = [measurements[row][parameter] for row in range(len(measurements))]
        dataframe_values_dict[formatter.get_parameters_descriptions(parameters[parameter])] = data_list
    dataframe = pd.DataFrame(dataframe_values_dict).melt(id_vars = "datetime")
    
    chart = (
        alt.Chart(dataframe)
        .mark_line()
        .encode(
            x = alt.X("datetime:T", title = ""),
            y = alt.Y("value:Q", title = f"{formatter.get_parameters_descriptions(parameters[0])} ({MeteoConstants.CONSTS_INFO[parameters[0]]["unit"]})" if len(parameters) == 1 else "").scale(zero = y_axis_zero),
            color = alt.Color("variable:N", title = "Parameters", legend = alt.Legend(orient = "bottom"))
        )
    )
    
    st.altair_chart(chart)

def render_menu():
    parameters = st.multiselect(
        label = "Parameters",
        options = formatter.remove_parameters_from_parameter_list(list(MeteoConstants.CONSTS_INFO.keys()), ["id", "datetime", "datetime_bin"]),
        format_func = lambda x: MeteoConstants.CONSTS_INFO[x]["description"]
    )
    start_date = st.datetime_input(label = "Start date", value = datetime.today() - timedelta(days = 1))
    end_date = st.datetime_input(label = "End date")
    advanced_options = st.expander(label = "Advanced options")
    with advanced_options:
        y_axis_zero = st.checkbox(label = "Start Y axis at 0 value", value = False)
        average = st.checkbox(label = "Use average data at set intervals", value = True)
        interval = st.number_input(label = "Interval (minutes)", value = 5, min_value = 1, disabled = not average)

    if st.button("Generate chart", disabled = not parameters):
        render_chart(parameters, start_date, end_date, average, interval, y_axis_zero)

render_menu()