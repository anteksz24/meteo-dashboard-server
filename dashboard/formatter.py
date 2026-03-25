from constants import MeteoConstants
import streamlit as st

class ValueWithUnit:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.value_unit = self.__get_value_unit()

    def __get_value_unit(self):
        if isinstance(self.value, list):
            return [str(self.value[i]) + " " + str(self.unit[i]) if MeteoConstants.get_unit_space_by_unit(self.unit[i]) else str(self.value[i]) + str(self.unit[i]) for i in range(len(self.value))]
        else:
            return (str(self.value) + " " + str(self.unit)) if MeteoConstants.get_unit_space_by_unit(self.unit) else (str(self.value) + str(self.unit))

class Formatter:
    def get_values_from_dict(self, data: dict, codes):
        if isinstance(codes, str):
            value = data.get(codes)
            unit = MeteoConstants.CODES_INFO[codes]["unit"]
            return ValueWithUnit(value, unit)
        elif isinstance(codes, list):
            values = [data[code] for code in codes]
            unit = [MeteoConstants.CODES_INFO[code]["unit"] for code in codes]
            return ValueWithUnit(values, unit)

    def get_values_from_list(self, data: list, codes):
        if isinstance(codes, str):
            values = [data[i][codes] for i in range(len(data))]
            unit = [MeteoConstants.CODES_INFO[codes]["unit"] for measurement in data]
            return ValueWithUnit(values, unit)
        elif isinstance(codes, list):
            values = []
            units = []
            for measurement in data:
                values.append([measurement[code] for code in codes])
                units.append([MeteoConstants.CODES_INFO[code]["unit"] for code in codes])
            return ValueWithUnit(values, units)

    def remove_values(self, data, codes):
        data_values_removed = data
        if isinstance(data, dict):
            for code in codes:
                data_values_removed.pop(code)
            return data_values_removed
        else:
            for code in codes:
                data_values_removed.remove(code)
            return data_values_removed

    def get_codes_descriptions(self, codes):
        if isinstance(codes, list):
            return [MeteoConstants.CODES_INFO[code]["description"] for code in codes]
        else:
            return MeteoConstants.CODES_INFO[codes]["description"]