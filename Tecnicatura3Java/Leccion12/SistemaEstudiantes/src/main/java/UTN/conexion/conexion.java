package UTN.conexion;

import java.sql.Connection;
import java.sql.SQLException;

public class conexion {
    public static Connection getConexion() {
        Connection conexion = null;
        //Variables de conexion
        var baseDatos = "estudiantes2022";
        var url = "jdbc:mysql://localhost:3306/" + baseDatos;
        var usuario = "root";
        var password = "admin";

        // cargamos la clase del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = java.sql.DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException  | SQLException e) {
            System.out.println("Error al conectar a la base de datos" + e.getMessage());
        }//fin try-catch
        return conexion;
    }//fin metodo Conexion
}
