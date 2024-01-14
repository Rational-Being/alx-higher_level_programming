#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
form sqlalchemy import (create_engine)
import sys

if __name__ == '__main__':
    engine = create_Engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv [3]))
    
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    for state in session.query(State).order_by(State.id):
        print('{}:{}'.format(state.id, state.name))