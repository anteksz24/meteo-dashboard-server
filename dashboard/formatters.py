import streamlit as st
from values import Values

class Formatters:
    def get_values(self, data, codes, unit = True):
        values = []
        if isinstance(data, dict):
            if isinstance(codes, str):
                return str(data.get(codes)) + str(Values.code_units.get(codes)) if unit else data.get(codes)
            elif isinstance(codes, list) and len(codes) == 1:
                return str(data.get(codes[0])) + str(Values.code_units.get(codes[0])) if unit else data.get(codes[0])
            else:
                for i in range(len(codes)):
                    values.append(data.get(codes[i]))
                    if unit:
                        values[i] = str(values[i]) + Values.code_units.get(codes[i])
                return values[0] if len(values) == 1 else values
        elif isinstance(data, list):
            if isinstance(codes, str):
                for i in range(len(data)):
                    values.append(data[i][codes])
                return values
            else:
                for i in range(len(data)):
                    for x in range(len(codes)):
                        values.append(data[i][codes[x]])
                    if unit:
                        values[i] = str(values[i]) + Values.code_units.get(codes[x])
                return values

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