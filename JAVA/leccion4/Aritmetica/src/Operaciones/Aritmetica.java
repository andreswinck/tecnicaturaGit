
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //El constructor es un metodo especial
    public Aritmetica(){  //constructor 1 VACIO
        System.out.println("Se esta ejecutando este cosntructor numero uno");
    }
    // Estamos viendo lo que se llama sobrecaga de constructores
    public Aritmetica(int a, int b){  //COSNTRUCTOR 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    
    
    //Metodos
    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a +b;
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1;
        this.b = arg2;
        //return a + b;
        return this.sumarConRetorno();
    }
}
