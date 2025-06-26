-- script that prints description of table
CREATE DATABASE IF NOT EXISTS hbtn_test_db_5;
USE hbtn_test_db_5;

SHOW CREATE TABLE first_table (
    id INT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);