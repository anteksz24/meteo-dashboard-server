import requests, json, sys, pandas as pd, streamlit as st
from utils.formatter import Formatter
from utils.fetcher import Fetcher

fetcher = Fetcher()
formatter = Formatter()

def render_frame():
    measurements = fetcher.fetch_data_from_api("latest")
    timestamp = measurements[0]["datetime"]
    data = formatter.remove_values_from_data_list(measurements, ["id", "datetime"])

    dataframe = pd.DataFrame(
        {
            "Parameter": formatter.get_parameters_descriptions(list(data[0].keys())),
            "Value": formatter.get_values(data, list(data[0].keys())).values_units[0],
        }
    )
    
    st.dataframe(dataframe, hide_index = True)
    st.write("**Last data update:** ", timestamp)   

render_frame()