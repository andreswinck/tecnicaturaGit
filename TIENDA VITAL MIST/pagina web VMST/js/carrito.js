const shopcontent = document.getElementById("shopcontent");
const verCarrito = document.getElementById("verCarrito");
const modalContainer = document.getElementById("modal-container");

let carrito = [];

productos.forEach((product) => {
    
    // creamos un DIV donde se va a mostrar el producto

    let content = document.createElement("div");
    // le asignamos una clase para poder darle estilos
    content.className = "card"; 
    // le asignamos el contenido al DIV que creamos con etiquetas HTML
    content.innerHTML = `
    <img src="${product.img.src}">     
    <h3>${product.nombre}</h3> 
    <p class="price">${product.precio}$</p>`;
    
    //agregamos el DIV al contenedor
    shopcontent.append(content);

    //agregamos un boton para comprar
    let comprar = document.createElement("button");
    comprar.innerText = "Comprar";
    comprar.className = "comprar";

    //agregamos el boton al contenedor
    content.append(comprar);

    //agregamos un evento al boton comprar
    comprar.addEventListener("click", () => {
        //agregamos el producto al carrito
        carrito.push({
            id: product.id,
            img: product.img.src,
            nombre: product.nombre,
            precio: product.precio,
        });
        console.log(carrito);
    }
    );
});

verCarrito.addEventListener("click", () => {
    //mostramos el carrito
    // console.log("aca toy!!!");
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
    
    modalHeader.append(modalbutton);

    carrito.forEach((product) => {

    // body del carrito

    let carritoContent = document.createElement("div");
    carritoContent.className = "modal-content";
    carritoContent.innerHTML = `
    <img src="${product.img}">
    <h3>${product.nombre}</h3>
    <p class="price">${product.precio}$</p> 
    `;
    
    modalContainer.append(carritoContent);



    });
     // footer del carrito
    // para el total acc es el acumulador y -el- es cada elemento
    const total = carrito.reduce((acc, el) => acc + el.precio, 0);
    const totalBuying = document.createElement("div");
    totalBuying.className = "total-content";
    totalBuying.innerHTML = `total a pagar: ${total}$`;
    modalContainer.append(totalBuying);

   


});

