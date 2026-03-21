import requests, json, sys, pandas as pd, streamlit as st
from formatters import Formatters

latest_data = json.loads(requests.get(sys.argv[1] + "/latest/").text)
f = Formatters()

def render_frame():
    timestamp = latest_data["DT"]
    data = f.remove_values(latest_data, ["ID", "DT", "S", "RNAME", "PW15M", "VIS", "PRSUM1H", "EXTDC", "STATUS"])

    dataframe = pd.DataFrame(
        {
            "Parameter": f.get_codes_descriptions(list(data.keys())),
            "Value": f.get_values_from_dict(data, list(data.keys())).get_value_unit(),
        }
    )
    
    st.dataframe(dataframe, hide_index = True)
    st.write("**Last data update:** ", timestamp)   

render_frame()