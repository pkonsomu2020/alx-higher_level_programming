#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Create connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new State to the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)
