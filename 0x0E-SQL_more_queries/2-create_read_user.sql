-- Script that creates a user and a database in mySQL server
-- Query to create the user 'user_0d_1' and database 'hbtn_0d_2' in MySQL server
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user 'user_0d_2'@'localhost';
