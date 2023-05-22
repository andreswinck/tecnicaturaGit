//importo cerrar secion desde firebase, este signout nos permite desloguear completamente
import { signOut } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-auth.js";
//importamos el auth
import { auth } from './firebase.js';
//llamamos al boton logout
const logout = document.querySelector('#logout');
//Añadimos una escucha para cuando le hagan clik
logout.addEventListener('click', async ()=>{
    //console.log('Logout');
    await signOut(auth);
    console.log('Deslogeado con exito');
});
