//El primer import es para saber si el usuario esta logueado
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-auth.js";
//para esto el segundo import es para traer a auth
import { auth } from './firebase.js'
//aqui importamos el registro
import './registro.js';
//Ahora importamos el archivo logout.js
import './logout.js';
//importo login-form
import './login-form.js';

//esto hace que cada vez que se lanza la aplicacion se carga esta funcion que muestra los datos del usuario
onAuthStateChanged(auth, async(user)=>{
    //console.log(user);
    //Validando si el usuario esta logueado
    //if(user){

    //}else{

    //}
})