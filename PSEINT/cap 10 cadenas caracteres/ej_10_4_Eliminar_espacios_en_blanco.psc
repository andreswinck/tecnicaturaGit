Proceso Eliminar_espacios_en_blanco
	// Diseñe un algoritmo que elimine los espacios en blanco de un texto.
	// defino las variables a utilizar
	Definir cad,separado Como Caracter;
	Definir largo,a,b,i,j,k,l Como Entero;
	Dimension separado[100];
	// poide que se ingrese la frase
	Escribir 'Ingrese la cadena para eliminarle los espacios: ';
	Leer cad;
	// inicializo las variables
	i <- 0;
	j <- 0;
	k <- 0;
	l <- 0;
	largo <- Longitud(cad);
	// separo los caracteres y los pongo en un arreglo para despues detectar los espacios
	Para i<-0 Hasta largo-1 Hacer
		separado[i] <- Subcadena(cad,i,i);
	FinPara
	l <- (largo-1);
	// compara cada caracter con el ESPACIO y si es un espacio
	// corre todos los caracteres que siguen un lugar en el arreglo
	Para i<-0 Hasta l Hacer
		Si separado[i]=' ' Entonces
			j <- i;
			Para k<-j Hasta l-1 Hacer
				separado[k] <- separado[k+1];
			FinPara
			l <- l-1;
		FinSi
	FinPara
	// muestra la frase sin espacios
	Escribir '***************************';
	Escribir 'LA FRASE SIN SEPARACIÓN ES:';
	Escribir '***************************';
	Para i<-0 Hasta l Hacer
		Escribir separado[i] Sin Saltar;
	FinPara
	Escribir '';
FinProceso
