
# bool contiene los valores TRUE y FALSE
valor = 0
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

valor = -15
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

valor = -0.01
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

# tipo string -> false si esta vacio, true si tiene algun caracter
valor = ''
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

valor = 'hola '
resultado = bool(valor)
print(f'el valor: {valor}, resultado: {resultado}')

# tpo colecciones -> false si esta vacio, true si tiene algun elemento
#lista
valor = []
resultado = bool(valor)
print(f'el valor de una lista vacia: {valor}, resultado: {resultado}')

valor = [1,2,3]
resultado = bool(valor)
print(f'el valor de una lista con elementos: {valor}, resultado: {resultado}')

#tupla
valor = ()
resultado = bool(valor)
print(f'el valor de tupla vacia: {valor}, resultado: {resultado}')

valor = (1,2,3)
resultado = bool(valor)
print(f'el valor de una tupla con valores: {valor}, resultado: {resultado}')

#diccionario
valor = {}
resultado = bool(valor)
print(f'el valor de un dicc vacio: {valor}, resultado: {resultado}')

valor = {'a':1, 'b':2}
resultado = bool(valor)
print(f'el valor de un dicc con elementos: {valor}, resultado: {resultado}')

#conjunto
valor = set()
resultado = bool(valor)
print(f'el valor de un conjunto vacio: {valor}, resultado: {resultado}')

valor = {1,2,3}
resultado = bool(valor)
print(f'el valor de un conjunto con elementos: {valor}, resultado: {resultado}')

# sentencias de control con booleanos
if bool(''):
    print('el valor es verdadero')
else:
    print('el valor es falso')  

if 'hola':
    print('el valor es verdadero')
else:
    print('el valor es falso')

# ciclos
# while
variable = 176
while variable:
    print(f'regresa verdadero')
    break
else:
    print('regresa falso')






