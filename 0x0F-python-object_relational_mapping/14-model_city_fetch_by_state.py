#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    """Prints all City objects from the database hbtn_0e_14_usa."""

    # Set up connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all cities, sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print results in format: "<state name>: (<city id>) <city name>"
    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # Close the session
    session.close()
