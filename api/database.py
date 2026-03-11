import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(os.getenv("METEO_DATABASE_URL"))

LocalSession = sessionmaker(
    bind = engine
)

class Base(DeclarativeBase):
    pass

def get_database_session():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()