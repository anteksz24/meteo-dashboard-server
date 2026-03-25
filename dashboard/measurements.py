import requests, json, sys, pandas as pd, streamlit as st
from utils.formatter import Formatter

latest_data = json.loads(requests.get(sys.argv[1] + "/latest/").text)
formatter = Formatter()

def render_frame():
    timestamp = latest_data[0]["DT"]
    data = formatter.remove_values_from_data_list(latest_data, ["ID", "DT", "S", "RNAME", "PW15M", "VIS", "PRSUM1H", "EXTDC", "STATUS"])

    dataframe = pd.DataFrame(
        {
            "Parameter": formatter.get_codes_descriptions(list(data[0].keys())),
            "Value": formatter.get_values(data, list(data[0].keys())).values_units[0],
        }
    )
    
    st.dataframe(dataframe, hide_index = True)
    st.write("**Last data update:** ", timestamp)   

render_frame()