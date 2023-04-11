//Diseñar un algoritmo que pida al usuario 5 apellidos, 
//los almacene en un arreglo y posteriormente muestre 
//los apellidos ordenados alfabéticamente. 
Proceso ordenar_5_apellidos_alfabeticamente
	//Defino variables
	Definir apellido,cambio Como Caracter;
	Definir i,j Como Entero;
	Dimension apellido[5];
	//Se pide el ingreso de los 5 apellidos
	Escribir "Ingrese los 5 apellidos:";
	para i<-0 Hasta 4 Hacer
		Escribir "Ingrese el apellido Nº",i+1," ";
		Leer apellido[i];
	FinPara
	//Se comparan y se ordenan alfabeticamente
	para i<-0 Hasta 4 Hacer
		Escribir "El apellido Nº",i+1," es ",apellido[i];
	FinPara
	para j<-0 Hasta 4 Hacer
				
		Para i<-j+1 Hasta 4 Hacer
			si apellido[i]<apellido[j] Entonces
				cambio<-apellido[i];
				apellido[i]<-apellido[j];
				apellido[j]<-cambio;
			FinSi
			
		FinPara
	FinPara
	//Se muestran ordenados alfabeticamente
	Escribir " ";
	Escribir "Ordenados alfabéticamente quedan:";
	Escribir "";
	para i<-0 Hasta 4 Hacer
		Escribir "El apellido Nº",i+1," es ",apellido[i];
	FinPara
FinProceso
