/*
Usos de Final
Variables: Evita cambiar el valor de la variable
Metodos: Evita que se modifique la def o el comportamiento de un metodo desde una clase hija
clases: Evita que se creen clases hijas
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39554843;
        System.out.println("miDni = " + miDni);
        // miDni = 4533453456; no se puede modificar
        //Persona.CONSTANTE_AQUI = 9; no se puede modificar
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);  
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); no se puede asignar una nueva referencia
        
        persona1.setNombre("Ariel Betancud");
        System.out.println("Persona1 nombre: " + persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("Persona1 nombre: " + persona1.getNombre());
    }
    
}

