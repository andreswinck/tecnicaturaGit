let x = 10;
console.log(x.length);
console.log('tipos primitivos');
//objeto
let persona ={
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail',
    edad: 30,
    nombreCompleto: function(){ //metodo o funcion
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

console.log('Ejecutando con un objeto');
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '260456782';
//como objeto
console.log(persona2.telefono);
console.log('creamos un nuevo objeto');
// como arreglo
console.log(persona['apellido']); //accedemos como si fuera un arreglo

//for in para recorrer la persona
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad])
}
console.log('cambiamos y eliminamos una propiedad');
persona.apellido ='Beta'; //cambiamos dinamicamente el valor
console.log(persona);
console.log(persona.apellido);
console.log('agregamos apellida')
persona.apellida = 'juarez';  //agregamos una propiedad
console.log(persona);
console.log(persona.apellida)
console.log('eliminamos apellida')
delete persona.apellida; //borramos la propiedad
console.log(persona);
console.log(persona.apellida) //desaparacio apellida

// Formas de imprimir un objeto 
//numero 1: concatenando
console.log('Formas de imprimir un objeto')
console.log('concatenando')
console.log(persona.nombre+', '+persona.apellido)


//numero 2: Ciclo for in
console.log('Ciclo for in')
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//numero 3: La funcion Object.values() lo regresa como un arreglo
console.log('array')
let personaArray = Object.values(persona);
console.log(personaArray);

//numero 4: Utilizamos Json
console.log(' Utilizamos Json')
let personaString = JSON.stringify(persona);
console.log(persona)
