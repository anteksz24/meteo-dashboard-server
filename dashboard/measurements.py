import requests, json, sys, pandas as pd, streamlit as st
from formatter import Formatter

latest_data = json.loads(requests.get(sys.argv[1] + "/latest/").text)
formatter = Formatter()

def render_frame():
    timestamp = latest_data["DT"]
    data = formatter.remove_values(latest_data, ["ID", "DT", "S", "RNAME", "PW15M", "VIS", "PRSUM1H", "EXTDC", "STATUS"])

    dataframe = pd.DataFrame(
        {
            "Parameter": formatter.get_codes_descriptions(list(data.keys())),
            "Value": formatter.get_values_from_dict(data, list(data.keys())).value_unit,
        }
    )
    
    st.dataframe(dataframe, hide_index = True)
    st.write("**Last data update:** ", timestamp)   

render_frame()