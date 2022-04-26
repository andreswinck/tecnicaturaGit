"""y = 5
print(id(y))
# nombre=input("Ingrese su nombre: ")
# print(nombre)
mivariable = 10
print(mivariable)
print(type(mivariable))
mivariable = "Un chanchito feliz"
print(mivariable)
print(type(mivariable))
mivariable = 3.5
print(type(mivariable))
a: str = "10"
print(a)
print(type(a))
x = 10
y = 5
z = x + y
print(x)
print(y)
print(z)

print(id(x))
print(id(y))
print(id(z))"""
# las literales se escriben en x240 y080 z400

# Tipos in, float, string, bool
x = 10
print(x)
print(type(x))

# Manejo de cadenas

miGrupoFavorito = "La Oreja de VanGogh"
caracteristicas = "The best rock band"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos booleanos (Bool)
miBooleano = 3 < 2
print(miBooleano)
if miBooleano:
    print("es verdadero")
else:
    print("El resultado es falso")

# entrada del usuario
"""resultado = input("Ingrese un numero: ")
print(resultado)"""
# conversión
numero1 = int(input("ingrese el primer número: "))
numero2 = int(input("ingrese el segundo número: "))
print("el resultado es: ", numero1+numero2)
