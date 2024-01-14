#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ = '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State.name, City.id, City.name).join(City, City.state_id == State.id).order_by(City.id)
    
    for state in states:
        print("{}: ({}) {}".format(state[0], state[1], state[2]))