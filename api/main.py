import os
from fastapi import FastAPI, status, Response, Depends
from database import get_database_session
from models import MeteoDataModel
from schemas import DataRequestSchema
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

app = FastAPI()

@app.get("/")
def get_data(db: Session = Depends(get_database_session)):
    try:
        result = db.execute(text('SELECT row_to_json(meteo_data) FROM meteo_data ORDER BY "ID" DESC LIMIT 1'))
        row = result.fetchone()
        return row[0] if row else Response(status_code = status.HTTP_404_NOT_FOUND)
    except:
        return Response(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.post("/post/")
def post_data(received_data: DataRequestSchema, db: Session = Depends(get_database_session)):
    if received_data.password == os.getenv("METEO_PASSWORD"):
        meteo_dict = received_data.content.model_dump()
        meteo_entry = MeteoDataModel(**meteo_dict)
        db.add(meteo_entry)
        db.commit()
        db.refresh(meteo_entry)
        return Response(status_code = status.HTTP_200_OK)
    else:
        return Response(status_code = status.HTTP_401_UNAUTHORIZED)