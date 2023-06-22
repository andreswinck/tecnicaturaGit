public class Persona {
    private int id;
    private String nombre;
    private String tel;
    private String email;
    private static int numeroPersonas = 0;

    // constructor vacio
    public Persona() {
        this.id = ++Persona.numeroPersonas;
    }

    // Constructor con parámetros (sobrecarga de constructores)

public Persona(String nombre, String tel, String email) {
        this.nombre = nombre;
        this.tel = tel;
        this.email = email;
    }

    // getters y setters


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    // método toString
    @Override
    public String toString() {
        return "Persona{" +
                "id=" + id +
                ", nombre=" + nombre +
                ", tel=" + tel +
                ", email=" + email +
                '}';
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.setNombre("Juan Perez");
        persona1.setTel("1234567890");
        persona1.setEmail("jperez@mail.com");
        System.out.println(persona1);
    }
}
