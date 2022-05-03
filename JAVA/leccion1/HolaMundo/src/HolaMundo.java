
import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola mundo desde Java");
       
       int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos Creciendo";
        System.out.println(miVariableCadena);
        // SCANNER
        Scanner scanner = new Scanner(System.in);
        System.out.println("proporciona el Titulo: ");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el Autor: ");
        String autor = scanner.nextLine();
        System.out.println(titulo + " fue escrito por " + autor);
*/

    }
}
