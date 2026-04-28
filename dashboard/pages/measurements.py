import asyncio, pandas as pd, streamlit as st
from utils.formatter import Formatter, Timestamp
from utils.fetcher import WebSocketConnector

formatter = Formatter()

async def render_frame():
    dataframe_placeholder = st.empty()
    timestamp_placeholder = st.empty()

    async for latest_measurement in WebSocketConnector().start_websocket_connection():
        with dataframe_placeholder:
            latest_measurement_timestamp = Timestamp(latest_measurement[0]["datetime"]).timestamp
            latest_measurement_params_removed = formatter.remove_values_from_data_list(data = latest_measurement, parameters = ["id", "datetime"])

            dataframe = pd.DataFrame(
                {
                    "Parameter": formatter.get_parameters_descriptions(parameters = list(latest_measurement_params_removed[0].keys())),
                    "Value": formatter.get_values(data = latest_measurement_params_removed, parameters = list(latest_measurement_params_removed[0].keys())).values_units[0]
                }
            )
    
            dataframe_placeholder.dataframe(dataframe, hide_index = True)
            timestamp_placeholder.write(f"**Last data update:** {latest_measurement_timestamp}")

asyncio.run(render_frame())