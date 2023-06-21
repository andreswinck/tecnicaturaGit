import java.util.Scanner;
public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true){
            System.out.println("****** Aplicación Calculadora ******");
            mostrarMenu();

            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {

                    ejecutarOperacion(operacion, entrada);


                } else if (operacion == 5) {
                    System.out.println("Gracias por utilizar la aplicación");
                    break; // rompemos el ciclo while
                } else {
                    System.out.println("La opción ingresada no es válida: " + operacion);
                } // fin del if-else
                System.out.println("Presione ENTER para continuar");
                
            } catch (Exception e) {
                System.out.println("Ocurrió un Error: " + e.getMessage());
                System.out.println();
            } // fin del try-catch
            
        } // fin del while

    } // fin del método main

    private static void mostrarMenu(){
        System.out.println("Menú de opciones");
        System.out.println("""
                1. Sumar
                2. Restar
                3. Multiplicar
                4. Dividir
                5. Salir""");
        System.out.print("Ingrese la opción deseada: ");
    } // fin del método mostrarMenu

    private static void ejecutarOperacion(int operacion, Scanner entrada){
        Double resultado;
        System.out.print("Ingrese el primer operando: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Ingrese el segundo operando: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        switch (operacion) {
            case 1 -> {resultado = operando1 + operando2;
                System.out.println("El resultado de la operación es: " + resultado);
            }
            case 2 -> {resultado = operando1 - operando2;
                System.out.println("El resultado de la operación es: " + resultado);
            }
            case 3 -> {resultado = operando1 * operando2;
                System.out.println("El resultado de la operación es: " + resultado);
            }
            case 4 -> {
                resultado = operando1 / operando2;
                System.out.println("El resultado de la operación es: " + resultado);
            }
        } // fin del switch
    } // fin del método ejecutarOperacion


} // fin de la clase CalculadoraUTN

