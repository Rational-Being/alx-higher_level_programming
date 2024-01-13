#!/usr/bin/python3

from sqlalchemy import Column, Interger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State 

    Args:
        Base (class): sqlalchemy
    """     
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=F)
