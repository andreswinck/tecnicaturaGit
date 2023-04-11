//SubProceso que calcula la potencia
//se invoca como "potencia"
//usa la variable pot para calcularla
SubProceso pot<-potencia(base,exponente)
	Definir pot Como Real;
	pot<-base^exponente;
FinSubProceso
//SubProceso que calcula la raiz
//se invoca como "resultaraiz"
//usa radicacion para calcularla
SubProceso radicacion<-resultaraiz(radicando,indice)
	Definir radicacion Como Real;
	radicacion<-radicando^(1/indice);
FinSubProceso
Proceso raiz_potencia_subproceso
//Diseñe un algoritmo que muestre un menú al usuario 
//con las siguientes opciones: potenciación, raíz cuadrada 
//y terminar, que cada opción la realice una función o procedimiento. 
	
//defino las variables	
	Definir op,bas,expon,radic,indic Como entero;
Repetir
		//menú de opciones que llama a los SubProcesos Segun la opción ingresada
	Escribir "Ingrese la opción deseada";
	Escribir "1 <- potenciación";
	Escribir "2 <- radicación";
	Escribir "3 <- Fin del programa";
	Leer op;
Hasta Que op>0 y op <4 
	Segun op Hacer
		1:
			Escribir "Ingrese la base";
			leer bas;
			Escribir "ingrese el esponente";
			leer expon;
			Escribir "el número ",bas," elevado a la ",expon," potencia tiene como resultado: ";
			Escribir "* ",potencia(bas,expon)," *";
		2:
			Escribir "Ingrese el radicando";
			leer radic;
			Escribir "ingrese el índice de radicación";
			leer indic;
			Escribir "La raíz ",indic," del número ",radic," tiene como resultado: ";
			Escribir "* ",resultaraiz(radic,indic)," *";
		3:
			Escribir "Fin del programa";
	
	FinSegun
	
FinProceso
