import asyncio, streamlit as st
from utils.fetcher import WebSocketConnector
from utils.formatter import Formatter
from utils.constants import MeteoConstants

async def render_websocket_data():
    raw_measurements_expander_placeholder = st.empty()
    metrics_expander_placeholder = st.empty()
    async for measurement in WebSocketConnector().start_websocket_connection():
        with raw_measurements_expander_placeholder.expander(label = "Raw WebSocket measurements"):
            st.write(measurement)
        with metrics_expander_placeholder.expander(label = "Measurements from WebSocket connection as metrics"):
            columns = st.columns(3)
            for measurement_parameter in range(0, len(measurement[0].keys())):
                column = columns[measurement_parameter % 3]
                column.metric(
                    label = MeteoConstants.CONSTS_INFO[list(measurement[0].keys())[measurement_parameter]]["description"],
                    value = Formatter().get_values(data = measurement, parameters = [list(measurement[0].keys())[measurement_parameter]]).values_units[0][0],
                    border = True
                )

asyncio.run(render_websocket_data())