-- Script that lists all the cities of california registered in the database
-- Query to list all the cities from california
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "california");
