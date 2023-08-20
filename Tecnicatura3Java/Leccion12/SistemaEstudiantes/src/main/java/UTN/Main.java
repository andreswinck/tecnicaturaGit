package UTN;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        var conexion = UTN.conexion.conexion.getConexion();
        if (conexion != null) {
            System.out.println("Conectado a la base de datos" + conexion);
        } else {
            System.out.println("No se pudo conectar a la base de datos");
        }
    }// fin metodo main

}// fin clase Main