// verCarrito.addEventListener("click", () => {
const pintarCarrito = () => {
    //logica del carrito
    //esto es para que no se repita el carrito cada vez que se hace click
    modalContainer.innerHTML = "";
    //esto es para que muestre el carrito cada vez que se hace click
    modalContainer.style.display = "flex";
    //creamos el header del carrito
    const modalHeader = document.createElement("div");
    modalHeader.className = "modal-header";
    modalHeader.innerHTML = `
    <h2>Carrito de compras</h2>
    `;
    
    modalContainer.append(modalHeader);
    // header del carrito
    const modalbutton = document.createElement("h1");
    modalbutton.innerText = "X";
    modalbutton.className = "modal-header-button";
    modalbutton.addEventListener("click", () => {
        modalContainer.style.display = "none";
    });
 
    modalHeader.append(modalbutton);
    
    // agrega cada producto del carrito
    carrito.forEach((product) => {
    // body del carrito
    let carritoContent = document.createElement("div");
    carritoContent.className = "modal-content";
    // le asignamos el contenido al DIV que creamos con etiquetas HTML
    // imagen, nombre y precio

    carritoContent.innerHTML = `
   
    <img src="${product.img}">
    <h3>${product.nombre}</h3>
    <p class="price">${product.precio}$</p>
    <p> Cant.: ${product.cantidad}</p>
    <p> Subt.: ${product.precio * product.cantidad}$</p>
    `;
    modalContainer.append(carritoContent);

    // boton para eliminar producto
    let eliminar = document.createElement("span");
    // eliminar.innerText = "❎";
    eliminar.innerHTML = `<i class="bi bi-trash borrarProducto"></i>`;
    eliminar.className = "delete-product";
    carritoContent.append(eliminar);
    eliminar.addEventListener("click", eliminarProducto);

    });
     // footer del carrito
    // para el total acc es el acumulador y -el- es cada elemento
    const total = carrito.reduce((acc, el) => acc + el.precio * el.cantidad, 0);
    const totalBuying = document.createElement("div");
    totalBuying.className = "total-content";
    totalBuying.innerHTML = `total a pagar: $ ${total}`;
    modalContainer.append(totalBuying);
};

verCarrito.addEventListener("click", pintarCarrito);

// boton para eliminar producto
//filtrar el carrito y eliminar el producto
const eliminarProducto = () => {
    const foundId = carrito.find((element) => element.id);

    carrito = carrito.filter((carritoId) => {
    
        return carritoId !== foundId;
});
//resta al contador del carrito
carritoCounter();
//muestra carrito actualizado
pintarCarrito();
};
//detecta cual es la cantidad de PRODUCTOS en el carrito

const carritoCounter = () => {
    cantidadCarrito.style.display = "block";
    cantidadCarrito.innerText = carrito.length;

};

