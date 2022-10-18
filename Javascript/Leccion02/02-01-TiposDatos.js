// Tipos de Datos en JS
/*
comentario de varias lineas similar a Java
*/
//tipo Str
var nombre = "Ariel"; 
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre)
nombre = 12.3;
console.log(typeof nombre);

//Tipo numerico
var numero = 3000; 
console.log(numero);
//tipo objeto
var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893"
}

console.log(typeof objeto);

//Tipo de dato BOOLEAN
var bandera = true;
console.log(bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion)

//Tipo de dato SYMBOL
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

// Tipo de dato clase pero es tipo FUNCION
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

}

console.log(typeof Persona);

// Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//nul: significa ausencia de valor
var y = null; // null no es un tipo de dato pero su origen es de tipo OBJECT
console.log(typeof y);

//Tipo de dato array [] y Empty String
var autos = ['Citroen','Audi','BMW','Ford']
console.log(autos);
console.log(typeof autos); // preguntamos que tipo de dato es->>

var z='';
console.log(z);// Esto se refiere a una cadena vacia
console.log(typeof z);






