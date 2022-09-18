/*
Ejercicio 5: Realizar un juego para adivinar un número
para ello genera un número aleatorio entre 0 y 100 y
luego ir pidiendo números indicando "es mayor" o "es menor"
respecto a N
El proceso termina cdo se acierta y se muestra el número
de intentos realizados.
*/
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada= new Scanner (System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // Genera número aleatorio
        
        do{
            System.out.println("Digite un numero"); 
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("Felicidades Acertaste el numero");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: " +conteo+ " intentos");
    }
   
           
}
