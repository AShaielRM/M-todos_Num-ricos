public class ErrorRedondeo_02 {
//Diferencia de números casi iguales
    public static void main(String[] args) {
        double a = 1.0000001;
        double b = 1.0000000;
        double resultado = (a - b) * 1e7;
        System.out.println("Resultado esperado: 1");
        System.out.println("Resultado obtenido: " + resultado);
    }
}
//Al restar dos números muy cercanos, el resultado puede ser impreciso por la representación en coma flotante.