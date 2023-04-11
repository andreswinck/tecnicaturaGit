//Escriba un subprograma nombrado cambio() 
//que tenga un parámetro en número entero 
//y seis parámetros de referencia en número entero n
//ombrados cien, cincuenta, veinte, diez, cinco y uno, 
//respectivamente. La función tiene que considerar el 
//valor entero transmitido como una cantidad en dólares 
//y convertir el valor en el número menor de billetes equivalentes. 
SubProceso cambio<-desglose(monto)
	//defino variables
	Definir bil100,bil50,bil20,bil10,bil5,bil1 Como Real;
	//calculo la cantidad de billetes de 100
	//como el resultado de la parte entera del valor divido 100
	bil100<-trunc(monto/100);
	//la cantidad de billetes de 50 restandole la cantidad de 100
	bil50<-trunc((monto-(bil100*100))/50);
	//la cantidad de 20 restandole la cant de 100 y de 50
	bil20<-trunc((monto-bil100*100-bil50*50)/20);
	//la cantidad de 10
	bil10<-trunc((monto-bil100*100-bil50*50-bil20*20)/10);
	//la cantidad de 5
	bil5<-trunc((monto-bil100*100-bil50*50-bil20*20-bil10*10)/5);
	//y la cantidad de 1
	bil1<-trunc((monto-bil100*100-bil50*50-bil20*20-bil10*10-bil5*5));
	//escribe la cantidad de billetes siempre y cuando no sea cero
	si bil100<>0 Entonces
		Escribir bil100," billetes de 100 u$s";
	FinSi
	si bil50<>0 Entonces
		Escribir bil50," billetes de 50 u$s";
	FinSi
	si bil20<>0 Entonces
		Escribir bil20," billetes de 20 u$s";
	FinSi
	si bil10<>0 Entonces
		Escribir bil10," billetes de 10 u$s";
	FinSi
	si bil5<>0 Entonces
		Escribir bil5," billetes de 5 u$s";
	FinSi
	si bil1<>0 Entonces
		Escribir bil1," billetes de 1 u$s";
	FinSi
	
FinSubProceso

Proceso desglosar_en_billetes_chicos
	Definir cantidad Como Real;
	//Se pide ingresar la cantidad
	Escribir "ingrese la cantidad de dólares a desglosar en billetes de menor denominación";
	leer cantidad;
	// se llama al SubProceso 
	Escribir desglose(cantidad);
FinProceso
