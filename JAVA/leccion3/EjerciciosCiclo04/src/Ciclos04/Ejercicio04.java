/*
Ejercicio 4: Pedir numeros hasta que se introduzca un numero negativo
y mostrar cuantos numeros se han introducido.
Lo hacemos primero con la clase Scanner
y luego con la JOptionPane
*/
package Ciclos04;
import javax.swing.JOptionPane;
public class Ejercicio04 {
    public static void main(String[] args) {    
        var numero =Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int cantnum;
        cantnum = 0;
        while(numero >= 0){
            cantnum ++;
          
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
    }
        JOptionPane.showMessageDialog(null,"Se han introducido "+cantnum+" numeros que no son negativos");
    }
}
