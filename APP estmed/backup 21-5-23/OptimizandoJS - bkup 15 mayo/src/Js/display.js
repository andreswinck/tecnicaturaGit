//import {hora,minutos} from "./control_hora.js";

//Con esto obtenemos el dominio
// const dominio = document.querySelector('control-dominio');
// console.log(dominio)

var sumarTiempo = 0;
//Obtenemos los botones Sumar y Restar tiempo
var sumarTiempo = document.getElementById('boton_sumar_tiempo');
var restarTiempo = document.getElementById('boton_restar_tiempo');
//Periodo establecido para el tiempo minimo de estacionamiento
let tiempoContrato = 0;
let costo = 25
let horafinal = 0;
let minutosfinal = 0;
let montofinal = 0;
var tiempoContrato2 = 0;
//let hora_finaliza_periodo = 0;

//Colocamos un escucha en el boton sumarTiempo o restarTiempo

//export const btn_suma = sumarTiempo.addEventListener("click", sumarTiempoDisplay);

    // const btn = document.getElementById('btn');

    // console.log(btn);

sumarTiempo.onclick = sumarTiempoDisplay
    // sumarTiempo.addEventListener('click', (event) => {
    //     event.
    //     sumarTiempoDisplay();
    // });
restarTiempo.onclick = restarTiempoDisplay
// restarTiempo.addEventListener("click", restarTiempoDisplay);

//Funcion que suma el tiempo
function sumarTiempoDisplay(){
    if(tiempoContrato === 240){
        pantalla_total_tiempo.innerHTML = tiempoContrato;
    }else{
        tiempoContrato += 15;
        pantalla_total_tiempo.innerHTML = tiempoContrato;
    }

    //muestra HOR FINALIZACION
    var suma_tiempo =  tiempoContrato+minutos
    // console.log('min inicial: '+ minutos + ' tiempo cont: ' + tiempoContrato + ' suma: '+suma_tiempo);
    var hour = hora +Math.trunc(suma_tiempo / 60);
    // console.log('hour= '+(suma_tiempo/60)+'hour '+hour);
    hour = (hour < 10)? '0' + hour : hour;
    var minute = suma_tiempo % 60;
    // console.log('minute'+minute);
    minute = (minute < 10)? '0' + minute : minute;
    horafinalizacion.innerHTML= hour + ':' + minute
    monto_a_pagar.innerHTML = (tiempoContrato/15*costo)
    var montofinal = (tiempoContrato/15*costo)
    var horafinal = hour
    var minutosfinal = minute
    var tiempoContrato2 = tiempoContrato
return tiempoContrato2
//return (horafinal, minutosfinal, montofinal)
}
//Funcion que resta el tiempo
function restarTiempoDisplay(){
    if(tiempoContrato === 15){
        pantalla_total_tiempo.innerHTML = tiempoContrato;
    }else{
        tiempoContrato -= 15;
        pantalla_total_tiempo.innerHTML = tiempoContrato;
    }
        //muestra HOR FINALIZACION
        var suma_tiempo =  tiempoContrato+minutos
        var hour = hora + Math.trunc(suma_tiempo / 60);
        hour = (hour < 10)? '0' + hour : hour;
        var minute = suma_tiempo % 60;
        minute = (minute < 10)? '0' + minute : minute;
        horafinalizacion.innerHTML=hour + ':' + minute
        monto_a_pagar.innerHTML = (tiempoContrato/15*costo)
        var montofinal = (tiempoContrato/15*costo)
        var horafinal = hour
        var minutosfinal = minute
        var tiempoContrato2 = tiempoContrato
//return horafinal,minutosfinal,montofinal
return tiempoContrato
}
export var periodocontratado = tiempoContrato2
// export {periodocontratado}
// export const ticketfinal ={
//     horafinal:horafinal,
//     minutosfinal:minutosfinal,
//     montofinal:montofinal
// };
// aceptar_periodo.addEventListener("click",cargar_ticket);
// aceptar_periodo.onclick = cargar_ticket
// function cargar_ticket(){
    // restarTiempo.removeEventListener("click", restarTiempoDisplay);
    // sumarTiempo.removeEventListener('click', sumarTiempoDisplay);
//     location.href = "ticket.html";

// }