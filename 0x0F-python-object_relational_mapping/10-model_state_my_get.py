#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query database for state with name matching the argument
    query = session.query(State).filter(name=sys.argv[4]).first()

    # print result or "Not found"
    result = query.first()
    if result is not None:
        print("{}".format(result.id))
    else:
        print("Not found")

    # close session
    session.close()
