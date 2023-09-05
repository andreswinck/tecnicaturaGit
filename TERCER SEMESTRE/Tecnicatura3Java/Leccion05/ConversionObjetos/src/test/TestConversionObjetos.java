
package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan" , 5000, TipoEscritura.CLASICO);
        //System.out.println("empleado = " + empleado);
        System.out.println(empleado.obtenerDetalles()); //Si queremos acceder a métodos Escritor
        //Downcasting
        //((Escritor)empleado).getTipoEscritura(); // Tenemos 2 opciones: esta es una
        //escritor.gettipoEscritura();
        
        //Upcasting
        //Empleado empleado2=escritor;
        //System.out.println(empleado2.obtenerDetalles());
        
    }
}
