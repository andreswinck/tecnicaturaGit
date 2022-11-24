/*
 * Testiando Jugador
 * 
 */
package test;

import trivia.Jugador;
import trivia.Preguntas;
import trivia.Titulos;

/**
 *
 * @author Nico
 */
public class TestJugador {
    public static void main(String[] args) {
        //Inicialización de los objetos de la clase
        Titulos inicio = new Titulos();
        Jugador nombre=new Jugador();
        Preguntas pregunta=new Preguntas();
        
        inicio.comienzoPresentacion(); //Presentación y comienzo del juego
        nombre.guardarNombre(); //Input y guardado del nombre del jugador
              
        pregunta.cargarPreguntas(); //Cargado manual de las preguntas
        pregunta.mostrarPregunta(); //Método para mostrar, responder y validar las preguntas
        pregunta.calcularGanador(); //Metodo para mostrar si el jugador gana o pierde
        
    }
    
    
}
