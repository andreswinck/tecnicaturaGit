Proceso calcular_la_sumatoria
	//calcular la sumatoria para la serie dada
	//s=1+(x^n)/n!
	Definir i, terminos, x, fact Como Entero;
	Definir s Como Real;
	//inicializo variables
	fact<-1;
	s<-1;
	Escribir Sin Saltar "Escriba la cantidad de t�rminos que desea calcular de la serie";
	Leer terminos;
	Para i<-1 Hasta terminos Hacer
		//calculo factorizacion y valor de serie para los terminos desde 1 Hasta
		//el t�rmino ingresado
		fact<-fact*i;
		s<-s+i^i/fact;
	FinPara
//Se muestra el resultado	
Escribir "La sumatoria para los ", terminos," t�rminos solicitados es: ", s;
FinProceso
