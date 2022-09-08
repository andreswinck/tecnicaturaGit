/*
Ejercicio 2: Leer un numero e indicar si es pos o neg
se repetira hasta que se introduzca 0
Luego hacerlo con JOptionpane
*/
package Ciclos02;

import java.util.Scanner;


public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite un numero:");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero> 0){
                System.out.println("El numero "+numero+" es positivo");
            }
            else{
                System.out.println("El numero "+numero+" es negativo");
            }
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
    }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
