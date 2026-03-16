import requests
import sys
import json
import streamlit as st
from values import Values

class Connection:
    def get_request(self, endpoint):
        try:
            return requests.get(url = endpoint)
        except requests.exceptions.RequestException:
            return None

class MetricRenderer:
    def __init__(self):
        connection = Connection()
        self.data = json.loads(connection.get_request(sys.argv[1]).text)
    
    def get_value_unit(self, key):
        return str(self.data[key]) + Values.code_units[key]

    def render_metrics(self):
        temperature, humidity = st.columns(2)
        temperature_surface, pressure = st.columns(2)
        wind_speed, wind_direction = st.columns(2)

        temperature.metric("Temperature", self.get_value_unit("TAAVG1M"), border = True)
        humidity.metric("Humidity", self.get_value_unit("RHAVG1M"), border = True)
        temperature_surface.metric("Temperature at ground surface", self.get_value_unit("TG2"), border = True)
        pressure.metric("Atmospheric pressure", self.get_value_unit("PAAVG1M"), border = True)
        wind_speed.metric("Wind speed", self.get_value_unit("WS"), border = True)
        wind_direction.metric("Dew point temperature", self.get_value_unit("DPAVG1M"), border = True)

renderer = MetricRenderer()
renderer.render_metrics()