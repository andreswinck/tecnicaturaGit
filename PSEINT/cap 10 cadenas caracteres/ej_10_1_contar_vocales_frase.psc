Proceso contar_vocales_frase
	//: Diseñe un programa que permita ingresar una cadena de caracteres, 
	//y detecte cuántas vocales tiene. 
	definir frase,vocales Como Caracter;
	Definir cantvoc,i,j Como Entero;
	Escribir "Ingrese la frase";
	leer frase;
	frase<-Minusculas(frase);
	vocales<-"aeiouáéíóú";
	cantvoc<-0;
	i<-0;
	j<-0;
	para i<-0 Hasta Longitud(frase)-1 Hacer
		para j<-0 Hasta Longitud(vocales)-1 Hacer
			si Subcadena(frase,i,i)=Subcadena(vocales,j,j) Entonces
				Escribir "se detecto la vocal ", Subcadena(vocales,j,j);
				cantvoc<-cantvoc+1;
				
			FinSi
		FinPara
		
	FinPara
	Escribir "La frase tiene ",cantvoc," vocales";
FinProceso