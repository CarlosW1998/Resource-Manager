from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import true
from config.database import Base

class Resource(Base):
    __tablename__="resource"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=True, unique=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique=False)
    password = Column(String(256), nullable=True, unique=False)
    email = Column(String(150), nullable=False, unique=True)
    role = Column(String(150), nullable=True, unique=False)