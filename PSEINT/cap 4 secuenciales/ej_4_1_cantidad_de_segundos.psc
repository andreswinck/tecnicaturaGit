Proceso cantidad_de_segundos
	Definir h,m,s,cantsegtot Como Real;
	Escribir"El siguiente programa calcular� cuantos segundos";
	Escribir "hay en el n�mero de horas, minutos y segundos que se ingresen";
	Escribir Sin Saltar"ingrese el n�mero de horas";
	Leer h;
	Escribir Sin Saltar"ingrese el valor de minutos";
	Leer m;
	Escribir Sin Saltar"ingrese el valor de segundos";
	Leer s;
	//
	cantsegtot<- (s+(m*60)+(h*3600));
	
	Escribir Sin Saltar "El n�mero total de segundos es de :",cantsegtot;

	
FinProceso
