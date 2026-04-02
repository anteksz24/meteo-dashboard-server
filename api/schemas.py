from pydantic import BaseModel

class DataRequestSchema(BaseModel):
    content: MeteoDataSchema
    password: str

class MeteoDataSchema(BaseModel):
    TAAVG1M: float
    RHAVG1M: float
    DPAVG1M: float
    PRSUM1H: float
    SRAVG1M: float
    SDUR1M: float
    SRDSUM1D: float
    TAMIN1D: float
    TAMAX1D: float
    RHMIN1D: float
    RHMAX1D: float
    TG1: float
    TG2: float
    TG3: float
    TG4: float
    TG5: float
    TG6: float
    TG7: float
    WD: float
    WS: float
    WDAVG2M: float
    WDMAX2M: float
    WDMIN2M: float
    WSAVG2M: float
    WSMAX2M: float
    WSMIN2M: float
    PAAVG1M: float
    DT: str