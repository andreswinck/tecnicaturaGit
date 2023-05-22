// variables de los botones ACEPTARsumar y restar tiempo
//los botones se uliizan con el id="" de cada uno
let sumarTiempo = document.getElementById("boton_sumar_tiempo");
let restarTiempo = document.getElementById("boton_restar_tiempo");
//periodo que se suma o resta con cada boton
let tiempocontrato = 15;

// llamo a las funciones sumar o restar al hacer CLICK en el boton
sumarTiempo.addEventListener("click",funcion_sumar_tiempo);
restarTiempo.addEventListener("click",funcion_restar_tiempo);

function funcion_sumar_tiempo(){
    if (tiempocontrato==240){
        recuadro_total_tiempo.innerHTML = tiempocontrato;  
    }
    else{
        tiempocontrato =tiempocontrato + 15;
        recuadro_total_tiempo.innerHTML = tiempocontrato;
    }
            
        }



function funcion_restar_tiempo(){

        if (tiempocontrato==15){
            recuadro_total_tiempo.innerHTML = tiempocontrato;  
        }
        else{
            tiempocontrato =tiempocontrato - 15;
            recuadro_total_tiempo.innerHTML = tiempocontrato;
        }

    }

// reloj
function startTime(){
    today=new Date();
    dia=today.getDate();
    mes=today.getMonth();
    anio=today.getFullYear();
    h=today.getHours();
    m=today.getMinutes();
    s=today.getSeconds();
    m=checkTime(m);
    s=checkTime(s);
    mfinal=today.getMinutes() + tiempocontrato;
    hfinal= h;

    if(mfinal>59){

    hfinal=h+Math.trunc(mfinal/60)
    mfinal=(((mfinal/60)-Math.trunc(mfinal/60))*60).toFixed()

    }
    document.getElementById('reloj').innerHTML="Hora "+h+":"+m+":"+s;
    document.getElementById('fecha').innerHTML=" Fecha: "+dia+" / "+ (mes+1) + " / "+anio;
    if (mfinal<10){
        document.getElementById('horafinalizacion').innerHTML=hfinal +":0"+ mfinal;
    }
    else{
        document.getElementById('horafinalizacion').innerHTML=hfinal +":"+ mfinal;
    }
    document.getElementById('monto_a_pagar').innerHTML="$" + (tiempocontrato)/15*25
    t=setTimeout('startTime()',500);
    }

function checkTime(i){
    if (i<10) {i="0" + i;}return i;}
    window.onload=function(){startTime();
    }

    aceptar_periodo.addEventListener("click",datosFinales);
function datosFinales(){
    const hora_inicio_esta = h;
    const minutos_inico_esta = m;
    const hora_final_esta = hfinal;
    const minuto_final_esta = mfinal;
    // document.getElementById('tomo_datos_finales').innerHTML ="Día "+ dia +"/"+(mes+1)+"/"+anio +" hora inicio período: "+hora_inicio_esta + ":"+ m + "- hora final período: " + hora_final_esta +":"+ minuto_final_esta;  
    
// guardando en JSON la fecha
    var cpagofecha = {
        cpagodia:dia,
        cpagomes:mes,
        cpagoanio:anio
    };
    localStorage.setItem("cpagofecha", JSON.stringify(cpagofecha));
    localStorage.setItem('cpagohoraInicio', hora_inicio_esta);
    localStorage.setItem('cpagominutosInicio',m);
    localStorage.setItem('cpagohoraFinaliza', hora_final_esta);
    localStorage.setItem('cpagominutosFinaliza',minuto_final_esta);
    localStorage.setItem('cpagotiempoContrato',tiempocontrato);
    


    // location.href = "ticket.html";
}

// export function datosFinales();