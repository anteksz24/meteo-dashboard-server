import altair as alt
from charts.dataframe_builder import DataframeBuilder
from utils.constants import MeteoConstants

class ChartBuilder:
    def __init__(self, fetcher, formatter):
        self.fetcher = fetcher
        self.formatter = formatter
        self.dataframe_builder = DataframeBuilder(formatter)

    def get_y_axis_title(self, parameters):
        if len(parameters) == 1:
            return f"{self.formatter.get_parameters_descriptions(parameters[0])} [{MeteoConstants.CONSTS_INFO[parameters[0]]["unit"]}]"
        else:
            return ""

    def build_chart(self, config):
        chart = alt.Chart(data = self.dataframe_builder.build_dataframe(self.fetcher.measurements, config),
                          mark = config.chart_type,
                          height = 400 + 20 * len(config.parameters),
                          encoding = alt.FacetedEncoding(x = alt.X(shorthand = "datetime:T",
                                                                   title = ""),
                                                         y = alt.Y(shorthand = "value:Q",
                                                                   title = self.get_y_axis_title(config.parameters),
                                                                   scale = alt.Scale(zero = config.y_axis_zero)),
                                                         color = alt.Color(shorthand = "variable:N",
                                                                           title = "Parameters",
                                                                           legend = alt.Legend(orient = "bottom",
                                                                                               labelLimit = 0,
                                                                                               columns = 1)),
                                                         tooltip = [alt.Tooltip(title = "Datetime",
                                                                                shorthand = "datetime:T",
                                                                                timeUnit = "utcyearmonthdatehoursminutes"),
                                                                    alt.Tooltip(title = "Parameter",
                                                                                shorthand = "variable:N"),
                                                                    alt.Tooltip(title = "Value",
                                                                                shorthand = "value:Q")]))
        return chart