import requests, sys, json, streamlit as st, os
from utils.formatter import Formatter
from utils.fetcher import Fetcher

fetcher = Fetcher()
formatter = Formatter()

def render_metrics():
    latest_data = fetcher.fetch_data_from_api("latest")
    average_data = fetcher.fetch_data_from_api("average")
    
    metrics = [
        ("Temperature", "air_temp_avg_1m"),
        ("Humidity", "humidity_avg_1m"),
        ("Temperature at ground surface", "air_temp_surface_avg_1m"),
        ("Atmospheric pressure", "pressure_adj_avg_1m"),
        ("Temperature 5 cm above ground", "air_temp_5cm_above_ground_avg_1m"),
        ("Wind speed", "wind_speed_inst")
    ]

    columns = st.columns(2)
    for i in range(0, len(metrics)):
        column = columns[i % 2]
        column.metric(
            label = metrics[i][0],
            value = formatter.get_values(latest_data, [metrics[i][1]]).values_units[0][0],
            chart_data = [value[0] for value in formatter.get_values(average_data, [metrics[i][1]]).values 
                          if value[0] is not None],
            border = True
        )

render_metrics()