def error_porcentual(valor_real, valor_aproximado):
    return abs((valor_real - valor_aproximado) / valor_real) * 100

temperatura_real = 36.5  # Temperatura real en grados Celsius
temperatura_medida = 35.8  # Temperatura obtenida con un termómetro

error = error_porcentual(temperatura_real, temperatura_medida)
print(f"Error porcentual en temperatura: {error:.2f}%")
#Se mide la temperatura de una persona con un termómetro y se compara con el valor esperado.