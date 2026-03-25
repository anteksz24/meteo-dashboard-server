import requests, sys, json, streamlit as st, pandas as pd, altair as alt
from utils.formatter import Formatter
from utils.constants import MeteoConstants
from datetime import datetime, timedelta

formatter = Formatter()

codes = st.multiselect(
    label = "Parameters",
    options = formatter.remove_codes_from_code_list(list(MeteoConstants.CODES_INFO.keys()), ["ID", "S", "RNAME", "PW15M", "VIS", "PRSUM1H", "EXTDC", "STATUS", "DT", "DT_BIN"]),
    format_func = lambda x: MeteoConstants.CODES_INFO[x]["description"]
)
start_date = st.datetime_input(label = "Start date", value = datetime.today() - timedelta(days = 1))
end_date = st.datetime_input(label = "End date")
advanced_options = st.expander(label = "Advanced options")
with advanced_options:
    y_axis_zero = st.checkbox(label = "Start Y axis at 0 value", value = False)
    average = st.checkbox(label = "Use average data at set intervals", value = True)
    interval = st.number_input(label = "Interval (minutes)", value = 5, min_value = 1, disabled = not average)
    
if st.button("Generate chart"):
    if not codes:
        st.error("Select at least one parameter from the list.")
    else:
        if not average:
            range_data = json.loads(requests.get(sys.argv[1] + f"/range?start={start_date}&end={end_date}").text)
        else:
            range_data = json.loads(requests.get(sys.argv[1] + f"/average?start={start_date}&end={end_date}&interval={interval}").text)
        timestamps = formatter.get_values(range_data, ["DT"] if not average else ["DT_BIN"]).values
        measurements = formatter.get_values(range_data, codes).values

        dataframe_values_dict = {"DT": [timestamp[0] for timestamp in timestamps]}
        for code in range(len(codes)):
            data_list = [measurements[row][code] for row in range(len(measurements))]
            dataframe_values_dict[formatter.get_codes_descriptions(codes[code])] = data_list
        dataframe = pd.DataFrame(dataframe_values_dict).melt(id_vars = "DT")
        
        chart = (
            alt.Chart(dataframe)
            .mark_line()
            .encode(
                x = alt.X("DT:T", title = ""),
                y = alt.Y("value:Q", title = f"{formatter.get_codes_descriptions(codes[0])} ({MeteoConstants.CODES_INFO[codes[0]]["unit"]})" if len(codes) == 1 else "").scale(zero = y_axis_zero),
                color = alt.Color("variable:N", title = "Parameters", legend = alt.Legend(orient = "bottom"))
            )
        )
        
        st.altair_chart(chart)