import os
from fastapi import FastAPI, status, Response, Depends, WebSocket
from database import get_database_session
from models import MeteoDataModel
from schemas import DataRequestSchema
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from datetime import datetime, timedelta, timezone

app = FastAPI()

def calculate_reduced_pressure(pressure):
    return round(pressure + float(os.getenv("METEO_PRESSURE_CORRECTION")), 2)

class Query:
    def get_query(self, filename):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"./queries/{filename}"), "r") as query:
            return text(query.read())

    def extract_query_result(self, query_result):
        data_list = [row[0] for row in query_result]
        return data_list

query = Query()

class WebSocketConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
        self.latest_data = None
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        
    async def broadcast(self, data: list):
        self.latest_data = data
        for connection in self.active_connections:
            await connection.send_json(data)
            
manager = WebSocketConnectionManager()

@app.get("/latest")
def get_latest_data(limit: int = 1, db: Session = Depends(get_database_session)):
    query_result = db.execute(query.get_query("latest.sql"), {"limit": limit})
    measurements = query.extract_query_result(query_result)
    return measurements

@app.get("/range")
def get_data_in_range(start: str, end: str, db: Session = Depends(get_database_session)):
    query_result = db.execute(query.get_query("range.sql"), {"start": start, "end": end})
    measurements = query.extract_query_result(query_result)
    return measurements

@app.get("/average")
def get_average_data(interval: int = 60, start: datetime = None, end: datetime = None, db: Session = Depends(get_database_session)):
    if not start:
        start = datetime.now().astimezone(timezone.utc) - timedelta(days = 1, hours = 1)
    if not end:
        end = datetime.now().astimezone(timezone.utc) - timedelta(hours = 1)
    query_result = db.execute(query.get_query("average.sql"), {"interval": interval, "start": start, "end": end})
    measurements = query.extract_query_result(query_result)
    return measurements

@app.post("/send")
async def post_data(received_data: DataRequestSchema, db: Session = Depends(get_database_session)):
    if received_data.password == os.getenv("METEO_PASSWORD"):
        meteo_entry = MeteoDataModel(**received_data.content.model_dump())
        meteo_entry.PAAVG1M_ADJ = calculate_reduced_pressure(meteo_entry.PAAVG1M)
        
        db.add(meteo_entry)
        db.commit()
        db.refresh(meteo_entry)
        
        latest_query_result = db.execute(query.get_query("latest.sql"), {"limit": 1})
        extracted_latest_measurements = query.extract_query_result(latest_query_result)
        await manager.broadcast(extracted_latest_measurements)
        return Response(status_code = status.HTTP_201_CREATED)
    else:
        return Response(status_code = status.HTTP_401_UNAUTHORIZED)

@app.websocket("/websocket")
async def websocket_connection(websocket: WebSocket, db: Session = Depends(get_database_session)):
    await manager.connect(websocket)
    latest_query_result = db.execute(query.get_query("latest.sql"), {"limit": 1})
    extracted_latest_measurements = query.extract_query_result(latest_query_result)
    await manager.broadcast(extracted_latest_measurements)
    try:
        while True:
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)