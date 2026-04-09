import altair as alt
from charts.dataframe_builder import DataframeBuilder
from utils.constants import MeteoConstants

class ChartBuilder:
    def __init__(self, fetcher, formatter):
        self.fetcher = fetcher
        self.formatter = formatter
        self.dataframe_builder = DataframeBuilder(formatter)
    
    def build_chart(self, config):
        chart = (
            alt.Chart(self.dataframe_builder.build_dataframe(self.fetcher.fetch_data_from_api(
                "average" if config.average else "range", config.start_date, config.end_date, config.interval
            ), config))
            .mark_line()
            .encode(
                x = alt.X("datetime:T", 
                          title = ""),
                y = alt.Y("value:Q", 
                          title = f"{self.formatter.get_parameters_descriptions(config.parameters[0])} ({MeteoConstants.CONSTS_INFO[config.parameters[0]]["unit"]})" if len(config.parameters) == 1 else "")
                .scale(zero = config.y_axis_zero),
                color = alt.Color("variable:N", 
                                  title = "Parameters", 
                                  legend = alt.Legend(orient = "bottom", 
                                                      labelLimit = 0, 
                                                      columns = 1)
                )
            )
            .properties(
                height = 400 + 20 * len(config.parameters)
            )
        )
        
        return chart