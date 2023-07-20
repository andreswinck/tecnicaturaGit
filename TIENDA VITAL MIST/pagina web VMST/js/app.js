const shopcontent = document.getElementById("shopcontent");
const verCarrito = document.getElementById("verCarrito");
const modalContainer = document.getElementById("modal-container");
const cantidadCarrito = document.getElementById("cantidadCarrito");

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
        //si se repite el producto, aumenta la cantidad
        //si no se repite, lo agrega al carrito
        // usando el metodo some() para saber si el producto se repite
        
        const repeat = carrito.some((repeatProduct) => repeatProduct.id === product.id);

        if (repeat) {
            carrito.map((prod) => {
                if (prod.id === product.id) {
                    prod.cantidad++;
                }
            })
            } else {

  
            carrito.push({
                id: product.id,
                img: product.img.src,
                nombre: product.nombre,
                precio: product.precio,
                cantidad: product.cantidad,

        });
        }
        console.log(carrito);
        carritoCounter();
    }
    );
});



