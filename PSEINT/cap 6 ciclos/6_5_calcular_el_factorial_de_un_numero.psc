Proceso factorial_de_un_numero
	//Calcular el factorial de un n�mero mayor o igual a 0. 
	Definir num,i,fact Como Entero;
	// pide que se ingrese el n�mero
	Escribir Sin Saltar "ingrese el n�mero para calcular el factorial del mismo";
	Leer num;
	i<-0;
	fact<-1;
	// si el n�mero es mayor que 0 calcula el factorial
	si num>0 Entonces
		Para i<-1 Hasta num	Hacer
			fact<-fact*i;
		FinPara
		Escribir "";
		Escribir "el factorial de ",num," es ", fact;	
		Escribir "";
	FinSi
	// si es 0 lo pone por definici�n
	si num=0 Entonces
		Escribir "";
		Escribir "El factorial de 0 es 1 por definici�n";
		Escribir "";
	FinSi
	// si el n�mero es negativo indica que no se puede calcular
	si num<0 Entonces
		Escribir "";
		Escribir "No se puede calcular el factorial de un n�mero negativo";
		Escribir "";
	FinSi
FinProceso
