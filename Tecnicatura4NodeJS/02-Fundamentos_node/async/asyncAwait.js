// la palabra async no es necesaria porque ya son asincronas
// pero es una buena practica usarla

async function hola(nombre){
    return new Promise(function(resolve, reject){
        setTimeout(function() {
            console.log('Hola '+nombre);
            resolve(nombre);
        }, 1000);
    });
}

async function hablar(nombre){
    return new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log('Bla bla bla bla...');
            resolve(nombre);
        }, 1000);
    });
}

async function adios(nombre){
    return new Promise((resolve, reject) =>{
        setTimeout(function() {
            console.log('Adios '+nombre);
            resolve();
        }, 1000);
    });
}

//await hola('Carlos'); mala sintaxis

// await solo es válido dentro de una función asíncrona
// async se puede usar sin await
// pero  await no se puede usar sin async
async function main(){
    let nombre = await hola('Carlos');
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre); 
    console.log('Terminamos el proceso');   
}

//console.log('Empezamos el proceso');
//main();
//console.log('Ésta va a ser la segunda instrucción');


// codigo en inglés

async function hello(nombre){
    return new Promise(function(resolve, reject){
        setTimeout(function() {
            console.log('Hi '+nombre);
            resolve(nombre);
        }, 1000);
    });
}

async function talk(nombre){
    return new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log('Go Go Go...');
            resolve(nombre);
        }, 1000);
    });
}

async function goodbye(nombre){
    return new Promise((resolve, reject) =>{
        setTimeout(function() {
            console.log('Bye '+nombre);
            resolve();
        }, 1000);
    });
}

async function main(){
    let nombre = await hello('Carlos');
    await talk();
    await talk();
    await talk();
    await goodbye(nombre); 
    console.log('Process finished');   
}

console.log('Starting process');
main();
console.log('This is going to be the second instruction');

