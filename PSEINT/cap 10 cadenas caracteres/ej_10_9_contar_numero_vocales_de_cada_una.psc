Proceso contar_numero_vocales_de_cada_una
	//defino varialbes
	Definir frase,car Como Caracter;
	Definir num_a,num_e,num_i,num_o,num_u,i Como Entero;
	Dimension car[100];
	// se pide que se ingrese la frase
	Escribir "ingrese la frase: ";
	Leer frase;
	//se inicializan las variables
	frase<-Minusculas(frase);
	num_a<-0; 
	num_e<-0;
	num_i<-0;
	num_o<-0;
	num_u<-0;
	
	//se parte la frase en sus caracteres y
	//se compara con las vocales
	//si se detecta una vocal se contabiliza
	para i<-0 Hasta Longitud(frase)-1 Hacer
		car[i]<-Subcadena(frase,i,i);
		si car[i]="a" o	car[i]="á" Entonces
			num_a<-num_a+1;
		FinSi
		si car[i]="e" o	car[i]="é" Entonces
			num_e<-num_e+1;
		FinSi
		si car[i]="i" o	car[i]="í" Entonces
			num_i<-num_i+1;
		FinSi
		si car[i]="o" o	car[i]="ó" Entonces
			num_o<-num_o+1;
		FinSi
		si car[i]="u" o	car[i]="ú" Entonces
			num_u<-num_u+1;
		FinSi
	
	FinPara
	//se escribe el resultado de cada vocal
	Escribir "La cantidad de cada vocal es: ";
	Escribir num_a, " a";
	Escribir num_e, " e";
	Escribir num_i, " i";
	Escribir num_o, " o";
	Escribir num_u, " u";
FinProceso
