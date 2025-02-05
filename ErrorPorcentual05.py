import math

def error_porcentual(valor_real, valor_aproximado):
    return abs((valor_real - valor_aproximado) / valor_real) * 100

numero = 50
raiz_real = math.sqrt(numero)  # Raíz cuadrada exacta
raiz_aproximada = 7.1  # Aproximación de la raíz

error = error_porcentual(raiz_real, raiz_aproximada)
print(f"Error porcentual en raíz cuadrada: {error:.2f}%")
 #Comparamos el valor real de sqrt(50) con una aproximación de 7.1.