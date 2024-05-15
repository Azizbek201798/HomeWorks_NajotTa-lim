CREATE DATABASE avtosalon;

CREATE TABLE mashinalar(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(15),price INT,capacity FLOAT,color TEXT, warranty int);

INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Ferrari",35000,2.1,"Red",3);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Tahoe",22000,2.2,"White",4);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Onix",12000,2.3,"Blue",5);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Damas",9000,2.4,"Red",3);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Jiguli",75000,2.5,"Red",4);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Nexia 2",15000,2.6,"White",5);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Cobalt",11000,2.7,"Black",3);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Tico",31000,2.8,"Yellow",4);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Matiz",65000,2.9,"Red",5);
INSERT INTO mashinalar(name,price,capacity,color,warranty) VALUES ("Traverse",21000,2.1,"Black",3);

-- Task - 4;
UPDATE mashinalar set price = price + 3000 WHERE price > 10000 and price <= 20000; 

-- Task - 5;
UPDATE mashinalar set capacity = 1 WHERE warranty = 5;

-- Task - 6;
ALTER TABLE mashinalar ADD column quality TEXT;

-- Task - 7;
UPDATE mashinalar SET quality = "Premium" WHERE price = (SELECT MAX(price) FROM mashinalar);

-- Task - 8;
UPDATE mashinalar SET quality = "Low qualality" WHERE price = (SELECT MIN(price) FROM mashinalar);

-- Task - 9;
ALTER TABLE mashinalar CHANGE quality quality TEXT AFTER name;

-- Task - 10;
ALTER TABLE mashinalar CHANGE name ism VARCHAR(15);
ALTER TABLE mashinalar CHANGE price narx INT;
ALTER TABLE mashinalar CHANGE capacity hajm INT;
ALTER TABLE mashinalar CHANGE color rang FLOAT;
ALTER TABLE mashinalar CHANGE warranty garantiya INT;
ALTER TABLE mashinalar CHANGE quality sifat TEXT;