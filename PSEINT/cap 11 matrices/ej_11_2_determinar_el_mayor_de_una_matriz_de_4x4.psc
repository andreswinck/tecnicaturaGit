Proceso determinar_el_mayor_de_una_matriz_de_4x4
	// defino variables
	Definir num,mayor Como Real;
	Definir i,j,k,auto,l,m Como Entero;
	//Definir auto Como caracter;
	Dimension num[4,4];
	k <- 1;
	l<-0;
	m<-0;
	// Se ingresan los datos para llenar la matriz 
	//Se da la opci�n de llenarla autom�ticamente o manualmente
	
	Repetir
		Escribir 'El programa determinar� el mayor de 16 n�meros';
		Escribir "Desea que el programa llene autom�ticamente la matriz? (1=si/2=no)";
		Leer auto;
			si auto=1 Entonces
				Para i<-0 Hasta 3 Hacer
					Para j<-0 Hasta 3 Hacer
						num[i,j]<-azar[100];
					FinPara
				FinPara
			SiNo
				si auto=2 Entonces
					Para i<-0 Hasta 3 Hacer
						Para j<-0 Hasta 3 Hacer
							Escribir 'Ingrese el n�mero ',k,'/16';
							Leer num[i,j];
							k <- k+1;
						FinPara
					FinPara
				FinSi
				
			FinSi
		Hasta Que auto>0 y auto<3
		Escribir "Los n�meros ingresados son:";
		Para i<-0 Hasta 3 Hacer
			Para j<-0 Hasta 3 Hacer
			
				Escribir Sin Saltar num[i,j]," ",;
					mayor <- num[i,j];
				FinPara
				Escribir "";
		FinPara
	
	// Se determina el mayor
	mayor <- num[0,0];
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Si num[i,j]>mayor Entonces
				mayor <- num[i,j];
				l<-i+1;
				m<-j+1;
			FinSi
		FinPara
	FinPara
	// Se muestra el mayor n�mero ingresado
	Escribir '';
	Escribir "*****************";
	Escribir 'El mayor es: ',mayor," fila ",l," columna ",m;
	Escribir "*****************";
FinProceso
