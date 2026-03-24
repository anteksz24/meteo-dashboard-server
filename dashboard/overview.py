import requests, sys, json, streamlit as st
from formatter import Formatter

latest_data = json.loads(requests.get(sys.argv[1] + "/latest/").text)
average_data = json.loads(requests.get(sys.argv[1] + "/average/").text)
formatter = Formatter()

def render_metrics():
    metrics = [
        ("Temperature", "TAAVG1M"),
        ("Humidity", "RHAVG1M"),
        ("Temperature at ground surface", "TG2"),
        ("Atmospheric pressure", "PAAVG1M"),
        ("Temperature 5 cm above ground", "TG1"),
        ("Wind speed", "WS")
    ]

    columns = st.columns(2)
    for i in range(0, len(metrics)):
        column = columns[i % 2]
        column.metric(
            label = metrics[i][0],
            value = formatter.get_values_from_dict(latest_data, metrics[i][1]).value_unit,
            chart_data = formatter.get_values_from_list(average_data, metrics[i][1]).value,
            border = True
        )

render_metrics()