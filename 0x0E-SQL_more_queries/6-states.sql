-- Script that creates a database and a table
-- Query to create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_od_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.sates (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
