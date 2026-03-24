class MeteoConstants:
    __DATA = [
        ("ID", "Primary ID number", "", None),
        ("S", "Weather station code", "", None),
        ("RNAME", "Record name", "", None),
        ("PW15M", "Present weather (WMO code table 4680)", "", None),
        ("VIS", "Visibility", "m", True),
        ("TAAVG1M", "Air temperature (1 minute average)", "°C", False),
        ("RHAVG1M", "Relative humidity (1 minute average)", "%", False),
        ("DPAVG1M", "Dew point temperature (1 minute average)", "°C", False),
        ("PRSUM1H", "Precipitation accumulation (1 hour)", "mm", True),
        ("SRAVG1M", "Global solar radiation (1 minute average)", "W/m²", True),
        ("SDUR1M", "Sunshine duration (1 minute)", "min", True),
        ("SRDSUM1D", "Sunshine duration (1 day sum)", "min", True),
        ("TAMIN1D", "Air temperature (1 day minimum)", "°C", False),
        ("TAMAX1D", "Air temperature (1 day maximum)", "°C", False),
        ("RHMIN1D", "Relative humidity (1 day minimum)", "%", False),
        ("RHMAX1D", "Relative humidity (1 day maximum)", "%", False),
        ("TG1", "Air temperature 5 cm above ground", "°C", False),
        ("TG2", "Air temperature at ground surface", "°C", False),
        ("TG3", "Ground temperature 5 cm under surface", "°C", False),
        ("TG4", "Ground temperature 10 cm under surface", "°C", False),
        ("TG5", "Ground temperature 20 cm under surface", "°C", False),
        ("TG6", "Ground temperature 50 cm under surface", "°C", False),
        ("TG7", "Ground temperature 100 cm under surface", "°C", False),
        ("WD", "Wind direction", "°", False),
        ("WS", "Wind speed", "m/s", True),
        ("WDAVG2M", "Wind direction (2 minutes average)", "°", False),
        ("WDMAX2M", "Wind direction (2 minutes maximum)", "°", False),
        ("WDMIN2M", "Wind direction (2 minutes minimum)", "°", False),
        ("WSAVG2M", "Wind speed (2 minutes average)", "m/s", True),
        ("WSMAX2M", "Wind speed (2 minutes maximum)", "m/s", True),
        ("WSMIN2M", "Wind speed (2 minutes minimum)", "m/s", True),
        ("PAAVG1M", "Atmospheric pressure (1 minute average)", "hPa", True),
        ("EXTDC", "External DC voltage", "V", True),
        ("STATUS", "Unit status", "", None),
        ("DT", "Datetime", "", None),
        ("DT_BIN", "Datetime at set interval", "", None)
    ]

    CODES_INFO = {
        code: {"description": description, "unit": unit, "unit_space": unit_space}
        for code, description, unit, unit_space in __DATA
    }
    
    @staticmethod
    def get_unit_space_by_unit(unit):
        unit_space = [data["unit_space"] for data in MeteoConstants.CODES_INFO.values() if unit == data["unit"]]
        return True if unit_space[0] == True else False