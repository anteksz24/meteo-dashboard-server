from datetime import datetime
from dataclasses import dataclass

@dataclass
class ChartConfig:
    parameters: list[str]
    start_date: datetime
    end_date: datetime
    chart_type: str
    y_axis_zero: bool = False
    average: bool = True
    interval: int = 5