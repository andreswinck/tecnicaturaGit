import psycopg2  # Esto es para conectarnos a POSTGREd

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')  # es una tupla
            cursor.execute(sentencia, valores)
            #  conexion.commit() esto se utiliza sin with
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
