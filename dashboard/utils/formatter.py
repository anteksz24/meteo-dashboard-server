import copy
from utils.constants import MeteoConstants

class ValuesWithUnits:
    def __init__(self, values, units):
        self.values = values
        self.units = units
        self.values_units = self.__get_values_units()

    def __get_values_units(self):
        values_units_list = []
        for value_in_list in range(len(self.values)):
            value_unit_list = [
                str(self.values[value_in_list][value]) + " " + str(self.units[value_in_list][value])
                if MeteoConstants.get_unit_space_by_unit(self.units[value_in_list][value])
                else str(self.values[value_in_list][value]) + str(self.units[value_in_list][value])
                for value in range(len(self.values[value_in_list]))
            ]
            values_units_list.append(value_unit_list)
        return values_units_list

class Formatter:
    def get_values(self, data: list, codes: list):
        values = []
        units = []
        for measurement in data:
            values.append([measurement[code] for code in codes])
            units.append([MeteoConstants.CONSTS_INFO[code]["unit"] for code in codes])
        return ValuesWithUnits(values, units)

    def remove_values_from_data_list(self, data, codes):
        data_values_removed = copy.deepcopy(data)
        for measurement in range(len(data)):
            for code in codes:
                data_values_removed[measurement].pop(code)
        return data_values_removed

    def remove_codes_from_code_list(self, code_list, codes_to_remove):
        codes_removed = copy.deepcopy(code_list)
        for code in codes_to_remove:
            codes_removed.remove(code)
        return codes_removed

    def get_codes_descriptions(self, codes):
        if isinstance(codes, list):
            return [MeteoConstants.CONSTS_INFO[code]["description"] for code in codes]
        else:
            return MeteoConstants.CONSTS_INFO[codes]["description"]