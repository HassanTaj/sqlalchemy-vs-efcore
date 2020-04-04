from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
Base = declarative_base()

class Todos(Base):
    __tablename__ = 'Todos'
    id = Column(UNIQUEIDENTIFIER, primary_key=True)
    task = Column(String, unique=False, nullable=True, primary_key=False)
    description = Column(String, unique=False, nullable=True, primary_key=False)
    endDate = Column(String, unique=False, nullable=True, primary_key=False)