Proceso detectar_palidromo
	// Diseñar un algoritmo que tomando como entrada 
	// una cadena de texto nos devuelva si es o no un palíndromo. 
	// Se conoce que se denomina palíndromo a una palabra o frase que, 
	// ignorando los blancos, se lee igual de izquierda a derecha que 
	// de derecha a izquierda. 
	Definir cad,separado,comodin Como Caracter;
	Definir largo,i,j,k,l Como Entero;
	Definir medio Como Real;
	Definir palidromo Como Logico;
	Dimension separado[100];
	// pide que se ingrese la frase
	Escribir 'Ingrese la cadena para determinar si es un palidromo';
	Leer cad;
	// inicializo las variables
	i <- 0;
	j <- 0;
	k <- 0;
	medio <- 0;
	largo <- Longitud(cad);
	// Escribir 'largo inicial ',largo
	palidromo <- Falso;
	l <- largo-1;
	// separo los caracteres para luego invertirlos
	Para i<-0 Hasta largo-1 Hacer
		separado[i] <- Subcadena(cad,i,i);
	FinPara
	Para i<-0 Hasta l Hacer
		Si separado[i]=' ' Entonces
			j <- i;
			Para k<-j Hasta l-1 Hacer
				separado[k] <- separado[k+1];
			FinPara
			l <- l-1;
		FinSi
	FinPara
	// aca determmino si el largo es par o impar y defino la mitad de la frase
	// defino el nuevo largo sin espacios
	largo <- l+1;
	// Escribir 'largo sin espacios ',largo
	Si largo MOD (2)=0 Entonces
		medio <- largo/2;
		// si es par comparo directamente
		Para i<-0 Hasta (medio-1) Hacer
			Si separado[i]=separado[largo-1-i] Entonces
				palidromo <- Verdadero;
			SiNo
				palidromo <- Falso;
			FinSi
		FinPara
	SiNo
		// si es impar determino el termino medio y no se icompara el que esta 
		// justo en la mitad
		medio <- ((largo/2)-0.5);
		Para i<-0 Hasta medio-1 Hacer
			Si separado[i]=separado[largo-1-i] Entonces
				palidromo <- Verdadero;
			SiNo
				palidromo <- Falso;
			FinSi
		FinPara
	FinSi
	// responde el programa si es un palidromo o no segun sea verdadero o falso
	Si palidromo=Verdadero Entonces
		Escribir '**************************';
		Escribir ' LA FRASE ES UN PALIDROMO ';
		Escribir '**************************';
	SiNo
		Escribir '*****************************';
		Escribir ' LA FRASE NO ES UN PALIDROMO ';
		Escribir '*****************************';
	FinSi
FinProceso
