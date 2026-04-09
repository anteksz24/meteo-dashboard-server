from datetime import datetime
from dataclasses import dataclass

@dataclass
class ChartConfig:
    parameters: list[str]
    start_date: datetime
    end_date: datetime
    average: bool = True
    interval: int = 5
    y_axis_zero: bool = False