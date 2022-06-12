//Venta de Libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Ingrese el ID del libro");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el precio del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envio es gratuito: ");
        boolean envioGratis = Boolean.parseBoolean(entrada.nextLine());
        System.out.println("Libro: "+ nombreLibro +" # ID: " + idLibro);
        System.out.println("Precio del libro: $" + precioLibro);
        System.out.println("Envio gratis es: " + envioGratis);*/
        /*ejercicio triangulo*/
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite el alto del rectangulo: ");
        int alto = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el ancho del rectangulo");
        int ancho = Integer.parseInt(entrada.nextLine());
        int area = 0;
        int perimetro = 0;
        area = alto * ancho;
        perimetro = (alto + ancho) * 2;
                
        
        System.out.println("area "+ area);
        System.out.println("perimetro " + perimetro);
       
    }
}
