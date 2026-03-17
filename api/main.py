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

@app.get("/average/")
def get_average_data(db: Session = Depends(get_database_session)):
    query = text("""
        SELECT
            row_to_json(t)
        FROM (
            SELECT
                EXTRACT(HOUR FROM "DT") AS "HOUR",
                ROUND(AVG("TAAVG1M")::NUMERIC, 1) AS "AVG_TAAVG1M",
                ROUND(AVG("RHAVG1M")::NUMERIC, 0) AS "AVG_RHAVG1M",
                ROUND(AVG("DPAVG1M")::NUMERIC, 1) AS "AVG_DPAVG1M",
                ROUND(AVG("SRAVG1M")::NUMERIC, 0) AS "AVG_SRAVG1M",
                ROUND(AVG("SDUR1M")::NUMERIC, 0) AS "AVG_SDUR1M",
                ROUND(AVG("SRDSUM1D")::NUMERIC, 0) AS "AVG_SRDSUM1D",
                ROUND(AVG("TAMIN1D")::NUMERIC, 1) AS "AVG_TAMIN1D",
                ROUND(AVG("TAMAX1D")::NUMERIC, 1) AS "AVG_TAMAX1D",
                ROUND(AVG("RHMIN1D")::NUMERIC, 0) AS "AVG_RHMIN1D",
                ROUND(AVG("RHMAX1D")::NUMERIC, 0) AS "AVG_RHMAX1D",
                ROUND(AVG("TG1")::NUMERIC, 1) AS "AVG_TG1",
                ROUND(AVG("TG2")::NUMERIC, 1) AS "AVG_TG2",
                ROUND(AVG("TG3")::NUMERIC, 1) AS "AVG_TG3",
                ROUND(AVG("TG4")::NUMERIC, 1) AS "AVG_TG4",
                ROUND(AVG("TG5")::NUMERIC, 1) AS "AVG_TG5",
                ROUND(AVG("TG6")::NUMERIC, 1) AS "AVG_TG6",
                ROUND(AVG("TG7")::NUMERIC, 1) AS "AVG_TG7",
                ROUND(AVG("WD")::NUMERIC, 0) AS "AVG_WD",
                ROUND(AVG("WS")::NUMERIC, 1) AS "AVG_WS",
                ROUND(AVG("WDAVG2M")::NUMERIC, 0) AS "AVG_WDAVG2M",
                ROUND(AVG("WDMAX2M")::NUMERIC, 0) AS "AVG_WDMAX2M",
                ROUND(AVG("WDMIN2M")::NUMERIC, 0) AS "AVG_WDMIN2M",
                ROUND(AVG("WSAVG2M")::NUMERIC, 1) AS "AVG_WSAVG2M",
                ROUND(AVG("WSMAX2M")::NUMERIC, 1) AS "AVG_WSMAX2M",
                ROUND(AVG("WSMIN2M")::NUMERIC, 1) AS "AVG_WSMIN2M",
                ROUND(AVG("PAAVG1M")::NUMERIC, 1) AS "AVG_PAAVG1M"
            FROM
                meteo_data
            WHERE
                "DT" >= NOW() - INTERVAL '24 hours'
            GROUP BY
                EXTRACT(HOUR FROM "DT")
            ORDER BY
                "HOUR"
        ) t;
    """)
    query_result = db.execute(query)
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