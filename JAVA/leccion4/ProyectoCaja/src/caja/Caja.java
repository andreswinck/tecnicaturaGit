package caja; //Package

public class Caja { //Clase publica caja
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Métodos y constructores (acciones)
    public Caja(){ //constructor 1 = vacío
}
    // constructor con parámetros
    public Caja(int ancho, int alto, int profundo){ //constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    public int calcularVolumen(){ //Método para calcular
        return ancho * alto * profundo;
    }
        
    }
     
