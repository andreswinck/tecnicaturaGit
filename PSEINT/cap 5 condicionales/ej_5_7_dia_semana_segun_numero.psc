Proceso dia_semana_segun_numero
	// Elaborar un programa que me muestre los d�as de las semanas cuando ingrese los siete primeros n�meros. 
	Definir numero Como Entero;
	Escribir 'Ingrese un n�mero entre 1 y 7: ' Sin Saltar;
	Leer numero;
	Segun numero  Hacer
		1:
			Escribir 'El d�a es Lunes';
		2:
			Escribir 'El d�a es Martes';
		3:
			Escribir 'El d�a es Miercoles';
		4:
			Escribir 'El d�a es Jueves';
		5:
			Escribir 'El d�a es Viernes';
		6:
			Escribir 'El d�a es Sabado';
		7:
			Escribir 'Domingo';
		De Otro Modo:
			Escribir 'N�mero no v�lido';
	FinSegun
FinProceso
