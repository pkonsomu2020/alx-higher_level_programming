#!/usr/bin/python3
"""
Adds the State object “California” with the City
“San Francisco” to the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Initializes connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Creates a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creates a new State and a new City
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    # Adds the new State and City to the session
    session.add(new_state)
    session.add(new_city)

    # Commits the session and closes it
    session.commit()
    session.close()
