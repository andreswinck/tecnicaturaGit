export function mostrarMensaje(mensaje, tipo="success"){
  //toastify //Registro Exitoso
Toastify({
  text: mensaje,
  duration: 2000,
  destination: "",
  newWindow: true,
  close: true,
  gravity: "top", // `top` or `bottom`
  position: "center", // `left`, `center` or `right`
  stopOnFocus: true, // Prevents dismissing of toast on hover
  style: {
    background: tipo === "success" ? "linear-gradient(to right, #00b09b, #96c93d)" : "red"
  },
  onClick: function(){} // Callback after click
}).showToast();

}

