Proceso determina_si_el_numero_es_par_o_impar
	Definir a Como Real;
	Escribir Sin Saltar"ingrese un numero; ";
	Leer a;
	//determina si es entero al restar al n�mero la parte entera y 
	// determinar si la parte decimal es distinta de cero
	Si (a-trunc(a)) <> 0 Entonces
		Escribir "el numero no es entero";
	SiNo
		//saca el resto de la divisi�n del n�mero por 2
		// si es impar, el resto da como resultado 1
		//en cambio para los pares el resto siempre es 0
		Si a MOD(2) = 0 Entonces
			Escribir "El n�mero es par";
			
		SiNo
			Escribir "el n�mero es impar";
			
		FinSi
	FinSi
	
FinProceso
