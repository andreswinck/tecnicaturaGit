import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        var salir = false;
        while (!salir) {
            mostrarMenu();
            try {
                salir = ejecutarOperacion(entrada, personas);
            }catch (Exception e){
                System.out.println("Ocurrió un Error: " + e.getMessage());
            }
            System.out.println();
        } // fin while
    } // fin main

    private static void mostrarMenu() {
        System.out.println("1. Agregar persona");
        System.out.println("2. Listar personas");
        System.out.println("3. Salir");
        System.out.print("Ingrese una opción: ");
    } // fin mostrarMenu

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = entrada.nextInt();
        var salir = false;
        switch (opcion) {
            case 1 -> {
                System.out.print("Ingrese el nombre: ");
                var nombre = entrada.next();
                System.out.print("Ingrese el teléfono: ");
                var tel = entrada.next();
                System.out.print("Ingrese el email: ");
                var email = entrada.next();
                // creamos el objeto persona
                var persona = new Persona(nombre, tel, email);
                // agregamos el objeto persona a la lista
                personas.add(persona);
                System.out.println("La lista tiene: " + personas.size() + " elementos");
            } // fin case 1
            case 2 -> {
                System.out.println("Listado de personas");
                // Mejoras con lambda y el método de referencia
                //personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);

            } // fin case 2
            case 3 -> {
                System.out.println("Gracias por usar el programa");
                salir = true;
            } // fin case 3
            default -> System.out.println("Opción no válida");
        } // fin switch
        return salir;
    } // fin ejecutarOperacion
}// Fin de la clase ListadoPersonasApp

