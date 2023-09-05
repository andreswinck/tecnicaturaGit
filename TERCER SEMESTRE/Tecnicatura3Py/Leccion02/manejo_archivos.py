# Declaramos una variable
try:
    archivo = open("prueba.txt", "w",encoding="utf8") #la - w - es de write (escribir)
    archivo.write("Programamos con diferentes tipos de archivos, ahora en TXT.\n")
    archivo.write("Los acentos son importantes para las palabras\n")
    archivo.write("como por ejemplo: acción, ejecución y producción\n")
    archivo.write("las letras son\n -w- para escribir \n-r- para leer archivo \n-a- para anexar al archivo \n-x- crea archivos\n")
    archivo.write("-t- es para texto, \nb archivos binarios, \nw+ lee y escribe son iguales r+\n")
    
    archivo.write("Con esto terminamos")
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo
# archivo.write("Todo quedó perfecto"): este es un errror I/O porque cerramos el archivo





