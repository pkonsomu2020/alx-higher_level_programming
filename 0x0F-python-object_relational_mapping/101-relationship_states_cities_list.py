#!/usr/bin/python3
"""Lists all State objects, and
corresponding City objects, contained
in the database hbtn_0e_101_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    # Get MySQL credentials from command line arguments
    # Start engine to interact with MySQL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State and City tables, and join them
    data = session.query(State, City).filter(State.id == City.state_id)\
                                     .order_by(State.id, City.id).all()

    # Print results
    for state, city in data:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # Close the session
    session.close()
