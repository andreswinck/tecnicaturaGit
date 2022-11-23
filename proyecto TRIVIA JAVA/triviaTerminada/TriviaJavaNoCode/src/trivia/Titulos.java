/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package trivia;

import com.sun.nio.sctp.SctpChannel;
import java.awt.BorderLayout;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

/**
 *
 * @author Nico
 */
public class Titulos {
    public String comienzo;
    public String terminando;
    
    public Titulos() {
    }

    public Titulos(String comienzo, String terminando) {
        this.comienzo = comienzo;
        this.terminando = terminando;
    }
    
    public void comienzoPresentacion(){
        
        var portada= new ImageIcon("TriviaGame.png");
        JLabel icon= new JLabel(portada);
        JLabel texto= new JLabel("Bienvenidos al Juego");
        JLabel texto1= new JLabel("Continue..");
        
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(icon,BorderLayout.CENTER);
        panel.add(texto,BorderLayout.NORTH);
        panel.add(texto1,BorderLayout.SOUTH);
        
        JOptionPane.showMessageDialog(null, panel, "Display image",JOptionPane.PLAIN_MESSAGE);
    }
    public void Rambo(){
        
        var portada= new ImageIcon("dontPlay.png");
        JLabel icon= new JLabel(portada);
        JLabel texto= new JLabel("NO JUEGUES CONMIGO");
        JLabel texto1= new JLabel("Continue..");
        
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(icon,BorderLayout.CENTER);
        panel.add(texto,BorderLayout.NORTH);
        panel.add(texto1,BorderLayout.SOUTH);
        
        JOptionPane.showMessageDialog(null, panel, "Display image",JOptionPane.PLAIN_MESSAGE);
    }
    public void Menu(){
        var portada= new ImageIcon("menu.png");
        JLabel icon= new JLabel(portada);
        JLabel texto= new JLabel("OPCIONES DEL JUEGO");
        JLabel texto1= new JLabel("LET'S PLAY");
        
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(icon,BorderLayout.CENTER);
        panel.add(texto,BorderLayout.NORTH);
        panel.add(texto1,BorderLayout.SOUTH);
        
        JOptionPane.showMessageDialog(null, panel, "Display image",JOptionPane.PLAIN_MESSAGE);
    }
    public void youWin(){
        var portada= new ImageIcon("youWin.png");
        JLabel icon= new JLabel(portada);
        JLabel texto= new JLabel("CONGRATULATIONS");
        JLabel texto1= new JLabel("CONTINUE CREDITS");
        
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(icon,BorderLayout.CENTER);
        panel.add(texto,BorderLayout.NORTH);
        panel.add(texto1,BorderLayout.SOUTH);
        
        JOptionPane.showMessageDialog(null, panel, "Display image",JOptionPane.PLAIN_MESSAGE);
    }
    public void youLose(){
        var portada= new ImageIcon("youLose.png");
        JLabel icon= new JLabel(portada);
        JLabel texto= new JLabel("OH NOO YOU LOSE");
        JLabel texto1= new JLabel("CONTINUE");
        
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(icon,BorderLayout.CENTER);
        panel.add(texto,BorderLayout.NORTH);
        panel.add(texto1,BorderLayout.SOUTH);
        
        JOptionPane.showMessageDialog(null, panel, "Display image",JOptionPane.PLAIN_MESSAGE);
    }
     
    //ACA ES DONDE INTENTE AGREGAR LA IMAGEN (ARREGLAR AQUI)
    public void credits(){
        var portada= new ImageIcon("credits.png");
        JLabel icon= new JLabel(portada);
        JLabel texto= new JLabel("CREDITS");
        JLabel texto1= new JLabel("THE END");
        
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(icon,BorderLayout.CENTER);
        panel.add(texto,BorderLayout.NORTH);
        panel.add(texto1,BorderLayout.SOUTH);
        
        JOptionPane.showMessageDialog(null, panel, "Display image",JOptionPane.PLAIN_MESSAGE);
    }
}
