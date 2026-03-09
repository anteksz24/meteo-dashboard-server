import streamlit as st
import pandas as pd
import requests
import json
import sys

class DataframeRenderer:
    def render_frame(self):
        data = json.loads(requests.get(url = sys.argv[1]).text)
        keys_list = list(data.keys())
        values_list = list(data.values())

        dataframe = pd.DataFrame(
            {
                "Key": keys_list,
                "Value": values_list,
            }
        )

        st.dataframe(dataframe, hide_index=True)

renderer = DataframeRenderer()
renderer.render_frame()