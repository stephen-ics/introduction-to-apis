from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

# Connecting db using raw sql instead of sqlalchemy
# try:
#    conn = psycopg.connect("dbname=apis user=postgres password=password123")
#    cursor = conn.cursor()
#    print('Connected to database!')
# except Exception as error:
#    print('Connecting to database failed')
#    print('Error', error)
