
package paquete1;

import paquete2.Clase4;

public class TestDefault {
    public static void main(String[] args) {
        //Clase2 clase2 = new Clase2();
        ClasedHija2 claseH2 = new ClasedHija2();
        claseH2.atributoDefault = "Cambio desde la prueba";
        System.out.println("claseH2  atributo default = " + claseH2.atributoDefault);
        
        Clase4 clase4 = new Clase4("Publico");
        System.out.println(clase4.getAtributoPrivate());
        clase4.setAtributoPrivate("Cambio");
        System.out.println("clase4 = " + clase4.getAtributoPrivate());
    }
}
