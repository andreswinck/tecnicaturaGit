/*
Ejercicio 8 : Pedir un número N y mostrar todos los numeros
desde el 1 hasta N 
*/
package Ciclos08;

import javax.swing.JOptionPane;


public class Ejercicio08 {
    public static void main(String[] args) {
            var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            int lista =1;
            while (lista <= numero){
                JOptionPane.showMessageDialog(null, lista);
                lista ++;

            }
    }
}
