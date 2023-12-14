-- script creates user and grant all privelegs

-- create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- gratnt priveleges

GRANT PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
