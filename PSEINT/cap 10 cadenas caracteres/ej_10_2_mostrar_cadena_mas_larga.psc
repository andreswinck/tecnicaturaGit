Proceso mostrar_cadena_mas_larga
	// Calcular la longitud de 2 cadenas de caracteres, 
	//y mostrar la cadena con la mayor longitud.
	Definir cad1,cad2 Como Caracter;
	Definir a,b Como Entero;
	Escribir "Ingrese la primera cadena de caracteres";
	Leer cad1;
	Escribir "Ingrese la segunda cadena de caracteres";
	Leer cad2;
	//se guarda la longitud de cada cadena en a y b
	a<-Longitud(cad1);
	b<-Longitud(cad2);
	// se compara a y b y se muestra la más extensa
	si a>b Entonces
		Escribir "La cadena más larga es: ", cad1;
	SiNo
		Escribir "La cadena más larga es: ", cad2;
		
	FinSi
	
FinProceso
