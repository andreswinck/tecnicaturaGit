
package test;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        /*
                Clases envolventes de tipos primitivos
                int = La clase envolvente es Integer
                Long - Float - Double - Boolean - Byte - Short - Character
        */
        
      int enteroPrim = 10;  // Tipo primitivo
      System.out.println("enteroPrim = " + enteroPrim);
      Integer entero = 10; //Tipo object con la clase Integer
      System.out.println("entero = " + entero.doubleValue());
      
      int entero2 = entero;  // Unboxing
        System.out.println("entero2 = " + entero2);
      
      
    }
}
