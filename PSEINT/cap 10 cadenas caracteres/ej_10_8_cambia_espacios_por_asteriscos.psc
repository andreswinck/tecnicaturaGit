Proceso cambia_espacios_por_asteriscos
	// Sustituir todos los espacios en blanco de una frase por un asterisco (*). 
	Definir cad,separado Como Caracter;
	Definir largo,i Como Entero;
	Dimension separado[100];
	// poide que se ingrese la frase
	Escribir 'Ingrese la cadena para cambiar los espacios por (*): ';
	Leer cad;
	// inicializo las variables
	i <- 0;
	largo <- Longitud(cad);
	// separo los caracteres y los pongo en un arreglo para 
	// despues detectar los espacios
	Para i<-0 Hasta largo-1 Hacer
		separado[i] <- Subcadena(cad,i,i);
	FinPara
	// compara cada caracter con el ESPACIO y si es un espacio
	// lo cambia por un asterisco
	Para i<-0 Hasta largo-1 Hacer
		Si separado[i]=' ' Entonces
			separado[i] <- '*';
		FinSi
	FinPara
	// muestra la frase con asteriscos en vez de espacios
	Escribir '***************************';
	Escribir 'LA FRASE CON ASTERISCOS ES:';
	Escribir '***************************';
	Para i<-0 Hasta largo-1 Hacer
		Escribir separado[i] Sin Saltar;
	FinPara
	Escribir '';
FinProceso
