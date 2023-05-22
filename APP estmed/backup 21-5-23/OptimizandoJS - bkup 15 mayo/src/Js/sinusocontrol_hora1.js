
//Creo una nueva fecha
var fechaActual = new Date();
  //Obtengo los valores de dia,mes,año por un lado y por el otro capto hora, minutos y segundos
    //Fecha
      var dia = fechaActual.getDate();
      var mes = fechaActual.getMonth() + 1;
      var anio = fechaActual.getFullYear();
    //Hora
      var hora = fechaActual.getHours();
      var minutos = fechaActual.getMinutes();
      var segundos = fechaActual.getSeconds();

  export const ticketinicio ={
    dia:dia,
    mes:mes,
    anio:anio,
    hora:hora,
    minutos:minutos,
  }
  
    //luego en el parrafo de id "fecha" y "hora" con un inner inserto la fecha y la hora
// document.getElementById("mostrar_fecha_actual").innerHTML = "Fecha: " + dia + "/" + mes + "/" + anio;

//Funcion que muestra la hora actual de sistema
function mostrarHora() {
    const fechaActual = new Date();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes();
    const segundos = fechaActual.getSeconds();


//minutos y/o segundos MENORES<10:
    if(minutos<10){
      if(segundos<10){
        var horaMostrada = hora + ":0" + minutos + ":0" + segundos;
      }else 
      if(segundos>10){
        var horaMostrada = hora + ":0" + minutos + ":" + segundos;
      }
      }else{
        if (segundos<10){
          var horaMostrada = hora + ":" + minutos + ":0" + segundos;
        }
        else{
          var horaMostrada = hora + ":" + minutos + ":" + segundos;
        }
    }

  // document.getElementById("mostrar_hora_actual").innerHTML = "Hora Actual: "+horaMostrada;
    // document.getElementById("hora").innerHTML = "Hora Actual: "+horaMostrada;
    setInterval(mostrarHora, 1000);
  }

//mostrarHora();
//export{hora,minutos,dia,mes,anio}


