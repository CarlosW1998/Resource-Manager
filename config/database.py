from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNECTION')

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

seasson_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
