use jugos:

insert into tbproductos(
producto, nombre, envase, volumen, sabor,
 precio) values (
 '773912', 'clean', 'botella pet','1 litro','naranja',8.01);

select * from tbproductos;

insert into tabla_de_vendedores(
matricula, nombre, porcentaje_comision) values (
'00233', 'Joan Geraldo de la Fonseca', 10);

select * from tabla_de_vendedores;

insert into tabla_de_vendedores(
matricula, nombre, porcentaje_comision) values (
'00235', 'Márcio Almeida Silva', 8);
insert into tabla_de_vendedores(
matricula, nombre, porcentaje_comision) values (
'00236', 'Cláudia Morais', 8);

select * from tabla_de_vendedores;

update tabla_de_vendedores set porcentaje_comision = 11
where matricula = '00236';

update tabla_de_vendedores set nombre = 'Joan Geraldo de la Fonseca Junior'
where matricula = '00233';

select * from tabla_de_vendedores;

delete from tabla_de_vendedores where matricula = '00233';