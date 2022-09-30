/*
Ejercicio 8 : Pedir un número N y mostrar todos los numeros
desde el 1 hasta N 
*/
package Ciclos08;

import java.util.Scanner;

public class Ciclos08 {
    public static void main(String[] args) {
            Scanner entrada = new Scanner (System.in);
            System.out.println("Ingrese un numero: ");
            int numero = Integer.parseInt(entrada.nextLine());
            
            int lista =1;
            while (lista <= numero){
                System.out.println(lista);
                lista ++;
            }
            
    }
    
}
