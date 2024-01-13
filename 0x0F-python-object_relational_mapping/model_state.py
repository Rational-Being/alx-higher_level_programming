#!/usr/bin/python3

from sqlalchemy import Column, Interger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State 

    Args:
        Base (_type_): _description_
    """    
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
