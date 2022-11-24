use holamundo;
CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

insert into user (name, edad, email) values ('Oscar',25,'oscar@gmail.com');
insert into user (name, edad, email) values ('Layla',15,'layla@gmail.com');
insert into user (name, edad, email) values ('Nicolas',36,'nico@gmail.com');
insert into user (name, edad, email) values ('Chanchito',7,'chanchito@gmail.com');

SELECT 
    *
FROM
    user;
SELECT 
    *
FROM
    user
LIMIT 1;
SELECT 
    *
FROM
    user
WHERE
    edad > 15;
SELECT 
    *
FROM
    user
WHERE
    edad >= 15;
SELECT 
    *
FROM
    user
WHERE
    edad > 20 AND email = 'nico@gmail.com';
SELECT 
    *
FROM
    user
WHERE
    edad > 20 OR email = 'layla@gmail.com';
SELECT 
    *
FROM
    user
WHERE
    edad BETWEEN 15 AND 30;
-- busqueda que contenga un string
SELECT 
    *
FROM
    user
WHERE
    email LIKE '%gmail%';
-- busqueda cuyo string termine con gmail (lleva un solo %)
SELECT 
    *
FROM
    user
WHERE
    email LIKE '%gmail';
select
	*
from
	user
order by
	edad asc;
select
	*
from
	user
order by
	edad desc;	

select max(edad) as mayor from user;
select min(edad) as menor from user;

-- seleccionar columnas
select id, name from user;

-- ponerle Alias a las columnas con as...
select id as DNI, name as nombre from user;









