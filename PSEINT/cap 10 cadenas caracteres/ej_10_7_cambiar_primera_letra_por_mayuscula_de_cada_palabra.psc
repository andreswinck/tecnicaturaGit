Proceso cambiar_primera_letra_por_mayuscula_de_cada_palabra
	//Ingresar una frase y modificarla convirtiendo 
	//el primer carácter de cada palabra si esta fuera 
	//una letra, de minúsculas a mayúsculas. 
	Definir frase,car,numer Como Caracter;
	Definir largo,i,j Como Entero;
	Escribir "Ingrese la frase a la cual se le cambiarán las primeras letras:";
	Leer frase;
	Dimension car[100];
	largo<-Longitud(frase);
	numer<-"0123456789";
	Escribir  Sin Saltar "el largo es: ",largo;
	Para i<-0 hasta largo-1 Hacer
		car[i]<-SubCadena(frase,i,i);
		Escribir "";
		Escribir "indice ",i," caracter ", car[i];
	FinPara
		para j<-0 Hasta Longitud(numer)-1 Hacer
		
	
			si car[0]<>Subcadena(numer,j,j) Entonces
				car[0]<-Mayusculas(car[0]);		
			FinSi
		FinPara
	para i<-0 Hasta largo-1 Hacer
		
		si car[i]=" " Entonces
			para j<-0 Hasta Longitud(numer)-1 Hacer
				
				si car[i+1]<> Subcadena(numer,j,j) Entonces
					car[i+1]<-Mayusculas(car[i+1]);
				FinSi
				
			
			FinPara
		FinSi
	FinPara
	para i<-0 Hasta largo-1 Hacer
		Escribir Sin Saltar car[i];
	FinPara
	Escribir "";
	
FinProceso
