class MeteoConstants:
    __DATA = [
        ("id", "Primary ID number", "", None, None),
        ("air_temp_avg_1m", "Air temperature (1 minute average)", "°C", False, "line"),
        ("humidity_avg_1m", "Relative humidity (1 minute average)", "%", False, "line"),
        ("dewpoint_avg_1m", "Dew point temperature (1 minute average)", "°C", False, "line"),
        ("precipitation_sum_1h", "Precipitation accumulation (1 hour)", "mm", True, "bar"),
        ("solar_rad_avg_1m", "Global solar radiation (1 minute average)", "W/m²", True, "bar"),
        ("sunshine_dur_1m", "Sunshine duration (1 minute)", "min", True, "line"),
        ("sunshine_dur_sum_1d", "Sunshine duration (1 day sum)", "min", True, "bar"),
        ("air_temp_min_1d", "Air temperature (1 day minimum)", "°C", False, "line"),
        ("air_temp_max_1d", "Air temperature (1 day maximum)", "°C", False, "line"),
        ("humidity_min_1d", "Relative humidity (1 day minimum)", "%", False, "line"),
        ("humidity_max_1d", "Relative humidity (1 day maximum)", "%", False, "line"),
        ("air_temp_5cm_above_ground_avg_1m", "Air temperature 5 cm above ground (1 minute average)", "°C", False, "line"),
        ("air_temp_surface_avg_1m", "Air temperature at ground surface (1 minute average)", "°C", False, "line"),
        ("ground_temp_5cm_avg_1m", "Ground temperature 5 cm under surface (1 minute average)", "°C", False, "line"),
        ("ground_temp_10cm_avg_1m", "Ground temperature 10 cm under surface (1 minute average)", "°C", False, "line"),
        ("ground_temp_20cm_avg_1m", "Ground temperature 20 cm under surface (1 minute average)", "°C", False, "line"),
        ("ground_temp_50cm_avg_1m", "Ground temperature 50 cm under surface (1 minute average)", "°C", False, "line"),
        ("ground_temp_100cm_avg_1m", "Ground temperature 100 cm under surface (1 minute average)", "°C", False, "line"),
        ("wind_direction_inst", "Wind direction (instant)", "°", False, "line"),
        ("wind_speed_inst", "Wind speed (instant)", "m/s", True, "line"),
        ("wind_direction_avg_2m", "Wind direction (2 minutes average)", "°", False, "line"),
        ("wind_direction_max_2m", "Wind direction (2 minutes maximum)", "°", False, "line"),
        ("wind_direction_min_2m", "Wind direction (2 minutes minimum)", "°", False, "line"),
        ("wind_speed_avg_2m", "Wind speed (2 minutes average)", "m/s", True, "line"),
        ("wind_speed_max_2m", "Wind speed (2 minutes maximum)", "m/s", True, "line"),
        ("wind_speed_min_2m", "Wind speed (2 minutes minimum)", "m/s", True, "line"),
        ("pressure_avg_1m", "Atmospheric pressure (1 minute average)", "hPa", True, "line"),
        ("pressure_adj_avg_1m", "Atmospheric pressure reduced to sea level (1 minute average)", "hPa", True, "line"),
        ("datetime", "Datetime", "", None, None),
        ("datetime_bin", "Datetime at set interval", "", None, None),
    ]

    CONSTS_INFO = {
        const: {"description": description, "unit": unit, "unit_space": unit_space, "default_chart_type": default_chart_type}
        for const, description, unit, unit_space, default_chart_type in __DATA
    }
    
    @staticmethod
    def get_unit_space_by_unit(unit):
        unit_space = [data["unit_space"] for data in MeteoConstants.CONSTS_INFO.values() if unit == data["unit"]]
        return False if not unit_space else unit_space[0]

class ChartConstants:
    __DATA = [
        (None, "Default type for this parameter"),
        ("line", "Line"),
        ("bar", "Bar"),
        ("area", "Area"),
        ("point", "Point"),
        ("square", "Square"),
    ]

    CHART_TYPES = {
        chart_type: {"chart_type_visible_name": chart_type_visible_name}
        for chart_type, chart_type_visible_name in __DATA
    }