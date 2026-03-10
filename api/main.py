import os
from fastapi import FastAPI, status, Response
from pydantic import BaseModel

app = FastAPI()
app.state.stored_data = None

class WeatherData(BaseModel):
    content: dict
    password: str

@app.post("/send/")
def send_data(received_data: WeatherData):
    if received_data.password == os.getenv("METEO_PASSWORD"):
        app.state.stored_data = received_data.content
        return Response(status_code = status.HTTP_200_OK)
    else:
        return Response(status_code = status.HTTP_401_UNAUTHORIZED)

@app.get("/")
def view_data():
    if app.state.stored_data is None:
        return Response(status_code = status.HTTP_404_NOT_FOUND)
    return app.state.stored_data