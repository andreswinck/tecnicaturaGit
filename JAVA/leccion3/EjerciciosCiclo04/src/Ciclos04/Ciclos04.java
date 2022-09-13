/*
Ejercicio 4: Pedir numeros hasta que se introduzca un numero negativo
y mostrar cuantos numeros se han introducido.
Lo hacemos primero con la clase Scanner
y luego con la JOptionPane
*/
package Ciclos04;
import java.util.Scanner;
public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite un numero:");
        var numero = Integer.parseInt(entrada.nextLine());
        int cantnum;
        cantnum = 0;
        while(numero >= 0){
            cantnum ++;

            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
    }
        System.out.println("El numero "+numero+" finaliza el programa");
        System.out.println("se han introducido "+cantnum+" numeros que no son negativos");
    }
}
