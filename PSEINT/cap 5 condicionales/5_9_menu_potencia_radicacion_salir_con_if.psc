Proceso sin_titulo
	// Hacer un programa que tenga un men� con las siguientes opciones:  
	// Opci�n 1: Elevar un n�mero a una potencia X 
	// Opci�n 2: Sacar la ra�z cuadrada de un n�mero 
	// Opci�n 3: Salir 
	Definir opcion Como Entero;
	Definir base,pot,res1,radic,ind Como Real;
	// mostrar menu
	Escribir ' ';
	Escribir '1 - elevar un n�mero a una potencia dada';
	Escribir '2 - Calcular la ra�z cuadrada de un n�mero dado';
	Escribir '3 - Salir';
	Escribir ' ';
	Escribir 'Elija una opci�n: ' Sin Saltar;
	Leer opcion;
	// calcula potencia si elige la opcion 1
	Si opcion=1 Entonces
		Escribir 'Ingrese la base: ' Sin Saltar;
		Leer base;
		Escribir 'Ingrese la potencia: ' Sin Saltar;
		Leer pot;
		res1 <- base^pot;
		Escribir 'el resultado de la potenciaci�n es: ',res1;
	SiNo
		// calcula la raiz si elige la opcion 2
		Si opcion=2 Entonces
			Escribir 'Ingrese el radicando: ' Sin Saltar;
			Leer radic;
			Escribir 'Ingrese el �ndice: ' Sin Saltar;
			Leer ind;
			res1 <- radic^(1/ind);
			Escribir 'el resultado de la potenciaci�n es: ',res1;
		SiNo
			// sale del programa si elige la opcion 3
			Escribir 'Fin del programa';
		FinSi
	FinSi
FinProceso
