Proceso eliminar_elemento_sin_dejar_huecos
	// Leer por teclado un arreglo de 5 elementos num�ricos 
	// y una posici�n (entre 0 y 4). Eliminar el elemento 
	// situado en la posici�n dada sin dejar huecos. 
	// define las variables
	Definir i,num,posicion,eliminado Como Entero;
	Dimension num[5];
	// se pide el ingreso de 5 numeros
	Escribir 'ingrese 5 n�meros';
	Para i<-0 Hasta 4 Hacer
		Escribir 'ingrese el elemnto N� ',i,' ' Sin Saltar;
		Leer num[i];
	FinPara
	// pide que se ingrese la posicion y se repite si el n�mero 
	// es <0 o >4
	Repetir
		Escribir 'Ingrese una posici�n entre 0 y 4' Sin Saltar;
		Leer posicion;
	Hasta Que posicion>-1 Y posicion<5
	// guarda el numero eliminado para mostrarlo al final
	eliminado <- num[posicion];
	// cambia las posiciones de los elementos para eliminar el hueco del eliminado
	Para i<-posicion Hasta 3 Hacer
		num[i] <- num[i+1];
	FinPara
	// muestra la lista final
	Escribir 'la lista queda';
	Para i<-0 Hasta 3 Hacer
		Escribir num[i],' ' Sin Saltar;
	FinPara
	Escribir '';
	// muestra el numero eliminado
	Escribir 'El n�mero eliminado es ',eliminado;
	Escribir "";
	
FinProceso
