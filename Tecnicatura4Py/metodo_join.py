# help(str.join)

tupla_str = ('hola', 'mundo', 'desde', 'python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP']
curso = ' , '.join(lista_cursos)
print(f'curso: {curso}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '30'}
llaves = ' - '.join(diccionario.keys())
valores = ' - '.join(diccionario.values())
print(f'llaves: {llaves}, Type: {type(llaves)}')
print(f'valores: {valores} Type: {type(valores)}')


