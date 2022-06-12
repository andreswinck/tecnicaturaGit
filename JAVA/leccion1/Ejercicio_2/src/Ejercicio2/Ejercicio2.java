
package Ejercicio2;

import java.util.Scanner;


public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int horasSemanales;
        float salarioHora, salarioTotal;
        
        System.out.println("Digite horas semanales: ");
        horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite salario por hora: ");
        salarioHora = Float.parseFloat(entrada.nextLine());
        
        salarioTotal = horasSemanales * salarioHora;
        System.out.println("\nEl salario semanal es U$S"+salarioTotal);
         
    }
}
