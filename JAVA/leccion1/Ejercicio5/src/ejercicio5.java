
import java.util.Scanner;


public class ejercicio5 {
    public static void main(String[] args) {
        /*Sumar tres calificaciones*/
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese la primera nota ");
        Float nota1 = Float.parseFloat(entrada.nextLine());
        System.out.println("Ingrese la segunda nota: ");
        Float nota2 = Float.parseFloat(entrada.nextLine());
        System.out.println("Ingrese la tercera nota: ");
        Float nota3 = Float.parseFloat(entrada.nextLine());
        System.out.println("\nLa suma de las notas es: " + (nota1 + nota2 + nota3));
                      
    }
}
