/*
Ejecicio 9: Pedir dia, mes y año de una fecha e
indicar si la fecha es correcta. Suponiendo que todos
los meses tienen 30 dias
*/
package Ciclos09;

import javax.swing.JOptionPane;


public class Ejercicio09 {
    public static void main(String[] args) {
        var dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día: "));
        var mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
        var anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));
        if ((dia !=0)&&(dia<=30)){
            if ((mes !=0)&&(mes<=12)){
                if ((anio !=0)&&(dia<=2022)){
                    JOptionPane.showMessageDialog(null,"La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null,"Año incorrecto");
                }
            }
                else{
                    JOptionPane.showMessageDialog(null,"Mes incorrecto");
                }
    }
                else{
                    JOptionPane.showMessageDialog(null,"Dia incorrecto");
                }
    }
}
