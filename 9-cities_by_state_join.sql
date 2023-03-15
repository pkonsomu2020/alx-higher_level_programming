-- Script that lists all the cities contained in the database
-- Query to join cities and states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.states_id = states_id;
