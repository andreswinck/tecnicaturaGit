Proceso imprimir_diagonal_de_matriz
	//Hacer un algoritmo que llene una matriz de 4*4  
	//y que almacene la diagonal principal en un arreglo. 
	//Imprimir el arreglo resultante. 
	// defino variables
	Definir num,diagonal Como Real;
	Definir i,j,k,auto Como Entero;
	Dimension num[4,4],diagonal[4];
	k <- 1;
	// Se ingresan los datos para llenar la matriz 
	// Se da la opci�n de llenarla autom�ticamente o manualmente
	Repetir
		Escribir 'El programa determinar� el mayor de 16 n�meros';
		Escribir 'Desea que el programa llene autom�ticamente la matriz? (1=si/2=no)';
		Leer auto;
		Si auto=1 Entonces
			Para i<-0 Hasta 3 Hacer
				Para j<-0 Hasta 3 Hacer
					num[i,j]<-azar(10);
				FinPara
			FinPara
		SiNo
			Si auto=2 Entonces
				Para i<-0 Hasta 3 Hacer
					Para j<-0 Hasta 3 Hacer
						Escribir 'Ingrese el n�mero ',k,'/16';
						Leer num[i,j];
						k <- k+1;
					FinPara
				FinPara
			FinSi
		FinSi
	Hasta Que auto>0 Y auto<3
	//se muestran los datos ingresados
	Escribir 'Los n�meros ingresados son:';
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir num[i,j],' ', Sin Saltar;
		FinPara
		Escribir "";
	FinPara
	//almaceno datos diagonal principal en el arreglo diagonal[j]
	Para j<-0 Hasta 3 Hacer
		diagonal[j]<-num[j,j];
	FinPara
	Escribir '';
	Escribir "Los datos de la diagonal principal son :";
	Para j<-0 Hasta 3 Hacer
		
		Escribir diagonal[j],' ', Sin Saltar;
	FinPara
	Escribir "";
FinProceso
