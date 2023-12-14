-- cretes table

CREATE DATABASE IF NOT EXITS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities ON hbtn_0d_usa(
	id INT AUTO-GENERATED UNIQUE NOT NULL PRIMARY KEY,
	state_id NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.state(id));
