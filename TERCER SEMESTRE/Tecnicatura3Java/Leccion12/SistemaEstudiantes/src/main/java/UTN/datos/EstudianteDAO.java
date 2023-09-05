package UTN.datos;

import UTN.dominio.Estudiante;

import static UTN.conexion.conexion.getConexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class EstudianteDAO {
    // Método listar
    public List<Estudiante> listarEstudiantes(){
        List<Estudiante> estudiantes = new ArrayList<>();
        //Creamos algunos objetos para comunicarnos con la BD
        PreparedStatement ps; //Para preparar la consulta
        ResultSet rs; //Para obtener los resultados de la consulta
        //Creamos la consulta
        Conexion con = getConexion();
        String sql = "SELECT * FROM estudiantes2022 order by idEstudiantes";
        try {
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                //Creamos un objeto estudiante
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idEstudiantes"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setEmail(rs.getString("mail"));
                estudiante.setTelefono(rs.getString("telefono"));
                //Agregamos el objeto estudiante a la lista
                estudiantes.add(estudiante);
            }
        } catch (Exception e) {
            System.err.println("Error al seleccionar datos: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.err.println("Error al cerrar la conexion: " + e.getMessage());
            }
        }//fin try-catch
        return estudiantes;
    }//fin metodo listar


    //Metodo por id ->find by id
    public boolean buscarEstudiantePorId(Estudiante estudiante){
        PreparedStatement ps; //Para preparar la consulta
        ResultSet rs; //Para obtener los resultados de la consulta
        //Creamos la consulta
        Conexion con = getConexion();
        String sql = "SELECT * FROM estudiantes2022 WHERE idEstudiantes = ?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if (rs.next()) {
                //Creamos un objeto estudiante
                estudiante.setIdEstudiante(rs.getString("idEstudiantes"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setEmail(rs.getString("mail"));
                estudiante.setTelefono(rs.getString("telefono"));
                return true; //Si se encontro el estudiante
            }// fin if
        } catch (Exception e) {
            System.err.println("Error al buscar estudiante: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.err.println("Error al cerrar la conexion: " + e.getMessage());
            }
        }//fin try-catch
        return false;
    }//fin metodo buscar por id
    }

    // Agregar estudiante
    public void agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps; //Para preparar la consulta
        Connection con = getConexion();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido, mail, telefono) VALUES (?,?,?,?)";
        ResultSet rs; //Para obtener los resultados de la consulta
        //Creamos la consulta
        Conexion con = getConexion();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido, mail, telefono) VALUES (?,?,?,?)";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getEmail());
            ps.setString(4, estudiante.getTelefono());
            ps.execute();

        } catch (Exception e) {
            System.err.println("Error al agregar estudiante: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.err.println("Error al cerrar la conexion: " + e.getMessage());
            }
        }//fin try-catch
    }//fin metodo agregar estudiante

    // Modificar un estudiante
    public void modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps; //Para preparar la consulta
        Connection con = getConexion();
        String sql = "UPDATE estudiantes2022 SET nombre = ?, apellido = ?, mail = ?, telefono = ? WHERE idEstudiantes = ?";

        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getEmail());
            ps.setString(4, estudiante.getTelefono());
            ps.setInt(5, estudiante.getIdEstudiante());
            ps.execute();
        } catch (Exception e) {
            System.err.println("Error al modificar estudiante: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.err.println("Error al cerrar la conexion: " + e.getMessage());
            }
        }//fin try-catch
        return false;
    }//fin metodo modificar estudiante

    // Eliminar un estudiante
    public void eliminarEstudiante(Estudiante estudiante){
        PreparedStatement ps; //Para preparar la consulta
        Connection con = getConexion();
        String sql = "DELETE FROM estudiantes2022 WHERE idEstudiantes = ?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            ps.execute();
            return true;
        } catch (Exception e) {
            System.err.println("Error al eliminar estudiante: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.err.println("Error al cerrar la conexion: " + e.getMessage());
            }
        }//fin try-catch
        return false;
    }//fin metodo eliminar estudiante

    public static void main(String[] args) {
        var estudianteDAO = new EstudianteDAO();
        //Modificar un estudiante
        var estudianteModificado = new Estudiante(1, "Juan", "Carlos", "946542323", "juan@mail.com")
        var modificado = estudianteDAO.modificarEstudiante(estudianteModificado);
        if(modificado)
            System.out.println("Estudiante modificado: "+estudianteModificado);
        else
            System.out.println("No se modificó el estudiante: "+estudianteModificado);

        //Agregar un estudiante
        var nuevoEstudiante = new Estudiante("Carlos", "Lara", "346542323", "carlosl@mail.com");
        var agregado = estudianteDAO.agregarEstudiante(nuevoEstudiante);
        if(agregado)
            System.out.println("Estudiante agregado: "+nuevoEstudiante);
        else
            System.out.println("Estudiante no agregado: "+nuevoEstudiante);


        //Listar los estudiantes
        System.out.println("Listado de estudiantes");
        List<Estudiante> estudiantes = estudianteDAO.listarEstudiantes();
        estudiantes.forEach(System.out::println); //funcion lambda para imprimir

        //Buscar estudiante por id
        var estudiante = new Estudiante();
        System.out.println("Estudiantes antes de la busqueda: "+estudiante1);
        var encontrado = estudianteDAO.buscarEstudiantePorId(estudiante1);
        if(encontrado)
            System.out.println("Estudiante encontrado: "+estudiante1);
        else
            System.out.println("Estudiante no encontrado: "+estudiante1.getIdEstudiante());
    }
}


