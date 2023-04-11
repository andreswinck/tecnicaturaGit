// Implementar un subprograma recursivo que realice la serie Fibonacci.
// SubProceso que calcula los términos de fibonacci
// fijando los dos primeros como 1
SubProceso fibonacci <- fibo(cantidad)
	Definir fibonacci Como Entero;
	Si cantidad=1 O cantidad=2 Entonces
		// Si cantidad es 1 o 2 el resultado es 1 porque son los
		// dos primeros términos fijos de la serie
		fibonacci <- 1;
	SiNo
		// Si es mayor a 2 calculo los términos (n)
		// sumando los términos anteriores (n-1) y (n-2) en forma recursiva
		// f(n)=f(n-1)+f(n-2)
		fibonacci <- fibo(cantidad-1)+fibo(cantidad-2);
	FinSi
FinSubProceso

Proceso fibonacci_recursivo
	// Defino variables
	Definir terminos,i Como Entero;
	// Solicito que ingrese el número de términos
	Escribir 'Ingrese la cantidad de términos de Fibonacci que desea visualizar:';
	Leer terminos;
	// Muestro los términos desde el primero hasta el solicitado
	Escribir 'La serie de Fibonacci hasta el término ',terminos,' es:';
	Para i<-1 Hasta terminos Hacer
		Escribir 'El término ',i,' es ',fibo(i);
	FinPara
FinProceso
