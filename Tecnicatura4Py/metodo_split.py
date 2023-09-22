# help(str.split)

# cursos = 'Python Django Flask C C++ C# Java PHP'
# lista_cursos = cursos.split()
# print(f'lista_cursos: {lista_cursos}')
# print(f'Type: {type(lista_cursos)}')

cursos_separados_por_coma = 'Python,Django,Flask,C,C++,C#,Java,PHP'
lista_cursos1 = cursos_separados_por_coma.split()
lista_cursos2 = cursos_separados_por_coma.split(',')
print(f'lista_cursos: {lista_cursos1}')
print(f'lista_cursos: {lista_cursos2}')
print(f'cantidad de elementos {len(lista_cursos2)}')


      


