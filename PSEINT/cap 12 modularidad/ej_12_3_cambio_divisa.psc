//Desarrollar un programa que pueda calcular el valor 
//del tipo de cambio de moneda (de tu moneda hacia d�lar y viceversa). 

//SubProceso cambio a dolar
SubProceso cambiodolar<-convertiradolar(cambiohoy,cantidad)
	Definir dolar Como Real;
	dolar<-cantidad/cambiohoy;
	Escribir dolar;
FinSubProceso
//SubProceso cambio a pesos	
SubProceso cambiopesos<-convertirapesos(cambiohoy,cantidad)
	Definir pesos Como Real;
	pesos<-cantidad*cambiohoy;
	Escribir pesos;
FinSubProceso
//men� de opciones para convertir la moneda dolar->pesos y viceversa
Proceso cambio_divisa
	//defino variables
	Definir cambio, tipomoneda,pesoadolar,dolarapeso Como Real;
	Escribir Sin Saltar"Ingrese el valor del dolar hoy: ";
	leer cambio;
	//Muestro men� opciones
	Escribir "ingrese el tipo de moneda que quiere convertir: ";
	Escribir "1<- pesos";
	Escribir "2<- d�lares";
	Leer tipomoneda;
	Segun tipomoneda Hacer
		1:
			Escribir "Ingrese la cantidad de pesos a convertir a d�lares";
			Leer pesoadolar;
			Escribir "	La equivalencia en d�lares es:";
			//llamo SubProceso 
			Escribir convertiradolar(cambio,pesoadolar);
		2:
			Escribir "Ingrese la cantidad de d�lares a convertir a pesos";
			Leer dolarapeso;
			Escribir "	La equivalencia en pesos es:";
			//llamo SubProceso 
			Escribir convertirapesos(cambio,dolarapeso);
		De Otro Modo:
			Escribir "Gracias por utilizar el programa";
	FinSegun
FinProceso
