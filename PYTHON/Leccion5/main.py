# Comenzamos con funciones
# mi_funcion() # no se puede llamar la funcion antes de definirla
# Definimos la función
def mi_funcion():
    print("Saludos a los alumnos de la tecnicatura")

mi_funcion() # estamos llamando a la función
mi_funcion() # se puede llamar una función N cantidad de veces

# desempaquetado de listas o list Unpacking

def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel","Betancud"]
show(person[0], person[1])  # pasamos un por uno los datos de la lista a la funcion
show(*person)   # pasamos todo junto
person2 = ("Osvaldo", "Giordanini")  # desempaquetado de TUPLAS
show(*person2)
# person3 = {"lastname": "Lucero", "name": "Natalia"}
# show(**person3)

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)
else:
    print("Esto se terminó")  # se ejecuta el ELSE aun con la lista vacía

# list comprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe","Pepe"]
alongP = [p for p in names if p[0] == "P"] # regresa una nueva lista
print(alongP)

#bottleC = [{ }]
#Arg = [b for b in bottleC if b["country"] == "Arg"]

# paso de Argumentos (funciones)

def mi_funcion2(name, lastName):
    print("Saludos")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Andres", "Winckler")

# La palabra return en funciones
# Creamos una funcion para sumar


def sumar(a, b):
    return a+b


# resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado es: {sumar(55, 45)}")


def sumar2(a: int = 0, b: int = 0) -> int:  # le damos valores por default

    return a + b


resultado = sumar2()
print(f"el resultado es: {resultado}")
print(f"el resultado es: {sumar2(22, 66)}")

# argumentos, variables en funciones


def listarNombres(*nombres):  #Normalmente se utiliza: *args
    for nombre in nombres: # se va a convertir en una tupla
        print(nombre)


listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listarNombres("MArcos","Daniel","Romina","Pepe")


def listarTerminos(**terminos):  # lo mas utilizado es **kwarg keyword args
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")


listarTerminos()  # no recibe nada no muestra nada
listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key")
listarTerminos(Nombre="Lionel Messi")

def desplegarNombres(nombres):
        for nombre in nombres:
            print(nombre)

nombres2 = ("Tito","Pedro","Carlos")
desplegarNombres(nombres2)
desplegarNombres("Carla")
desplegarNombres((10, 11))  #  numeros pasados como tupla (tiene que haber una coma si pasamos un solo elemento p.e. (10,)
desplegarNombres([12, 13])  #  numeros pasados como lista

# funciones recursivas
# clacula el factorial de un número ingresado por el usuario
def factorial(numero):
    if numero == 1:  # caso base
        return 1
    else:
        return numero * factorial(numero-1) # caso recursivo
numerofactorial = int(input("Digite el número para calcular el factorial; "))
resultado = factorial(numerofactorial)  # Lo hacemos en código duro
print(f"el factorial del numero {numerofactorial} es: {resultado}")
