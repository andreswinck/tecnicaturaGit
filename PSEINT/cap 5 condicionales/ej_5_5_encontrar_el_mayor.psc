Proceso encontrar_el_mayor
	Definir a,b,c,mayor Como Real;
	Escribir Sin Saltar"Ingrese el primer n�mero";
	Leer a;
	Escribir Sin Saltar"Ingrese el segundo n�mero";
	Leer b;
	Escribir Sin Saltar"Ingrese el tercer n�mero";
	Leer c;
	mayor<-a;
	si b>mayor Entonces
		mayor<-b;
	FinSi
	si c>mayor Entonces
		mayor<-c;
	FinSi
	Escribir Sin Saltar"el mayor de los tres n�meros es: ", mayor;
	Escribir "";
	Escribir "";
FinProceso
