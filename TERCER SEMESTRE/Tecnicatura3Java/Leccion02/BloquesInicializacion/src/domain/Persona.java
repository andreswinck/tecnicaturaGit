
package domain;


public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static { //Bloque de inicializacion estatico
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersonas;
    }
    
    {// Bloque de inicializacion NO ESTATICO (contexto dinamico) solo con abrir las llaves 
        System.out.println("Ejecucion del bloque No Estatico");
        this.idPersona = Persona.contadorPersonas++; // Incrementamos el atributo
    }
    
    // Los bloques de inicializacion se ejecutan ANTES del constructor
    
    public Persona(){
        System.out.println("Ejecucion del constructo");
    }
    
    public int idPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
   
}
