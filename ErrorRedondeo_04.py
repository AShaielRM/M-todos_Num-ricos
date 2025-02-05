suma = 0.0
for _ in range(1000000):
    suma += 0.000001  # Sumamos un millón de veces 0.000001

print("Esperado: 1.0")
print("Obtenido:", suma)
#Debido al error de redondeo, el resultado puede no ser exactamente 1.0, sino algo como 1.000000000007918. 
# Esto ocurre porque los números pequeños pierden precisión al sumarse muchas veces.