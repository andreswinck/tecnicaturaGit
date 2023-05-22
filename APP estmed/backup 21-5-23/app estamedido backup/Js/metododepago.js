// storage.clear();
var fechaguardada = localStorage.getItem('cpagofecha')
var datosfechaguardada = JSON.parse(fechaguardada);
hora_inicial_estacionamiento = localStorage.getItem("cpagohoraInicio");
minutos_inicial_estacionamiento = localStorage.getItem("cpagominutosInicio");
hora_final_estacionamiento = localStorage.getItem("cpagohoraFinaliza");
minutos_final_estacionamiento = localStorage.getItem("cpagominutosFinaliza");
monto_a_pagar = localStorage.getItem("cpagotiempoContrato");
document.getElementById('fecha_contratada').innerHTML = datosfechaguardada.cpagodia+ " / "+(datosfechaguardada.cpagomes+1) +" / "+datosfechaguardada.cpagoanio;
document.getElementById('hora_inicio').innerHTML = hora_inicial_estacionamiento +":"+  minutos_inicial_estacionamiento;
document.getElementById('hora_finaliza').innerHTML = hora_final_estacionamiento +":" +  minutos_final_estacionamiento;
document.getElementById('monto_total').innerHTML = monto_a_pagar/15*25;



// storage.clear();
/*
// Obtener los datos de LocalStorage
var datosGuardados = localStorage.getItem("datos");

// Convertir el string JSON a objeto
var datos = JSON.parse(datosGuardados);

// Acceder a los valores del objeto
console.log(datos.nombre); // "Andres"
console.log(datos.edad); // 25
console.log(datos.email); // "andres@example.com"
*/