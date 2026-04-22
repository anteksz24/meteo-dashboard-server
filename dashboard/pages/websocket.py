import os, ast, asyncio, time, streamlit as st
from websockets.sync.client import connect

websocket_url = os.getenv("METEO_WEBSOCKET_URL")

async def display_websocket_data():
    measurements_placeholder = st.empty()
    with connect(websocket_url) as websocket:
        while True:
            measurements = websocket.recv()
            measurements = ast.literal_eval(measurements[1:-1])
            measurements_placeholder.write(measurements)
            time.sleep(1)

asyncio.run(display_websocket_data())