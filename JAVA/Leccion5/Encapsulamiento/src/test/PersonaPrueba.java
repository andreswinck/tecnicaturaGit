
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
        //Modificar a través de los métodos
        
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre ="Juan Ignacio"; ya no se puede utilizar por el encapsulamiento
        //System.out.println("persona1 = " + persona1.nombre);
        
        // se muestra el resultado con el nombre modificado
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 el booleano es: "+persona1.isEliminado());
        
        //Tarea Crear un objeto de tipo Persona, asignar valores de manera inicial
        //e imprimir, luego modificar sus valores y volver a imprimir
        
        //creamos persona2 y mostramos los datos
        Persona persona2 = new Persona("Jorge",100000, false);
        System.out.println("persona2 tiene por nombre: "+persona2.getNombre());
        System.out.println("persona2 tiene por sueldo: "+persona2.getSueldo());
        System.out.println("persona2 tiene por bool: "+persona2.isEliminado());
    
        //Modificamos los datos
        persona2.setNombre("Carlitos");
        persona2.setSueldo(105000);
        persona2.setEliminado(true);
        //Mostramos las modificaciones
        System.out.println("El nombre modificado de persona2 es: "+persona2.getNombre());
        System.out.println("El sueldo midificado de persona2 quedó en: "+persona2.getSueldo());
        System.out.println("El boolenano cambio a: "+persona2.isEliminado());
    
    
    }
}
