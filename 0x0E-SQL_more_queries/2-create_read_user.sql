-- script creates databse user and grant all privelegs

-- create databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- gratnt priveleges
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
