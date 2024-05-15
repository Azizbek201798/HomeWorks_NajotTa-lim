-- Task - 1 => DONE by Azizbek

CREATE DATABASE milliy_taomlar;

CREATE TABLE ovqat(id INT AUTO_INCREMENT PRIMARY KEY,taom_nomi VARCHAR(20),taom_masalliqlari VARCHAR(50));

INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Mastava","Yog,guruch,gosht,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Shashlik","Piyoz,uksus,gosht,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Tandir kabob","Yog,gosht,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Shorva","Yog,piyoz,kartoshka,guruch,gosht,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Biqtirma","Yog,kartoshka,gosht");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Chalop","Qatiq,guruch,loviya,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Manti","Un,gosht,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Xonim","Kartoshka,un,gosht,piyoz,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Donar","Yog,un,gosht,suv");
INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES ("Mastava","Yog,guruch,gosht,suv");

-- Task - 1;
SELECT * FROM ovqat WHERE taom_nomi LIKE '%a';

-- Task - 2;
SELECT * FROM ovqat WHERE taom_masalliqlari LIKE '%guruch%';
