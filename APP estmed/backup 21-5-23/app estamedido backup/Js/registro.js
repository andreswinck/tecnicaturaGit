import { createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-auth.js"
import { auth } from './firebase.js';
import { mostrarMensaje } from './mostrar-mensajes.js';
const registrarse = document.querySelector('#registro-usuario');
//console.log(registrarse);
registrarse.addEventListener('submit', async (e)=>{
    e.preventDefault()


const email = registrarse['registro-email'].value;
const password = registrarse['registro-password'].value;

//creando usuario con email y password en firebase
try{
const userCredentials = await createUserWithEmailAndPassword(auth, email, password)
console.log(userCredentials);

mostrarMensaje("bienvenido "+ userCredentials.user.email);

//Manejo de errores  
} catch (error){
//console.log(error.message);
//console.log(error.code);
if(error.code === 'auth/email-already-in-use'){
    mostrarMensaje('Correo electronico ya registrado', error);
}else if(error.code ==='auth/invalid-email'){
    mostrarMensaje('Email invalido', error);
}else if(error.code === 'auth/weak-password'){
    mostrarMensaje("La contraseña es muy debil", error)
}else if(error.code){
    mostrarMensaje('Ups algo salio mal', error)
}
}

})