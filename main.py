import os
from fastapi import FastAPI
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
        return {"Status": "Data sent successfully"}
    else:
        return {"Error": "Invalid password"}

@app.get("/")
def view_data():
    if app.state.stored_data is None:
        return {"Error": "No data"}
    return app.state.stored_data