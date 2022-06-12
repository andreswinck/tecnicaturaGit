
import java.util.Scanner;
/* Guille tiene N dolares
    Luis tiene la mitad de Guillermo
    Juan tiene la mitad de lo que tienen Luis y Guillermo juntos
    -- imprimir el total que tienen los tres ---    
*/

public class ejercicio6 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        float cantGuille , cantLuis, cantJuan, cantotal;
        System.out.println("Ingrese la cantidad de dolares que tiene Guilermo: ");
        cantGuille = Float.parseFloat(entrada.nextLine());
        cantLuis = cantGuille/2;
        cantJuan = (cantGuille + cantLuis)/2;
        cantotal = cantGuille + cantJuan + cantLuis;
        System.out.println("la cantidad de dolares de Luis es de: " + cantLuis);
        System.out.println("la cantidad de dolares de Juan es de: " + cantJuan);
        System.out.println("\nEl total de los 3 es de: " + cantotal);        
        
    }
}
