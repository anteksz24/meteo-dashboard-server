class MeteoConstants:
    __DATA = [
        ("id", "Primary ID number", "", None),
        ("air_temp_avg_1m", "Air temperature (1 minute average)", "°C", False),
        ("humidity_avg_1m", "Relative humidity (1 minute average)", "%", False),
        ("dewpoint_avg_1m", "Dew point temperature (1 minute average)", "°C", False),
        ("precipitation_sum_1h", "Precipitation accumulation (1 hour)", "mm", True),
        ("solar_rad_avg_1m", "Global solar radiation (1 minute average)", "W/m²", True),
        ("sunshine_dur_1m", "Sunshine duration (1 minute)", "min", True),
        ("sunshine_dur_sum_1d", "Sunshine duration (1 day sum)", "min", True),
        ("air_temp_min_1d", "Air temperature (1 day minimum)", "°C", False),
        ("air_temp_max_1d", "Air temperature (1 day maximum)", "°C", False),
        ("humidity_min_1d", "Relative humidity (1 day minimum)", "%", False),
        ("humidity_max_1d", "Relative humidity (1 day maximum)", "%", False),
        ("air_temp_5cm_above_ground_avg_1m", "Air temperature 5 cm above ground", "°C", False),
        ("air_temp_surface_avg_1m", "Air temperature at ground surface", "°C", False),
        ("ground_temp_5cm_avg_1m", "Ground temperature 5 cm under surface", "°C", False),
        ("ground_temp_10cm_avg_1m", "Ground temperature 10 cm under surface", "°C", False),
        ("ground_temp_20cm_avg_1m", "Ground temperature 20 cm under surface", "°C", False),
        ("ground_temp_50cm_avg_1m", "Ground temperature 50 cm under surface", "°C", False),
        ("ground_temp_100cm_avg_1m", "Ground temperature 100 cm under surface", "°C", False),
        ("wind_direction_inst", "Wind direction", "°", False),
        ("wind_speed_inst", "Wind speed", "m/s", True),
        ("wind_direction_avg_2m", "Wind direction (2 minutes average)", "°", False),
        ("wind_direction_max_2m", "Wind direction (2 minutes maximum)", "°", False),
        ("wind_direction_min_2m", "Wind direction (2 minutes minimum)", "°", False),
        ("wind_speed_avg_2m", "Wind speed (2 minutes average)", "m/s", True),
        ("wind_speed_max_2m", "Wind speed (2 minutes maximum)", "m/s", True),
        ("wind_speed_min_2m", "Wind speed (2 minutes minimum)", "m/s", True),
        ("pressure_avg_1m", "Atmospheric pressure (1 minute average)", "hPa", True),
        ("pressure_adj_avg_1m", "Atmospheric pressure (reduced to sea level)", "hPa", True),
        ("datetime", "Datetime", "", None),
        ("datetime_bin", "Datetime at set interval", "", None),
    ]

    CONSTS_INFO = {
        const: {"description": description, "unit": unit, "unit_space": unit_space}
        for const, description, unit, unit_space in __DATA
    }
    
    @staticmethod
    def get_unit_space_by_unit(unit):
        unit_space = [data["unit_space"] for data in MeteoConstants.CONSTS_INFO.values() if unit == data["unit"]]
        return False if not unit_space else unit_space[0]