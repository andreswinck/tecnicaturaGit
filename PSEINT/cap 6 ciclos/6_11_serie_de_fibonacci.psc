Proceso serie_de_fibonacci
	// Se trata de una secuencia infinita de n�meros naturales; 
	// a partir del 0 y el 1, se van sumando a pares, de manera que 
	// cada n�mero es igual a la suma de sus dos anteriores, de manera 
	// que: ... 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
	// defino las variables
	Definir i,terminos,num Como Entero;
	// se pide ingresar el n�mero de terminos
	Escribir 'ingrese la cantidad de t�rminos que desea ';
	Escribir 'de la serie hasta un m�ximo de 45';
	Leer terminos;
	// se impone un m�cimo de 45 por las limitaciones del programa
	Si terminos>45 Entonces
		Escribir 'EL M�XIMO ES 45, intente nuevamente';
		Escribir 'ingrese la cantidad de t�rminos que desea ';
		Escribir 'de la serie hasta un m�ximo de 45';
		Leer terminos;
	FinSi
	Dimension num[46];
	// se fijan los primeros 2 valores que son fijos de la serie (0 y 1)
	num[0] <- 0;
	num[1] <- 1;
	Escribir 'La serie de FIBONACCI de ',terminos,' t�rminos es:';
	Escribir '';
	// se muestran los dos primeros t�rminos de la serie que son fijos
	Escribir '0 1 ' Sin Saltar;
	Para i<-2 Hasta (terminos-1) Hacer
		// se determinan los t�rminos siguientes sumando los dos anteriores
		num[i] <- num[i-1]+num[i-2];
		// se muestran los t�rminos de la serie
		Escribir num[i],' ' Sin Saltar;
	FinPara
FinProceso
