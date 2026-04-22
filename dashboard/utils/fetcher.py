import requests, os, json, ast, time
from websockets.sync.client import connect

class WebSocketConnector:
    def __init__(self):
        self.websocket_url = os.getenv("METEO_WEBSOCKET_URL")

    async def start_websocket_connection(self):
        with connect(self.websocket_url) as websocket:
            while True:
                measurements = websocket.recv()
                measurements = ast.literal_eval(measurements[1:-1])
                time.sleep(1)
                yield measurements

class StaticMeasurementsFetcher:
    def __init__(self, endpoint_name: str = None, start_date: str = None, end_date: str = None, interval: int = None):
        self.api_url = os.getenv("METEO_API_URL")
        self.measurements = self.__fetch_data_from_api(endpoint_name, start_date, end_date, interval)
        
    def __fetch_data_from_api(self, endpoint: str, start_date: str = None, end_date: str = None, interval: int = None):
        if endpoint == "latest":
            data = json.loads(requests.get(self.api_url + "/latest").text)
        elif endpoint == "average":
            if start_date and end_date and interval:
                average_url = f"/average?start={start_date}&end={end_date}&interval={interval}"
            else:
                average_url = "/average"
            data = json.loads(requests.get(self.api_url + average_url).text)
        elif endpoint == "range":
            data = json.loads(requests.get(self.api_url + f"/range?start={start_date}&end={end_date}").text)
        return data