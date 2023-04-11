//Diseñe un algoritmo que contenga el siguiente menú: 
	//1.	Llenar una matriz de 4*4 
	//2.	Mostrar la matriz 
	//3.	Sumar todos los elementos de la matriz 
	//4.	Salir 

Proceso algoritmo_con_menu
	//defino variables
	Definir opcion,num,i,j,k,suma,cont Como Entero;
	Dimension num[4,4];
	suma<-0;
	k<-0;
	//Muestro menu de opciones
	Repetir
		Limpiar Pantalla;
	Escribir "Ingrese la opcion deseada";
	Escribir "1<-Llenar matriz de 4x4";
	Escribir "2<-Mostrar la matriz";
	Escribir "3<-Sumar elementos de la matriz";
	Escribir "4<-Salir";
	
		
		Leer opcion;
		Segun opcion Hacer
			1:
				//opcion 1 llenar matriz
				Limpiar Pantalla;
				Escribir "Usted eligió llenar matriz 4x4";
				Para i<-0 Hasta 3 Hacer
					Para j<-0 Hasta 3 Hacer
						k<-k+1;
						Escribir "Ingrese el elemento Nº",k;
						leer num[i,j];
					FinPara
				FinPara
				k<-0;
				Limpiar Pantalla;
			2:
				Limpiar Pantalla;
				//Opcion 2 mostrar los valores ingresados
				Escribir "Sólo funciona ésta opción si se";
				Escribir "ingresaron los elementos de la matriz";
				Escribir "Anteriormente";
				Escribir "Los elementos de la matriz son:";
			
				Para i<-0 Hasta 3 Hacer
					Para j<-0 Hasta 3 Hacer
						Escribir Sin Saltar num[i,j]," ";
					FinPara
					Escribir "";
				FinPara
				Escribir "presione una tecla para continuar";
				leer cont;
				
			3:
				//Muestra la suma de los elementos
				Escribir "";
				Escribir "La suma de los elementos de la matriz es:";
				para i<-0 Hasta 3 Hacer
					para j<-0 Hasta 3 Hacer
						suma<-suma+num[i,j];
					FinPara
				FinPara
				Escribir "";
				Escribir suma;
				Escribir "";
				Escribir "presione una tecla para continuar";
				leer cont;
				suma<-0;
			4:
				//Sale del programa
				Escribir "Programa finalizado por el usuario";
		FinSegun
Hasta Que opcion=4;
FinProceso
