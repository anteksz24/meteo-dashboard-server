import os
from fastapi import FastAPI, status, Response, Depends
from database import get_database_session
from models import MeteoDataModel
from schemas import DataRequestSchema
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

app = FastAPI()

def extract_query_result(query_result):
    data_list = [row[0] for row in query_result]
    return data_list[0] if len(data_list) == 1 else data_list

@app.get("/latest/")
def get_latest_data(limit: int = 1, db: Session = Depends(get_database_session)):
    query = text('SELECT row_to_json(meteo_data) FROM meteo_data ORDER BY "DT" DESC LIMIT :limit')
    query_result = db.execute(query, {"limit": limit})
    measurements = extract_query_result(query_result)
    return measurements if measurements else Response(status_code = status.HTTP_404_NOT_FOUND)

@app.get("/range/")
def get_data_in_range(start: str, end: str, db: Session = Depends(get_database_session)):
    query = text('SELECT row_to_json(meteo_data) FROM meteo_data WHERE "DT" BETWEEN :start AND :end ORDER BY "DT" DESC')
    query_result = db.execute(query, {"start": start, "end": end})
    measurements = extract_query_result(query_result)
    return measurements if measurements else Response(status_code = status.HTTP_404_NOT_FOUND)

@app.post("/post/")
def post_data(received_data: DataRequestSchema, db: Session = Depends(get_database_session)):
    if received_data.password == os.getenv("METEO_PASSWORD"):
        meteo_entry = MeteoDataModel(**received_data.content.model_dump())
        db.add(meteo_entry)
        db.commit()
        db.refresh(meteo_entry)
        return Response(status_code = status.HTTP_200_OK)
    else:
        return Response(status_code = status.HTTP_401_UNAUTHORIZED)