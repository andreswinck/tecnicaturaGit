import psycopg2 as bd  # Esto es para conectarnos a POSTGREd

conexion = bd.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432',
                        database='test_bd')

try:
    conexion.autocommit = False   # esto no deberia estar INICIA TRANSACCION
    cursor = conexion.cursor()
    # INSERTA UN NUEVO REGISTRO

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Jorge', 'Prol', 'clara@mail.com')
    cursor.execute(sentencia, valores)

    #  MODIFICA UN REGISTRO
    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores =('Juan Carlos', 'Perez', 'jcperez@mail.com', 1)

    cursor.execute(sentencia, valores)

    conexion.commit()   # hacemos el commit manualmente FINALIZA TRANSACCION
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()
