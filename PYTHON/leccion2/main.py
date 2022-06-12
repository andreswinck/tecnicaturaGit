En esta clase veremos la sentencia if/else

# condicion = '' # variable vacia da False
condicion = 10
if condicion == True:  # se simplifica con -if condicion:-

    print("Condición Verdadera")

elif condicion == False:  # se simplifica asi -elif not condicion:-   pero no funciona igual ya que no entra en el ELSE

    print("Condición Falsa")
else:
    print("Condición sin especificar")

num = int(input("Digite un numero en el rango de 1 al 3: "))
numTexto = ""
if num == 1:
     numTexto = "Número uno"
elif num == 2:
     numTexto = "Número dos"
elif num == 3:
     numTexto = "Número tres"
else:
     numTexto = "Has ingresado un número fuera de rango"

print(f"el dato ingresado es  {num} - {numTexto}")

#operador ternario

"""condicion = False
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion falsa")

print("Condicion Verdadera") if condicion else print("Condicion falsa")"""

