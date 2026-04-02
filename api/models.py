from sqlalchemy import Column, Integer, Float, TIMESTAMP
from database import Base

class MeteoDataModel(Base):
    __tablename__ = "meteo_data"

    ID = Column("id", Integer, primary_key = True, index = True)
    TAAVG1M = Column("air_temp_avg_1m", Float)
    RHAVG1M = Column("humidity_avg_1m", Float)
    DPAVG1M = Column("dewpoint_avg_1m", Float)
    PRSUM1H = Column("precipitation_sum_1h", Float)
    SRAVG1M = Column("solar_rad_avg_1m", Float)
    SDUR1M = Column("sunshine_dur_1m", Float)
    SRDSUM1D = Column("sunshine_dur_sum_1d", Float)
    TAMIN1D = Column("air_temp_min_1d", Float)
    TAMAX1D = Column("air_temp_max_1d", Float)
    RHMIN1D = Column("humidity_min_1d", Float)
    RHMAX1D = Column("humidity_max_1d", Float)
    TG1 = Column("air_temp_5cm_above_ground_avg_1m", Float)
    TG2 = Column("air_temp_surface_avg_1m", Float)
    TG3 = Column("ground_temp_5cm_avg_1m", Float)
    TG4 = Column("ground_temp_10cm_avg_1m", Float)
    TG5 = Column("ground_temp_20cm_avg_1m", Float)
    TG6 = Column("ground_temp_50cm_avg_1m", Float)
    TG7 = Column("ground_temp_100cm_avg_1m", Float)
    WD = Column("wind_direction_inst", Float)
    WS = Column("wind_speed_inst", Float)
    WDAVG2M = Column("wind_direction_avg_2m", Float)
    WDMAX2M = Column("wind_direction_max_2m", Float)
    WDMIN2M = Column("wind_direction_min_2m", Float)
    WSAVG2M = Column("wind_speed_avg_2m", Float)
    WSMAX2M = Column("wind_speed_max_2m", Float)
    WSMIN2M = Column("wind_speed_min_2m", Float)
    PAAVG1M = Column("pressure_avg_1m", Float)
    PAAVG1M_ADJ = Column("pressure_adj_avg_1m", Float)
    DT = Column("datetime", TIMESTAMP)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.PAAVG1M_ADJ = round(self.PAAVG1M + 11.4, 2)