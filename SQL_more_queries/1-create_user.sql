-- script that creates a user with grants
CREATE USER 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1@localhost'