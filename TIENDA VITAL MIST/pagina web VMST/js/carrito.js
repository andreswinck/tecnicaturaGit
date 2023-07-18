const shopcontent = document.getElementById("shopcontent");

const productos = [
    {   id: 1,
        nombre: "Producto 1",
        precio: 100,
        img: {
            src:"/fotos/FOTOS PARA USAR/frasco1.png",
        }
    },

    {   id: 2,
        nombre: "Producto 2",
        precio: 200,
        img: {
            src:"/fotos/FOTOS PARA USAR/frasco2.png",
        }
    },
    {   id: 3,
        nombre: "Producto 3",
        precio: 300,
        img: {
            src:"/fotos/FOTOS PARA USAR/frasco3.png",
        }
    },
    {   id: 4,
        nombre: "Producto 4",
        precio: 400,
        img: {
            src:"/fotos/FOTOS PARA USAR/frasco4.png",
        }
    },
];

let carrito = [];

productos.forEach((product) => {
    let content = document.createElement("div");
    content.innerHTML = `<img src="${product.img.src}"> <h3>${product.nombre}</h3> <p>${product.precio}$</p>`;
    shopcontent.append(content);

});





