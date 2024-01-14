#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ = '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = session.query(State).filter(state.id == 2).one()
    new_state.update({"name": ("New Mexico")})

    session.commit()
    
    print(new.state.id)