"""EJERCICIO 4
Haremos un programa que cuando el usuario ingrese su edad
le diga o imprima la etapa de su vida
0 a 9 = La infancia es increible y bella
10 a 19 = Tienes muchos cambios, mucho que estudiar
20 a 29 = Amor y comienza el trabajo
Para las siguietes etapas deberás completarlo..."""

edad = int(input("Digite su edad: "))
if 0 <=edad <= 9:
    print("La infancia es increible y bella")
elif 10 <=edad <= 19:
    print("Tienes muchos cambios, mucho que estudiar")
elif 20 <=edad <= 29:
    print("Se viene el desarrollo profesional, no pierdas el tiempo")
elif 30 <= edad <= 39:
    print("Llegan la familia y los hijos... ")
elif 40 <= edad <= 49:
    print("Tiempo de progresar en la vida")
elif 50 <= edad <= 59:
    print("Ultimas oportunidades para arriesgarte a hacer lo que no pudiste hasta ahora")
elif 60 <= edad <= 69:
    print("Se viene la jubilación y los nietos")
elif 70 <=edad <= 110:
    print("A disfrutar los ultimos años de tu vida")
else:
    print("Usted ingresó una edad incorrecta")
