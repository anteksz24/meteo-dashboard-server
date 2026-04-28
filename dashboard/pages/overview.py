import asyncio, streamlit as st
from utils.formatter import Formatter
from utils.fetcher import StaticMeasurementsFetcher, WebSocketConnector

formatter = Formatter()

async def render_metrics():
    average_data = StaticMeasurementsFetcher(endpoint_name = "average").measurements
    metrics_placeholder = st.empty()

    metrics = [
        ("Air temperature", "air_temp_avg_1m"),
        ("Humidity", "humidity_avg_1m"),
        ("Temperature at ground surface", "air_temp_surface_avg_1m"),
        ("Atmospheric pressure", "pressure_adj_avg_1m"),
        ("Temperature 5 cm above ground", "air_temp_5cm_above_ground_avg_1m"),
        ("Wind speed", "wind_speed_inst")
    ]

    async for latest_measurement in WebSocketConnector().start_websocket_connection():
        with metrics_placeholder:
            columns = st.columns(2)
            for i in range(0, len(metrics)):
                column = columns[i % 2]
                column.metric(
                    label = metrics[i][0],
                    value = formatter.get_values(data = latest_measurement, parameters = [metrics[i][1]]).values_units[0][0],
                    chart_data = [value[0] for value in formatter.get_values(data = average_data, parameters = [metrics[i][1]]).values
                                if value[0] is not None],
                    border = True
                )

asyncio.run(render_metrics())