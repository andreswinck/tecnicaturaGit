
package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el numero de mes");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion desconocida";
        switch (mes){
            case 1, 2, 3 -> estacion ="VERANO";
            case 4,5,6 -> estacion = "OTONIO";
            case 7,8,9 -> estacion = "INVIERNO";
            case 10,11,12 -> estacion ="PRIMAVERA";
        }
        System.out.println("estacion = " + estacion);
                
            
    }
    }
