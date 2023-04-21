miFuncion(8,2) //Esto se conoce como Hoisting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;


}

//Llamamos la funcion

miFuncion(5, 4);

let resultado = miFuncion(6,7);
console.log(resultado);

//Declaramos una funcion de tipo expreseion o anonima

let x = function(a, b){ return a +b}; //Se cierran con ;
resultado = x(5,6); // al llamarla se pone la variable y ()
console.log(resultado);

//Funciones de tipo self y invocking
(function(a, b){
    console.log("Ejecutando la funcion: "+ (a + b));
})(9,6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}

miFuncionDos(5, 7, 6,8 ,9);

//tostring

var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// seguir en video 6 de la clase 3 de js

