-- Task - 4 => DONE by Azizbek

CREATE TABLE meva(id INT AUTO_INCREMENT PRIMARY KEY, meva_nomi VARCHAR(20), meva_narxi INT, meva_turi VARCHAR(20));

INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olma",25000,"Termez");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Banan",23000,"Andjan");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Shaptoli",52000,"Termez");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olma",25000,"Termez");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Gilos",12000,"Narpay");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Qovun",37000,"Forish");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Tarvuz",74000,"Denov");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Qulupnay",45000,"Bo'ka");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olxori",5000,"Toshkent");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olma",25000,"Termez");

-- Task - 1;
SELECT * FROM meva WHERE meva_narxi BETWEEN 10000 AND 50000 ORDER BY meva_narxi DESC;

-- Task - 2;
SELECT m1.*
FROM meva AS m1
JOIN meva AS m2 ON LENGTH(m1.meva_nomi) = LENGTH(m2.meva_nomi) AND m1.id != m2.id
ORDER BY m1.meva_narxi DESC;