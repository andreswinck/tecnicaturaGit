resultado = None
a = 10
b = 0
try:
    resultado = a/b # modificamos
except Exception as e:
    print(f"Ocurrió un error: {e}")

print(f"El resultado es: {resultado}")
print("Seguimos...")
