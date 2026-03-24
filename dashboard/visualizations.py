import requests, sys, json, streamlit as st, pandas as pd
from formatter import Formatter
from constants import MeteoConstants
from datetime import datetime, timedelta

formatter = Formatter()

code = st.selectbox(
    label = "Parameter",
    options = formatter.remove_values(list(MeteoConstants.CODES_INFO.keys()), ["ID", "S", "RNAME", "PW15M", "VIS", "PRSUM1H", "EXTDC", "STATUS", "DT", "DT_BIN"]),
    format_func = lambda x: MeteoConstants.CODES_INFO[x]["description"],
    index = None
)
start_date = st.datetime_input(label = "Start date", value = datetime.today() - timedelta(days = 1))
end_date = st.datetime_input(label = "End date")
average = st.checkbox(label = "Use average data at set intervals", value = True)
interval = st.number_input(label = "Interval (minutes)", value = 5, min_value = 1, disabled = not average)

if st.button("Generate chart"):
    if code == None:
        st.error("Select parameter from the list.")
    else:
        if not average:
            range_data = json.loads(requests.get(sys.argv[1] + f"/range?start={start_date}&end={end_date}").text)
        else:
            range_data = json.loads(requests.get(sys.argv[1] + f"/average?start={start_date}&end={end_date}&interval={interval}").text)
        timestamps = formatter.get_values_from_list(range_data, "DT" if not average else "DT_BIN").value
        measurements = formatter.get_values_from_list(range_data, code).value

        dataframe = pd.DataFrame({"DT": timestamps, code: measurements}).set_index("DT")

        st.line_chart(dataframe)