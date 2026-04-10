from utils.fetcher import Fetcher
from datetime import datetime, timezone, timedelta

fetcher = Fetcher()

class LatestMeasurements:
    def __init__(self, latest_measurements_outdated, latest_datetime):
        self.latest_measurements_outdated = latest_measurements_outdated
        self.latest_datetime = str(latest_datetime)[:-6]

class AverageMeasurements:
    def __init__(self, average_measurements_incomplete, average_list_length):
        self.average_measurements_incomplete = average_measurements_incomplete
        self.average_list_length = average_list_length

class Warnings:
    def __init__(self):
        self.latest = self.__check_latest()
        self.average = self.__check_average()
    
    def __str__(self):
        print(self.latest.latest_datetime)
        return f"""
            **There are warnings available for the system!**\n
            {"Latest data is outdated. Last data update was "
                f"{self.latest.latest_datetime} of UTC time."
            if self.latest.latest_measurements_outdated else ""}\n
            {"Average charts are incorrect and incomplete. There are "
                f"{self.average.average_list_length} rows in average data API response out of 25 needed."
            if self.average.average_measurements_incomplete else ""}
        """
    
    def check_available_warnings(self):
        return True if self.latest or self.average else False
    
    def __check_latest(self):
        latest_data = fetcher.fetch_data_from_api("latest")
        latest_timestamp = datetime.fromisoformat(latest_data[0]["datetime"]).replace(tzinfo = timezone.utc)
        if latest_timestamp < datetime.now(timezone.utc) - timedelta(hours = 1):
            return LatestMeasurements(True, latest_timestamp)
        else:
            return LatestMeasurements(False, latest_timestamp)
    
    def __check_average(self):
        average_data = fetcher.fetch_data_from_api("average")
        if len(average_data) < 25:
            return AverageMeasurements(True, len(average_data))
        else:
            return AverageMeasurements(False, len(average_data))