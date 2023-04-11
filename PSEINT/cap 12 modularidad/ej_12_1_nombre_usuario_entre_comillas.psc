Proceso nombre_usuario_entre_comillas
	//Diseñar un algoritmo que pida un nombre al usuario 
	//y que despliegue en pantalla el nombre entre asteriscos. 
	//La cantidad de asteriscos debe ser la misma que caracteres 
	//en el nombre incluido espacios. 
	
	//defino variables
	Definir nombreusuario,aster Como Caracter;
	Definir long,i Como Entero;
	Dimension aster[100];
	//ingresa nombre de usuario
Escribir "Ingrese el nombre de usuario";
Leer nombreusuario;
	//calcula longitud del nombre de usuario
long<-Longitud(nombreusuario);
// crea un arreglo con tantos asteriscos como tenga de longitud el nombreusuario
para i<-0 Hasta long-1 Hacer
	aster[i]<-"*";
FinPara//muestra el arreglo de asteriscos+nombreusuario+arreglo asteriscos
para i<-0 Hasta long-1 Hacer
	Escribir Sin Saltar aster[i];
FinPara
Escribir Sin Saltar nombreusuario;
para i<-0 Hasta long-1 Hacer
	Escribir Sin Saltar aster[i];
FinPara
Escribir "";
FinProceso
