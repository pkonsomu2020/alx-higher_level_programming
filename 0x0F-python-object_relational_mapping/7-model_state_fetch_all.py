#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    # create connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                           sys.argv[3]))

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    # query database
    State = session.query(State).order_by(State.id)

    # print results
    print(states)
    for state in State:
        print("{}: {}".format(state.id, state.name))

    # close session
    session.close()
