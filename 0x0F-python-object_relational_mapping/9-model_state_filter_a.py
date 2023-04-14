#!/usr/bin/python3
"""
lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db_name), pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query database for all states containing "a"
    query = session.query(State).filter(State.name.like('%a%'))
    .order_by(State.id)

    # print results
    for state in query:
        print("{}: {}".format(state.id, state.name))

    # close session
    session.close()
