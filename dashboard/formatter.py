from constants import MeteoConstants

class ValueWithUnit:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.value_unit = self.__get_value_unit()
    
    def __get_value_unit(self):
        if isinstance(self.value, list):
            return [str(self.value[i]) + str(self.unit[i]) for i in range(len(self.value))]
        else:
            return str(self.value) + str(self.unit)

class Formatter:
    def get_values_from_dict(self, data: dict, codes):
        if isinstance(codes, str):
            value = data.get(codes)
            unit = MeteoConstants.CODE_UNITS.get(codes)
            return ValueWithUnit(value, unit)
        elif isinstance(codes, list):
            values = [data[code] for code in codes]
            unit = [MeteoConstants.CODE_UNITS.get(code) for code in codes]
            return ValueWithUnit(values, unit)

    def get_values_from_list(self, data: list, codes):
        if isinstance(codes, str):
            values = [data[i][codes] for i in range(len(data))]
            unit = [MeteoConstants.CODE_UNITS.get(codes) for measurement in data]
            return ValueWithUnit(values, unit)
        elif isinstance(codes, list):
            values = []
            units = []
            for measurement in data:
                values.append([measurement[code] for code in codes])
                units.append([MeteoConstants.CODE_UNITS.get(code) for code in codes])
            return ValueWithUnit(values, units)

    def remove_values(self, data, codes):
        for code in codes:
            data.pop(code)
        return data

    def get_codes_descriptions(self, codes):
        codes_descriptions = [MeteoConstants.CODE_DESCRIPTIONS[code] for code in codes]
        return codes_descriptions