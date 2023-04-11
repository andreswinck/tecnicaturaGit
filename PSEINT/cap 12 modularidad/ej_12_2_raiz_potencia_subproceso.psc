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
//Dise�e un algoritmo que muestre un men� al usuario 
//con las siguientes opciones: potenciaci�n, ra�z cuadrada 
//y terminar, que cada opci�n la realice una funci�n o procedimiento. 
	
//defino las variables	
	Definir op,bas,expon,radic,indic Como entero;
Repetir
		//men� de opciones que llama a los SubProcesos Segun la opci�n ingresada
	Escribir "Ingrese la opci�n deseada";
	Escribir "1 <- potenciaci�n";
	Escribir "2 <- radicaci�n";
	Escribir "3 <- Fin del programa";
	Leer op;
Hasta Que op>0 y op <4 
	Segun op Hacer
		1:
			Escribir "Ingrese la base";
			leer bas;
			Escribir "ingrese el esponente";
			leer expon;
			Escribir "el n�mero ",bas," elevado a la ",expon," potencia tiene como resultado: ";
			Escribir "* ",potencia(bas,expon)," *";
		2:
			Escribir "Ingrese el radicando";
			leer radic;
			Escribir "ingrese el �ndice de radicaci�n";
			leer indic;
			Escribir "La ra�z ",indic," del n�mero ",radic," tiene como resultado: ";
			Escribir "* ",resultaraiz(radic,indic)," *";
		3:
			Escribir "Fin del programa";
	
	FinSegun
	
FinProceso
