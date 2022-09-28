/*
Ejercicio 6: Pedir numeros hasta que se tecle un cero, mostrar
la suma de todos los numeros introducidos.
*/
package Ciclos06;

import javax.swing.JOptionPane;

public class Ejercicio06 {
    public static void main(String[] args) {
        int numero,suma = 0;
    do{
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        suma +=numero;
    }while (numero !=0);
    JOptionPane.showMessageDialog(null,"\nLa suma de todos los numeros ingresados es: "+suma);
    }
    }
    
