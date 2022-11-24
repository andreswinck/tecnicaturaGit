/*
Ejercicio 3: Leer 5 numeros por teclado, almacenarlos en
un arreglo y a continuacion realizar la media de los
numeros positivos, la media de los negativos y contar el
numero de ceros.
*/
package arreglos_Ejercicio_3;

import java.util.Scanner;

public class Arreglos_ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos=0, positivos=0,mediaNegativos,mediaPositivos;
        int conteo0=0, conteo_negativos=0, conteo_positivos=0;
         
        
        System.out.println("Guardando los numeros: ");
        for (int i = 0; i < 5; i++) {
            System.out.println("Ingrese un numero: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i]>0){
                conteo_positivos ++;
                positivos +=numeros[i];
            }
            else if(numeros[i]<0){
                conteo_negativos ++;
                negativos +=numeros[i];
            }
            else{
                conteo0 ++;
            }
        }
        if (conteo_positivos ==0){
            System.out.println("\nNo se puede sacar la media de los positivos");
        }
        else{
            mediaPositivos = positivos/conteo_positivos;
            System.out.println("La media de los positivos es: " + mediaPositivos);
        }
        if (conteo_negativos ==0){
            System.out.println("\nNo se puede sacar la media de los negativos");
        }
        else{
            mediaNegativos = negativos/conteo_negativos;
            System.out.println("La media de los negativos es: " + mediaNegativos);
        }
        if (conteo0 ==0){
            System.out.println("\nNo hay ceros");
        }
        else{
            System.out.println("La cantidad de ceros es: " + conteo0);
        }
                
    }
}
