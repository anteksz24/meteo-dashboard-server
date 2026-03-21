from values import Values

class ValueWithUnit:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    
    def get_value_unit(self):
        return [str(self.value[i]) + str(self.unit[i]) for i in range(len(self.value))] if isinstance(self.value, list) else str(self.value) + str(self.unit)

class Formatters:
    def get_values_from_dict(self, data: dict, codes):
        if isinstance(codes, str):
            value = data.get(codes)
            unit = Values.code_units.get(codes)
            return ValueWithUnit(value, unit)
        elif isinstance(codes, list):
            values = [data[code] for code in codes]
            units = [Values.code_units.get(codes[i]) for i in range(len(codes))]
            return ValueWithUnit(values, units)

    def get_values_from_list(self, data: list, codes):
        if isinstance(codes, str):
            values = [data[i][codes] for i in range(len(data))]
            unit = [Values.code_units.get(codes) for i in range(len(data))]
            return ValueWithUnit(values, unit)
        elif isinstance(codes, list):
            pass

    def remove_values(self, data, codes):
        for i in range(len(codes)):
            data.pop(codes[i])
        return data

    def get_codes_descriptions(self, codes):
        codes_descriptions = []
        for i in range(len(codes)):
            if list(codes)[i] in list(Values.code_descriptions.keys()):
                codes_descriptions.append(Values.code_descriptions[codes[i]])
        return codes_descriptions