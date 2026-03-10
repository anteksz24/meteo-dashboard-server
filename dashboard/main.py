import streamlit as st
import pandas as pd
import requests
import json
import sys

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
                data.pop("DT")
                keys_list = list(data.keys())
                values_list = list(data.values())
                dataframe = pd.DataFrame(
                    {
                        "Key": keys_list,
                        "Value": values_list,
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