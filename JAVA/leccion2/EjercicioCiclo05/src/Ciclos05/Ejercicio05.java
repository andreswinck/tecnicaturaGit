/*
Ejercicio 5: Realizar un juego para adivinar un número
para ello genera un número aleatorio entre 0 y 100 y
luego ir pidiendo números indicando "es mayor" o "es menor"
respecto a N
El proceso termina cdo se acierta y se muestra el número
de intentos realizados.
*/
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // Genera número aleatorio
        
        do{

            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null,"Felicidades Acertaste el numero");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste el numero en: " +conteo+ " intentos");

    }
    }
