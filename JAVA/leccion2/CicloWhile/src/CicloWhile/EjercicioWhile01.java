
package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //inferencia de tipos
        while (conteo <= 7){
            System.out.println("conteo = " + conteo);
            conteo++; //incrementa variable en 1
        }
            System.out.println("FIN CICLO WHILE");
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);
            System.out.println("FIN CICLO DO WHILE");
        for (var contando = 0;contando<7 ; contando++) {
            System.out.println("contando = " + contando);
        }
            System.out.println("FIN CICLO FOR");
    }
}
