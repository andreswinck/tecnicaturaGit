import UTN.EstudianteDAO;
import UTN.dominio.Estudiante;
import java.util.Scanner;

public class SistemaEstudiantesApp {
    public static void main(String[] args) {
        var Salir = false;
        var consola = new Scanner(System.in);
        //Se crea una instancia de la clase servicio, esto lo hacemos fuera del ciclo
        var estudianteDao = new EstudianteDAO();//Esta instancia debe hacerse una vez
        while (!salir){
            try{
                mostrarMenu();//mostar el menu
                //Este será el método ejecutarOpciones que devolverá un booleano
                salir = ejecutarOpciones(consola, estudianteDao);//arroja excepcion
            }catch (Exception e){
                System.err.println("Error al ejecutar la operaciónn: " + e.getMessage());
            }
        }//fin while
    }// fin Main

    private static void mostrarMenu() {
        System.out.println("""
                SISTEMA DE ESTUDIANTES
                1. Listar estudiantes
                2. Buscar estudiante
                3. Agregar estudiante
                4. Modificar estudiante
                5. Eliminar estudiante
                6. Salir
                Ingrese una opción:
                """);
    }
//Método para ejecutar las opciones, va a regresar un valor booleano, ya qe es el que
    //nos va a indicar si el usuario quiere salir o no
    private static boolean ejecutarOpciones(Scanner consola, EstudianteDAO estudianteDao) {
        var opcion = Integer.parseInt(consola.nextLine());
        var salir = false;
        switch (opcion){
            case 1:
                //Listar estudiantes
                System.out.println("Listado de estudiantes");
                //no muestra la informacion, solo recupera la info y regresa una lista
                var estudiantes = estudianteDao.listarEstudiantes();//recupera la info
                //vamos a iterar cada objeto de tipo estudiante
                estudiantes.forEach(System.out::println);//imprime la info
            case 2:
                //Buscar estudiante
                System.out.println("Ingrese el id del estudiante a buscar: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var encontrado = estudianteDao.buscarEstudiantePorId(estudiante));
                if(encontrado)
                    System.out.println("Estudiante encontrado: " + estudiante);
                else
                    System.out.println("Estudiante no encontrado: " + estudiante);
            case 3:
                //Agregar estudiante
                System.out.println("Agregar estudiante");
                System.out.println("Ingrese el nombre del estudiante: ");
                var nombre = consola.nextLine();
                System.out.println("Ingrese el apellido del estudiante: ");
                var apellido = consola.nextLine();
                System.out.println("Ingrese el email del estudiante: ");
                var email = consola.nextLine();
                System.out.println("Ingrese el telefono del estudiante: ");
                var telefono = consola.nextLine();
                var nuevoEstudiante = new Estudiante(nombre, apellido, telefono, email);
                var agregado = estudianteDao.agregarEstudiante(nuevoEstudiante);
                if(agregado)
                    System.out.println("Estudiante agregado: "+estudiante);
                else
                    System.out.println("Estudiante no agregado: "+estudiante);
            case 4:
                //Modificar estudiante
                System.out.println("Modificar estudiante");
                System.out.println("Ingrese el id del estudiante a modificar: ");
                var idEstudianteModificar = Integer.parseInt(consola.nextLine());
                System.out.println("Ingrese el nombre del estudiante: ");
                var nombreModificar = consola.nextLine();
                System.out.println("Ingrese el apellido del estudiante: ");
                var apellidoModificar = consola.nextLine();
                System.out.println("Ingrese el email del estudiante: ");
                var emailModificar = consola.nextLine();
                System.out.println("Ingrese el telefono del estudiante: ");
                var telefonoModificar = consola.nextLine();
                //creamos una instancia de la clase estudiante
                var estudiante =
                        new Estudiante(idEstudiante, nombre, apellido, telefono, email);
                var modificado = estudianteDao.modificarEstudiante(estudiante);
                if(modificado)
                    System.out.println("Estudiante modificado: "+estudiante);
                else
                    System.out.println("Estudiante no modificado: "+estudiante);
            case 5:
                //Eliminar estudiante
                System.out.println("Eliminar estudiante");
                System.out.println("Ingrese el id del estudiante a eliminar: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var eliminado = estudianteDao.eliminarEstudiante(estudiante);
                if(eliminado)
                    System.out.println("Estudiante eliminado: "+estudianteEliminar);
                else
                    System.out.println("Estudiante no eliminado: "+estudianteEliminar);
            case 6:
                //Salir
                System.out.println("Gracias por usar el sistema");
                salir = true;
            default: System.out.println("Opción no válida");
        }//fin switch
        return salir;
    }//fin metodo ejecutarOpciones
}//fin clase Main


