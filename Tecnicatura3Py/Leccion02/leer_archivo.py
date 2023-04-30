archivo = open("prueba.txt","r",encoding="utf8") # -r- para leer archivo -a- para anexar al archivo -x-  
# print(archivo.read(16))
# print(archivo.read(10)) #continuamos con la linea anterior
# print(archivo.readline())
# print(archivo.readline())

# vamos a iterar el archivo, cada una de las lineas

# for linea in archivo:
    # print(linea): itera todos los elementos del archivo

# print(archivo.readlines()[11])  # accedemos al archivo como si fuera una lista
# Anexamos informacion, cpiamos a otro

archivo2 = open("Copia.txt","w",encoding="utf8")
archivo2.write(archivo.read()) 
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo

print("Se ha terminado el proceso de leer y copiar archivos")





