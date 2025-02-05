public class ErrorPorcentual03 {
    public static void main(String[] args) {
        double masaReal = 250.0;  // Masa real en gramos
        double masaMedida = 245.6;  // Masa obtenida con una balanza

        double errorPorcentual = Math.abs((masaReal - masaMedida) / masaReal) * 100;

        System.out.println("Error porcentual en medición de masa: " + errorPorcentual + "%");
    }
}
//Comparamos la masa real de un objeto con la masa medida por una balanza, mostrando el error porcentual.