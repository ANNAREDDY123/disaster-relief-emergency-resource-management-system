CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR(100),
email VARCHAR(100) UNIQUE,
password VARCHAR(255),
role VARCHAR(30)
);

CREATE TABLE camps(
id INTEGER PRIMARY KEY AUTOINCREMENT,
camp_name VARCHAR(100),
location VARCHAR(150),
district VARCHAR(100),
capacity INTEGER,
available_capacity INTEGER,
status VARCHAR(20)
);

CREATE TABLE victims(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100),
age INTEGER,
gender VARCHAR(20),
contact_number VARCHAR(15),
family_members INTEGER,
camp_id INTEGER,
FOREIGN KEY(camp_id) REFERENCES camps(id)
);

CREATE TABLE resources(
id INTEGER PRIMARY KEY AUTOINCREMENT,
camp_id INTEGER,
resource_type VARCHAR(100),
quantity INTEGER,
distributed_by VARCHAR(100),
distribution_date DATE,
FOREIGN KEY(camp_id) REFERENCES camps(id)
);

CREATE TABLE volunteers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100),
email VARCHAR(100) UNIQUE,
phone VARCHAR(15),
assigned_camp INTEGER,
availability_status BOOLEAN,
FOREIGN KEY(assigned_camp) REFERENCES camps(id)
);
