create database holamundo;
show databases;
use holamundo;
create	table animales(
	id int,
    tipo varchar(255),
    estado varchar(255),
    primary key(id)
    
);
-- insert into animales (tipo,estado) values ('chanchito','feliz');
-- esta linea no sera ejecutada

alter table animales modify column id int auto_increment;

show create table animales;

CREATE TABLE `animales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

insert into animales (tipo,estado) values ('chanchito','feliz');
insert into animales (tipo,estado) values ('dragon','feliz');
insert into animales (tipo,estado) values ('felipe','triste');

select * from ANIMALES;
select * from ANIMALES where id =1;
select * from ANIMALES where estado ='feliz' and tipo = 'dragon';

update animales set estado = 'feliz' where id = 4;
select * from ANIMALES;

