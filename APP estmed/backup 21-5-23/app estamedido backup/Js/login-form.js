//importamos desde firebase
import { signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-auth.js"
//Traemos el auth del archivo firebase 
import { auth } from './firebase.js';
//traigo los toasty
import { mostrarMensaje } from './mostrar-mensajes.js';

const login = document.querySelector('#form-login');

login.addEventListener('submit', async (e) => {
    e.preventDefault()

const email = login['email-login'].value;
const password = login['password-login'].value;

try {
const credentials = await signInWithEmailAndPassword(auth, email, password);
console.log(credentials);
mostrarMensaje("bienvenido "+ credentials.user.email);
window.location.replace("http://127.0.0.1:5500/Registro.html");
} catch (error) {
console.log(error);
if(error.code === 'auth/wrong-password'){
    mostrarMensaje('Password incorrecto', error);
}else if(error.code ==='auth/user-not-found'){
    mostrarMensaje('Usuario no encontrado', error);
}else {
    mostrarMensaje('Ups algo salio mal', error)
}
}

})