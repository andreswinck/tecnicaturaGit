Proceso encontrar_subcadena_en_frase
	//Realizar un programa que permita contabilizar 
	//cuantas veces una subcadena se repite dentro de una frase. 
	
	//defino variables
	Definir frase,subc Como Caracter;
	Definir larfra,larsubc,i,repe Como entero;
	//se pide se ingrese la frase e y la cadena a buscar
	Escribir "ingrese la frase a comparar: ";
	leer frase;	
	Escribir "ingrese la cadena a buscar en la frase: ";
	leer subc;
	Dimension car[100];
	//se encuentra longitud de la frase y la cadena
	larfra<-Longitud(frase);
	larsubc<-Longitud(subc);
	repe<-0;
	//se comparan tantos caracteres como el largo 
	//de la subcadena con los caracteres de la cadena original
	//recorriendola y guardando cuando son iguales en
	//la variable repe
	para i<-0 Hasta (larfra-larsubc) Hacer
		
		si Subcadena(frase,i,larsubc-1+i)=subc Entonces
			
			repe<-repe+1;
		FinSi
	FinPara
	// se muestra el resultado
	Escribir "la cadena ",subc," se repite ",repe," veces";
FinProceso
