Proceso calcular_el_maximo_y_el_minimo
	// Ingresar "N" n�meros, calcular el m�ximo y m�nimo de ellos. 
	// defino varables
	Definir canter,i Como Entero;
	Definir termino,minimo,maximo Como Real;
	// se ingresa el n�mero de t�rminos
	Escribir 'Digite la cantidad de terminos que desea ingresar: ' Sin Saltar;
	Leer canter;
	Dimension termino[100];
	// se ingresan los t�rminos
	Para i<-0 Hasta (canter-1) Hacer
		Escribir 'ingrese el t�rmino N�',(i+1) Sin Saltar;
		Leer termino[i];
	FinPara
	// se define como m�ximo y m�nimo el primer n�mero ingresado
	minimo <- termino[0];
	maximo <- termino[0];
	// se comparan los t�rminos para determinar el m�ximo y el m�nimo
	Para i<-0 Hasta (canter-1) Hacer
		Si termino[i]<minimo Entonces
			minimo <- termino[i];
		FinSi
		Si termino[i]>maximo Entonces
			maximo <- termino[i];
		FinSi
	FinPara
	// se muestran los resultados
	Escribir 'el t�rmino M�NIMO es: ',minimo;
	Escribir 'el t�rmino M�XIMO es: ',maximo;
FinProceso
