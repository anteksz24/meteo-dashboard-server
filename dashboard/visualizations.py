import requests, sys, json, streamlit as st, pandas as pd
from formatters import Formatters
from values import Values
from datetime import datetime, timedelta

f = Formatters()

code = st.selectbox(
    label = "Parameter",
    options = Values.code_descriptions.keys(),
    format_func = lambda x: Values.code_descriptions[x],
    index = None
)
start_date = st.date_input(label = "Start date", value = datetime.today() - timedelta(days = 1))
end_date = st.date_input(label = "End date")

if st.button("Generate chart"):
    if code == None:
        st.error("Select parameter from the list.")
    else:
        range_data = json.loads(requests.get(sys.argv[1] + f"/range?start={start_date}&end={end_date}").text)
        timestamps = f.get_values(range_data, "DT", False)
        measurements = f.get_values(range_data, code, False)

        dataframe = pd.DataFrame({"DT": timestamps, code: measurements}).set_index("DT")

        st.line_chart(dataframe)