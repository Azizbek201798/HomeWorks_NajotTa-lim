CREATE DATABASE IF NOT EXISTS Users;
show databases; show tables;
CREATE TABLE IF NOT EXISTS client(client_id int, name varchar(10), age int, gender varchar(10));
DESCRIBE table_name;
INSERT INTO client(clint_id,name,age,gender) VALUES (1,"Azizbek",25,"Men");
SELECT * FROM client WHERE gender =  "Men";
SELECT * FROM client WHERE age > 25 AND age <= 40; 
CREATE TABLE IF NOT EXISTS subject(id INT PRIMARY KEY AVTO_INCREMENT,name VARCHAR(50) NOT NULL, teacher_name VARCHAR(20) DEFAULT "Azizbek");
UPDATE subject SET name = "Kamola" WHERE id = 1;