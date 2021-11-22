from sqlalchemy import Column, Integer, String
from config.database import Base

class Resource(Base):
    __tablename__="resource"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=True, unique=False)