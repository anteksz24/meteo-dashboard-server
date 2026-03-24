import requests, sys, json, streamlit as st, pandas as pd
from formatter import Formatter
from constants import MeteoConstants
from datetime import datetime, timedelta

formatter = Formatter()

code = st.selectbox(
    label = "Parameter",
    options = MeteoConstants.CODES_INFO.keys(),
    format_func = lambda x: MeteoConstants.CODES_INFO[x]["description"],
    index = None
)
start_date = st.date_input(label = "Start date", value = datetime.today() - timedelta(days = 1))
end_date = st.date_input(label = "End date")

if st.button("Generate chart"):
    if code == None:
        st.error("Select parameter from the list.")
    else:
        range_data = json.loads(requests.get(sys.argv[1] + f"/range?start={start_date}&end={end_date}").text)
        timestamps = formatter.get_values_from_list(range_data, "DT").value
        measurements = formatter.get_values_from_list(range_data, code).value

        dataframe = pd.DataFrame({"DT": timestamps, code: measurements}).set_index("DT")

        st.line_chart(dataframe)