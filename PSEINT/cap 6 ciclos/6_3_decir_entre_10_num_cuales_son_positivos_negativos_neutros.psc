Proceso decir_entre_10_num_cuales_son_positivos_negativos_neutros
	Definir i,num Como Entero;
	Dimension num[10];
	Para i<-0 Hasta 9 Hacer
		Escribir 'ingrese el n�mero ',(i+1) Sin Saltar;
		Leer num[i];
	FinPara
	Escribir '';
	Escribir 'Ahora se determinar� cual es positivo, negativo, o neutro';
	Escribir '';
	Para i<-0 Hasta 9 Hacer
		Si num[i]<0 Entonces
			Escribir 'el n�mero ',num[i],' es negativo';
		FinSi
		Si num[i]>0 Entonces
			Escribir 'el n�mero ',num[i],' es positivo';
		FinSi
		Si num[i]=0 Entonces
			Escribir 'el n�mero ',num[i],' es neutro';
		FinSi
	FinPara
FinProceso
