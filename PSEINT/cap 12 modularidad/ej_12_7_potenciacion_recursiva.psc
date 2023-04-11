//Escribir una funci�n recursiva para elevar un numero a una potencia.  
// Implementaci�n del c�lculo de una potencia mediante una funci�n recursiva
// El paso recursivo se basa en que a^b = se calcula mutiplicando a por si misma 
//tantas veces como sea el valor de b
// Tenieno en cuenta que a^0 = 1
SubProceso potenciacion<-potencia(base,exponente)	
	//Defino variables
	Definir potenciacion Como Entero;
	si exponente=0 Entonces
		//El c�lculo termina cuando el exp es 0
		potenciacion<-1;
	SiNo
		//C�lculo recursivo de la potencia (Base por s� misma tantas
		//veces como sea el n�mero del exponente
		potenciacion<-base*potencia(base,exponente-1);
	FinSi
FinSubProceso

Proceso potenciacion_recursiva
	//Defino variables
	Definir a,b Como Entero;
	//Solicito la base y el exponente
	Escribir "Ingrese el n�mero a elevar a una potencia:";
	Leer a;
	Escribir "Ingrese la potencia a la que desea elevar el n�mero anterior:";
	Leer b;
	//Muestro resultado
	Escribir "El resultado es: ", potencia(a,b);
FinProceso
