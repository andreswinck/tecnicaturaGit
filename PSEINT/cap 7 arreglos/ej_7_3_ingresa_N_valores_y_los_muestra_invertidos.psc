Proceso ej_7_3_ingresa_N_valores_y_los_muestra_invertidos
	Definir lista,i,j,r Como Real;
	Dimension lista[100];
	Escribir "Ingrese los datos, recuerde que el programa soporta un m�ximo de 100 valores";
	i<-0;
	//se pide el ingreso de datos
	Repetir
		Escribir Sin Saltar "Ingrese un valor, recuerde que para finalizar deber� ingresar 0.01";
		Leer lista[i];
		i<-i+1; //se incrementa el indice en 1
	Hasta Que i=100 o lista[i-1]=0.01 // se evalua que sean menos de 100 datos y que no sea igual a 0.01
										
	Escribir "la lista original ingresada es: "; // se muestra lista original
	si i=100 Entonces  //evalua si se lleg� al limite de datos
		r<-i-1;		   // o se sali� por ingreso de 0.01
	SiNo			   // dependiendo de ello se define cual ser� el �ltimo valor del indice del vector
		r<-i-2;         // se elimina 1 si se lleg� si limite � 2 si se ingres� 0.01 
	FinSi
	Para j<-0 Hasta r	Hacer // el indice va hasta r 
							  // 
		Escribir Sin Saltar "", lista[j], ", ";
	FinPara
	
	Escribir "la lista en orden inverso es: "; // se muestra lista invertida
	Para j<-(r) Hasta 0 Con Paso -1	Hacer
		Escribir Sin Saltar "", lista[j], ", ";
	FinPara
	//FinPara
	

FinProceso
