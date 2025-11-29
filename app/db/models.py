from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(String, primary_key=True, index=True)
    code = Column(Text, default='')
