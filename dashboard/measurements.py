import streamlit as st
import pandas as pd
import requests
import json
import sys
from values import Values

class Connection:
    def get_request(self, endpoint):
        try:
            return requests.get(url = endpoint)
        except requests.exceptions.RequestException:
            return None

class DataframeRenderer:
    def __init__(self):
        self.endpoint = sys.argv[1]
        self.connection = Connection()

    def render_frame(self):
        request = self.connection.get_request(self.endpoint)
        if request is not None:
            if request.status_code == 200:
                data = json.loads(request.text)
                timestamp = data["DT"]
                data.pop("ID")
                data.pop("DT")
                keys = list(data.keys())
                keys_descriptions = list(data.keys())
                values = list(data.values())
                values_units = list(data.values())

                for i in range(0, len(keys)):
                    if list(data.keys())[i] in list(Values.code_descriptions.keys()):
                        keys_descriptions[i] = Values.code_descriptions[keys[i]]

                for i in range(0, len(values)):
                    values_units[i] = str(values[i]) + Values.code_units[keys[i]]

                dataframe = pd.DataFrame(
                    {
                        "Key": keys_descriptions,
                        "Value": values_units,
                    }
                )
                st.dataframe(dataframe, hide_index = True)
                st.write("**Last data update:** ", timestamp)   
            elif request.status_code == 404:
                st.error("No data in API.")
            else:
                st.error("An unknown error occurred.")
        else:
            st.error("Cannot connect to API.")
    
renderer = DataframeRenderer()
renderer.render_frame()