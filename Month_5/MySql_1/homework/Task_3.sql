-- Task - 3 => DONE by Azizbek

CREATE TABLE airplane(id INT AUTO_INCREMENT PRIMARY KEY, samalyot_turi VARCHAR(17),uchish_sanasi VARCHAR(20),town_from VARCHAR(30),town_to VARCHAR(30),uchish_vaqti VARCHAR(30));

INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING 707","21.04.2024","Toshkent","Dubai","22:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING 747","22.04.2024","Termez","Toshkent","16:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("AIRBUS A380","12.03.2024","Toshkent","Samarqand","09:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("Cesna 372","02.02.2024","Toshkent","Termez","01:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("F-35","06.09.2024","Toshkent","Barselona","23:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING AH-64","22.02.2024","Madrid","Dubai","21:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING 707","12.06.2024","Toshkent","Paris","17:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING 747","02.11.2024","Toshkent","Samarqand","15:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING B-555","14.04.2024","Madrid","Toshkent","14:30");
INSERT INTO airplane(samalyot_turi,uchish_sanasi,town_from,town_to,uchish_vaqti) VALUES ("BOEING AK-47","13.02.2024","Termez","Dubai","11:30");

-- Task - 1;
SELECT * FROM airplane WHERE uchish_sanasi LIKE '___03%' OR uchish_sanasi LIKE '___04%' OR uchish_sanasi LIKE '___05%';

-- Task - 2;
SELECT * FROM airplane WHERE (TIME(uchish_vaqti) BETWEEN '14:00' AND '18:00') AND town_to = 'Toshkent';