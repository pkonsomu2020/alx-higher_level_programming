#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create engine. Args are provided via script input.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session factory bound to engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all states with a name containing 'a'
    states = session.query(State).filter(State.name.like('%a%'))

    # Delete all states with a name containing 'a'
    for state in states:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close session
    session.close()
