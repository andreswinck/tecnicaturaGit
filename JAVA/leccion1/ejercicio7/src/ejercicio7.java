
import java.util.Scanner;


public class ejercicio7 {
    /* cada empleado recibe 1000 pesos
    mas 150 por cada carro
    mas 5% del valor de cada carro
    
    */
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        final int salario = 1000;
        float cantCarros, valorCarro, salarioTotal;
                
        System.out.println("Ingrese la cantidad de carros vendidos = ");
        cantCarros = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese valor de cada carro = ");
        valorCarro = Float.parseFloat(entrada.nextLine());
        salarioTotal = salario + cantCarros * 150 + cantCarros * valorCarro * 0.05f;
        System.out.println("el salario del empleado sera de: " + salarioTotal);
                
    }
    
}
