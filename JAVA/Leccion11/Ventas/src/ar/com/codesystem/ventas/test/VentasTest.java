
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Pollera", 2900.00);
        Producto producto4 = new Producto("Remera Hombre", 5900.00);
        Producto producto5 = new Producto("Campera Mujer", 39900.00);
        Producto producto6 = new Producto("Remera Mujer", 1900.00);
        Producto producto7 = new Producto("Calzoncillo Boxer", 3100.00);
        Producto producto8 = new Producto("Bombacha", 1900.00);
        Producto producto9 = new Producto("Camisa Hombre", 5900.00);
        Producto producto10 = new Producto("Bluza", 4900.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto7);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto6);
        orden3.mostrarOrden();
        
        //Tarea: 
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden =  2
        
        
        
    }
}
