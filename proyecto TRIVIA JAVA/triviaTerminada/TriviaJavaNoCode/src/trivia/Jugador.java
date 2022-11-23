/*
 * Clase jugador
 */
package trivia;

import javax.swing.JOptionPane;

/**
 *
 * @author No_code
 */
public class Jugador {
    public String nombreJugador;
    public String puntoJugador;
    public int contador;
    public Jugador() {
    }

    public Jugador(String nombreJugador, String puntoJugador) {
        this.nombreJugador = nombreJugador;
        this.puntoJugador = puntoJugador;
    }

    public String getNombreJugador() {
        return nombreJugador;
    }

    public void setNombreJugador(String nombreJugador) {
        this.nombreJugador = nombreJugador;
    }

    public String getPuntoJugador() {
        return puntoJugador;
    }

    public void setPuntoJugador(String puntoJugador) {
        this.puntoJugador = puntoJugador;
    }

    @Override
    public String toString() {
        return "Jugador {" + "Nombre del jugador = " + nombreJugador + ", puntos del Jugador = " + puntoJugador + '}';
    }
    
    public void guardarNombre(){
        Titulos rambo = new Titulos();
        Titulos menu= new Titulos();
        Jugador jugador1 = new Jugador();
        jugador1.setNombreJugador(JOptionPane.showInputDialog(null, "POR FAVOR INGRESE EL NOMBRE DEL JUGADOR: "));
        //Aqui evalua que el campo nombre del jugador no este vacio
        if (jugador1.nombreJugador.isEmpty()) {
            System.out.println("Su nombre esta vacio intente nuevamente");
            contador += 1;
            if (contador == 3) { //Aqui si no pones nada mas de tres veces te apura rambo
                rambo.Rambo();
                guardarNombre();
            } else { //Si no te guarda el nombre
                guardarNombre(); 
            }
        } else { //Si haces todo correcto te asigna el puntaje a 0 y de modo de prueba mostramos nombre
            // y puntos del jugador imprimiendo el objeto jugador1
            menu.Menu();
            jugador1.setPuntoJugador("0");
            System.out.println("jugador1 = " + jugador1);
        }
    }
}
