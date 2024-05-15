-- Task - 2 => DONE by Azizbek

CREATE DATABASE bozor;

CREATE TABLE meva(id INT AUTO_INCREMENT PRIMARY KEY, meva_nomi VARCHAR(20), meva_narxi INT, meva_turi VARCHAR(20));

INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olma",25000,"Termez");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Banan",23000,"Andjan");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Shaptoli",52000,"Termez");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olma",25000,"Termez");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Gilos",12000,"Narpay");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Qovun",37000,"Forish");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Tarvuz",14000,"Denov");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Qulupnay",45000,"Bo'ka");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olxori",5000,"Toshkent");
INSERT INTO meva(meva_nomi, meva_narxi, meva_turi) VALUES ("Olma",25000,"Termez");

-- Task - 1;
CREATE TABLE temp_meva AS
SELECT MAX(id) AS max_id
FROM meva
GROUP BY meva_nomi, meva_narxi, meva_turi;

DELETE FROM meva
WHERE id NOT IN (
    SELECT max_id
    FROM temp_meva
);

DROP TABLE temp_meva;

-- Task - 2;
SELECT * FROM meva ORDER BY meva_narxi DESC LIMIT 5;

-- Additional
SELECT MAX(id) FROM meva GROUP BY meva_nomi,meva_narxi,meva_turi;

DELETE FROM meva
WHERE id NOT IN (
    SELECT MAX(id) 
    FROM meva 
    GROUP BY meva_nomi,meva_turi,meva_narxi
);

DROP TABLE meva;
