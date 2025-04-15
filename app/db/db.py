from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url, echo=True, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()
