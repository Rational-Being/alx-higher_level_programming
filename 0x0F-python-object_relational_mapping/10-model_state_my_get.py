#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import Base, State

if __name__ = '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).filter(State.name == state.name).order_by(State.id)
    
    if state in not None:
        for state in states:
            print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")