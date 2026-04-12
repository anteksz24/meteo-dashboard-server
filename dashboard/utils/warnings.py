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
        self.average_list_length_shortage = 25 - average_list_length

class Warnings:
    def __init__(self):
        self.latest = self.__check_latest()
        self.average = self.__check_average()
    
    def __str__(self):
        return f"""
            **System warning**\n
            {"Latest data is outdated. It was last updated over an hour ago ("
                f"{self.latest.latest_datetime})."
            if self.latest.latest_measurements_outdated else ""}\n
            {"Charts displayed on the Overview page are incomplete. They should display data from last 24 hours and "
                "consist of 25 points. However, "
                f"{self.average.average_list_length_shortage} data points are currently missing."
            if self.average.average_measurements_incomplete else ""}
        """
    
    def check_available_warnings(self):
        return True if self.latest.latest_measurements_outdated or self.average.average_measurements_incomplete else False
    
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