#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from model_State import Base

class City(Base):
    
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)