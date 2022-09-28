# Ejercicio 8: Menú interactivo - cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de 1000 $ y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir


saldo = float(1000)
while True:
    print("\t Menú Cajero Automático")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    print()
    opcion = int(input("\n Ingrese la opción deseada (1 - 4): "))
    if opcion == 1:
        ingreso = float(input("Digite el monto a ingresar en la cuenta: "))
        saldo += ingreso
        print(f"El saldo actual es de-->: {saldo}")
    elif opcion == 2:
        retiro = float(input("Digite el monto a retirar de la cuenta: "))
        if retiro > saldo:
            print("No tiene fondos suficientes")
        else:
            saldo -= retiro
            print(f"El saldo actual es de-->: {saldo}")
    elif opcion == 3:
        print(f"El saldo actual es de: {saldo}")
    elif opcion == 4:
        print("Gracias por usar el servicio")
        break
    else:
        print("Esa opción es incorrecta")
        print()
