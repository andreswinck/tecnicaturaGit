Proceso suma_N_numeros
	//Calcular la suma de los "N" primeros n�meros
	Definir numfinal, sumanum,i Como Entero;
	Escribir Sin Saltar "Se sumar�n los n�meros desde el 1 hasta el que ingrese a continuaci�n: ";
	Leer numfinal;
	sumanum<- 0;
	// genera un ciclo desde i=1 hasta el n�mero introducido y lo suma a sumanum
	Para i<-1 Hasta numfinal Con Paso 1 Hacer
		sumanum<- sumanum + i;
	FinPara
	// da el resultado de la suma
	Escribir "el resultado de sumar desde el 1 hasta el ", numfinal," es: ", sumanum;
FinProceso
