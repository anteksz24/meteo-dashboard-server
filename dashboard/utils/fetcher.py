import requests, os, json

class Fetcher:
    def __init__(self):
        self.api_url = os.getenv("METEO_API_URL")
        
    def fetch_data_from_api(self, endpoint: str, start_date: str = None, end_date: str = None, interval: int = None):
        if endpoint == "latest":
            data = json.loads(requests.get(self.api_url + "/latest/").text)
        elif endpoint == "average":
            if start_date and end_date and interval:
                average_url = f"/average/?start={start_date}&end={end_date}&interval={interval}"
            else:
                average_url = "/average/"
            data = json.loads(requests.get(self.api_url + average_url).text)
        elif endpoint == "range":
            data = json.loads(requests.get(self.api_url + f"/range/?start={start_date}&end={end_date}").text)
        return data