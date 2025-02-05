saldo = 0.0
deposito = 0.01  # Depositamos 0.01 en cada iteración

for _ in range(1000):  # Hacemos 1000 depósitos
    saldo += deposito

print("Esperado: 10.00")
print(f"Obtenido: {saldo:.15f}") 
#El resultado debería ser exactamente 10.00, pero debido al error de redondeo en los números decimales, puede aparecer algo como 9.999999999999831. 
#En aplicaciones reales, esto puede generar errores en cálculos financieros.