import requests, sys, json, streamlit as st
from formatters import Formatters

latest_data = json.loads(requests.get(sys.argv[1] + "/latest/").text)
average_data = json.loads(requests.get(sys.argv[1] + "/average/").text)
f = Formatters()

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
                        value = f.get_values_from_dict(latest_data, metrics[i][1]).get_value_unit(),
                        chart_data = f.get_values_from_list(average_data, "AVG_" + metrics[i][1]).value,
                        border = True
                )

render_metrics()