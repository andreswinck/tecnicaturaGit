Funcion convertir<-digitos(entrada_digitos)
	Definir i, convertir, num, long, suma Como Entero;
	Definir dato Como Caracter;
	Dimension num[99];
	i<-0;
	long<-Longitud(entrada_digitos);
	suma<-0;
	Para i<-0 Hasta long-1 Con Paso 1 Hacer
		dato<-Subcadena(entrada_digitos,i,i);
		convertir<-ConvertirANumero(dato);
		num[i]<-convertir;
		suma<-suma+num[i];
	FinPara
	Escribir "La suma de los digitos ingresados es:  ",suma;
FinFuncion

Proceso Cap12_Modularidad_ej_9
	//Ejercicio 9: Implementar un subprograma recursivo que permita sumar los dígitos de un número
	
	Definir entrada_digitos Como caracter;

	Escribir "Por favor ingrese digitos";
	Leer entrada_digitos;
	
	Escribir Sin Saltar digitos(entrada_digitos);
FinProceso
