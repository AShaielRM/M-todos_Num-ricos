a = 0.1 + 0.2  
b = 0.3

print("Esperado: 0.3")
print(f"Obtenido: {a}")

# Comparación directa
if a == b:
    print("Son iguales")
else:
    print("¡Son diferentes debido al error de redondeo!")

tolerancia = 1e-9
if abs(a - b) < tolerancia:
    print("Son aproximadamente iguales (corrigiendo el error de redondeo).")
    
#Matemáticamente, 0.1 + 0.2 debería dar 0.3, pero en Python (y muchos otros lenguajes), 
#el resultado es 0.30000000000000004 debido al error de redondeo.