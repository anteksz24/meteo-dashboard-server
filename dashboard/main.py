import streamlit as st
import pandas as pd
import requests
import json
import sys

class DataframeRenderer:
    def render_frame(self):
        data = json.loads(requests.get(url = sys.argv[1]).text)
        datetime = data["DT"]
        data.pop("DT")
        keys_list = list(data.keys())
        values_list = list(data.values())

        dataframe = pd.DataFrame(
            {
                "Key": keys_list,
                "Value": values_list,
            }
        )
        
        st.dataframe(dataframe, hide_index=True)
        st.write("Last data update: ", datetime)

renderer = DataframeRenderer()
renderer.render_frame()