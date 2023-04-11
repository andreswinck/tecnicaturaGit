Proceso invertir_caracteres
	//Cambiar una cadena de caracteres, al revés 
	Definir cad,separado,comodin Como Caracter;
	Definir largo,i Como Entero;
	Definir medio como real;
	Dimension separado[100];
	// pide que se ingrese la frase
	Escribir 'Ingrese la cadena para invertir sus caracteres: ';
	Leer cad;
	// inicializo las variables
	i <- 0;
	medio<-0;
	largo <- Longitud(cad);
	
		// separo los caracteres para luego invertirlos
	Para i<-0 Hasta largo-1 Hacer
		separado[i] <- Subcadena(cad,i,i);
	FinPara
	// aca determmino si el largo es par o impar y defino la mitad de la frase
	Si largo MOD(2) = 0 Entonces
		medio<-largo/2;
		//si es par intercambio directamente
		para i<-0 Hasta (medio-1) Hacer
			comodin<-separado[i];
			separado[i]<-separado[largo-1-i];
			separado[largo-1-i]<-comodin;
		FinPara
	SiNo
		//si es impar determino el termino medio y no se intercambia el que esta 
		//justo en la mitad
		medio<-((largo/2)-0.5);
		para i<-0 Hasta medio-1 Hacer
			comodin<-separado[i];
			separado[i]<-separado[largo-1-i];
			separado[largo-1-i]<-comodin;
		FinPara
	FinSi
	

	
	Escribir '***************************';
	Escribir 'LA FRASE INVERTIDA ES:';
	Escribir '***************************';
	Para i<-0 Hasta largo-1 Hacer
		Escribir separado[i] Sin Saltar;
	FinPara
	Escribir '';
FinProceso
