
package domain;

import java.util.Date;

public class Cliente extends Persona {
    private int idClliente;
    private Date fechaRegistro; // Importar clase DATE
    private boolean vip;
    private static int contadorCliente; //es para incrementar
    
    //Constructor
    public Cliente(Date fechaRegistro, boolean vip, String nombre,
            String genero, int edad, String direccion){
        super(nombre, genero, edad, direccion);
        this.idClliente = ++Cliente.contadorCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    public int getIdClliente() {
        return this.idClliente;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;   
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("idClliente=").append(idClliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    

}
