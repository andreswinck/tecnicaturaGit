from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    # Método que se ejecuta cuando se crea el objeto
    def __enter__(self):
        log.debug(f'Inicio método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    # Método que se ejecuta cuando se elimina el objeto
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug(f'Se ejecuta método exit')
        # Se confirmarán los cambios si todo ha salido bien
        # Se deshacen los cambios si algo salió mal
        if valor_excepcion:
            self._conexion.rollback()
            log.debug(f"Ocurrió una excepción: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}")
        else:
            self._conexion.commit()
            log.debug("Transacción exitosa.")
        # Cerramos el cursor
        self._cursor.close()
        # Regresamos la conexión al pool
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())