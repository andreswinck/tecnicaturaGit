class Persona{ //clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
}

class Empleado extends Persona{ //clase hija
    constructor(nombre, apellido, departamento){
        super (nombre,apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = this.departamento;
    }
}




let persona1 = new Persona('Martin','Perez');

//get y SET de persona2 para nombre
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);


//get y SET de persona1 para apellido
console.log(persona1.apellido);
//set
persona1.apellido = 'Martinez';
//get
console.log(persona1.apellido)

//nombre y apellido cambiados de persona1
console.log(persona1.nombre+' '+persona1.apellido);


//get y SET de persona2 para nombre
let persona2 = new Persona('Carlos','Lara');
//get
console.log(persona2.nombre);
//set
persona2.nombre = 'Maria Laura';
//get con el cambio de nombre
console.log(persona2.nombre);


//get y SET de persona para apellido
//set
persona2.apellido = 'Carrizo'
//get
console.log(persona2.apellido);
//obtenemos el nombre y apellido cambiados de persona2 con Get
console.log(persona2.nombre+' '+persona2.apellido)

let empleado1 = new Empleado('Maria','Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombre)