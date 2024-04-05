SELECT 
    b.dpt_name,
    COUNT(a.emp_dept)
FROM emp_details AS a
JOIN emp_department AS b ON a.emp_dept = b.dpt_code
GROUP BY b.dpt_name
HAVING COUNT(a.emp_dept)>2
ORDER BY COUNT(a.emp_dept) DESC;


CREATE TABLE emp_department(
    dpt_code int,
    dpt_name varchar,
    dpt_allotment int
);

CREATE TABLE emp_details(
    emp_id int,
    emp_fname varchar,
    emp_lname varchar,
    emp_dept int
);

INSERT INTO emp_department VALUES
(57,'IT',65000),
(63,'Finance',15000),
(47,'HR',240000),
(27,'RD',55000),
(89,'QC',75000);

INSERT INTO emp_details VALUES
(127323,'Michael','Robbin',57),
(526689,'Carlos','Snares',63),
(843795,'Enric','Dosio',57),
(328717,'Jon','Snares',63),
(444527,'Joseph','Dosni',47),
(659831,'Zanifer','Emily',47),
(123456,'Kuleswar','Sitaraman',57),
(765432,'Azizbek','Ziyodullayev',47);