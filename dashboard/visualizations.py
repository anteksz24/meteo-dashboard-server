import requests, sys, json, streamlit as st, pandas as pd
from formatters import Formatters

f = Formatters()

code = st.text_input("Vaisala code")
start_date = st.text_input("Start date")
end_date = st.text_input("End date")

if st.button("Generate chart"):
    range_data = json.loads(requests.get(sys.argv[1] + f"/range?start={start_date}&end={end_date}").text)

    timestamps = f.get_values(range_data, "DT", False)
    measurements = f.get_values(range_data, code, False)

    dataframe = pd.DataFrame({"DT": timestamps, code: measurements}).set_index("DT")

    st.line_chart(dataframe)