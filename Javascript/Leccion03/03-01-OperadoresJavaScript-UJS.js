// Ejercicio para encontrar numeros pares e impares
let parImpar = 7;
if(parImpar % 2 == 0 ){
    console.log("Es un numero PAR");
}
else{
    console.log("Es un numero IMPAR");
}

// Ejercicio: es mayor de edad
let edad = 18, adulto = 18;
if(edad >= adulto){
    console.log("Usted es una persona adulta");
}
else{
    console.log("Usted es una persona menor de edad");
}

//Ejercicio: Dentro de un rango
let dentroRango =15;  //aqui cambiamos el valor
let valMin = 0 , valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log("Está dentro del rango")    
}
else{
    console.log("Está fuera del rango")
}

//Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if (vacaciones || diaDescanso){
    console.log("El padre puede asistir");
}
else{
    console.log("El padre no puede asistir");
}

//Operador ternario
let resutlado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resutlado2);
let numero = 8;
resutlado2 = numero %2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resutlado2)

//Convertir String a Number
let miNumero = "18"; //es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero) //es una funcion
console.log(typeof edad2)
// funcion isNaN
if(isNaN(edad2)){  // is not a number devuelve un resultado booleano
    console.log("Esta variable no es un numero")
}
else{
    if (edad2>=18){
        console.log("Puede votar");
    }
    else{
        console.log("Es demasiado joven para votar");
    }
}

// Operador ternario
let resutlado3 = edad2 >=18 ? "Puede votar" : "Es demasiado joven para votar";
console.log(resutlado3)

//Funcion isNaN
