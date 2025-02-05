public class ErrorPorcentual02 {
    public static void main(String[] args) {
        double velocidadReal = 60.0;  // Velocidad real en km/h
        double velocidadMedida = 58.5;  // Velocidad obtenida por un sensor

        double errorPorcentual = Math.abs((velocidadReal - velocidadMedida) / velocidadReal) * 100;

        System.out.println("Error porcentual en velocidad: " + errorPorcentual + "%");
    }
}
//Se mide la velocidad de un vehículo y se compara con el valor real.