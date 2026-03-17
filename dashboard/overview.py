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
        self.data = json.loads(connection.get_request(sys.argv[1] + "/latest/").text)
        self.data_average = json.loads(connection.get_request(sys.argv[1] + "/average/").text)

    def get_value_unit(self, key):
        return str(self.data[key]) + Values.code_units[key]
    
    def get_average_data_list(self, code):
        average_data_list = []
        for i in range(0, len(self.data_average)):
            average_data_list.append(self.data_average[i][code])
        return average_data_list

    def render_metrics(self):
        temperature, humidity = st.columns(2)
        temperature_surface, pressure = st.columns(2)
        dew_point_temperature, wind_speed = st.columns(2)
        temperature.metric("Temperature", self.get_value_unit("TAAVG1M"), chart_data = self.get_average_data_list("AVG_TAAVG1M"), border = True)
        humidity.metric("Humidity", self.get_value_unit("RHAVG1M"), chart_data = self.get_average_data_list("AVG_RHAVG1M"), border = True)
        temperature_surface.metric("Temperature at ground surface", self.get_value_unit("TG2"), chart_data = self.get_average_data_list("AVG_TG2"), border = True)
        pressure.metric("Atmospheric pressure", self.get_value_unit("PAAVG1M"), chart_data = self.get_average_data_list("AVG_PAAVG1M"), border = True)
        dew_point_temperature.metric("Dew point temperature", self.get_value_unit("DPAVG1M"), chart_data = self.get_average_data_list("AVG_DPAVG1M"), border = True)
        wind_speed.metric("Wind speed", self.get_value_unit("WS"), chart_data = self.get_average_data_list("AVG_WS"), border = True)

renderer = MetricRenderer()
renderer.render_metrics()