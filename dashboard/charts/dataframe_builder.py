import pandas as pd

class DataframeBuilder:
    def __init__(self, formatter):
        self.formatter = formatter

    def build_dataframe(self, measurements, config):
        timestamps = self.formatter.get_values(measurements, ["datetime"] if not config.average else ["datetime_bin"]).values
        measurements = self.formatter.get_values(measurements, config.parameters).values
        
        dataframe_values_dict = {"datetime": [timestamp[0] for timestamp in timestamps]}
        for parameter in range(len(config.parameters)):
            data_list = [measurements[row][parameter] for row in range(len(measurements))]
            dataframe_values_dict[self.formatter.get_parameters_descriptions(config.parameters[parameter])] = data_list
        
        return pd.DataFrame(dataframe_values_dict).melt(id_vars = "datetime")