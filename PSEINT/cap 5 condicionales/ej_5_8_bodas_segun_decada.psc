Proceso sin_titulo
	// Elaborar un programa que me muestre el significado de aniversario de cada d�cada hasta los 60
	Definir opcion Como Entero;
	Repetir
		Borrar Pantalla;
		Escribir 'El siguiente programa devuelve el nombre';
		Escribir 'que reciben las d�cadas de casado';
		Escribir 'por favor ingrese de cuantas d�cadas de casado desa conocer el nombre';
		Escribir 'pudiendo ser entre 1 y 6 decadas, � ingrese 0 para salir del programa' Sin Saltar;
		Leer opcion;
		// segpun la opcion elegida entre 1 y 6 devuelve el nombre que reciben las bodas
		Segun opcion  Hacer
			1:
				Escribir '----------------------------------------------------';
				Escribir '// A los 10 a�os se cumplen las Bodas de Hojalata //';
				Escribir '____________________________________________________';
			2:
				Escribir '-----------------------------------------------------';
				Escribir '// A los 20 a�os se cumplen las Bodas de Porcelana //';
				Escribir '_____________________________________________________';
			3:
				Escribir '---------------------------------------------------';
				Escribir '// A los 30 a�os se cumplen las Bodas de Perlas  //';
				Escribir '___________________________________________________';
			4:
				Escribir '-------------------------------------------------';
				Escribir '// A los 40 a�os se cumplen las Bodas de Rub� //';
				Escribir '________________________________________________';
			5:
				Escribir '-----------------------------------------------';
				Escribir '// A los 50 a�os se cumplen las Bodas de Oro //';
				Escribir '_______________________________________________';
			6:
				Escribir '----------------------------------------------------';
				Escribir '// A los 60 a�os se cumplen las Bodas de Diamante //';
				Escribir '____________________________________________________';
			0:
				Escribir '-----------------------------------';
				Escribir '// Gracias por usar el programa  //';
				Escribir '___________________________________';
			De Otro Modo:
				Escribir '***************************';
				Escribir '*     Opci�n no v�lida    *';
				Escribir '*   INT�NTELO NUEVAMENTE  *';
				Escribir '* Ingrese 1,2,3,4,5,6 � 0 *';
				Escribir '***************************';
		FinSegun
		Esperar Tecla;
	Hasta Que opcion=0
FinProceso
