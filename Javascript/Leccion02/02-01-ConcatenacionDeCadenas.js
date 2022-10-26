var nombre = "José";
var apellido = " Montes";
var nombreCompleto = nombre+" "+apellido; //primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Ariel"+" "+"Betancud"; // Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //lee de izq a derecha y lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 219;
console.log(juntos);
juntos = 78 + 17 + nombre; // aqui hace la suma primero e imprime
console.log(juntos);

nombre +=apellido; //Tercera forma de concatenar
console.log(nombre)

// Hoy ya no se va a usar var, se utiliza let y constç
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2);

let x, y;  // se pueden crear varias variables en una sola linea
x = 17, y = 21;
let z = x + y;
console.log(z);
let _1run = 31;
let $break = "rompe"

console.log(_1run);
console.log($break);
