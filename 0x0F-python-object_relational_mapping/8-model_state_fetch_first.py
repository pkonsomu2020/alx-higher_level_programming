#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # create connection
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],))

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query database for first state
    states = session.query(State).order_by(State.id).first()

    # print result or "Nothing" if table is empty
    print("{}: {}".format(state.id, state.name))

    # close session
    session.close()
