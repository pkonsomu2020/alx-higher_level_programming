#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == '__main__':
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured "Session" class.
    Session = sessionmaker(bind=engine)

    # Create a Session instance.
    session = Session()

    # Query the City objects, joined with their corresponding State objects.
    cities = session.query(City).join(State).order_by(City.id).all()

    # Loop through the query results and print them in the required format.
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))

    # Close the session.
    session.close()
