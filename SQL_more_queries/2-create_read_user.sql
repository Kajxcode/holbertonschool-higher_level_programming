-- script that creates a new user with select privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';