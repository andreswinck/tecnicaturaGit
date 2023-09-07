# Capa de datos de la entidad Persona
from capa_datos_persona.cursor_del_pool import CursorDelPool
from conexion import Conexion
from Persona import Persona
from logger_base import log


class PersonaDAO:
    _SELECIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

    # definimos los métodos de la clase persona
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._INSERTAR, (persona.nombre, persona.apellido, persona.email))
                log.debug(f'Persona insertada: {persona}')

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._ACTUALIZAR,
                               (persona.nombre, persona.apellido, persona.email, persona.id_persona))
                log.debug(f'Persona actualizada: {persona}')

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._ELIMINAR, (persona.id_persona,))
                log.debug(f'Persona eliminada: {persona}')

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    # eliminar un registro
    # persona1 = Persona(id_persona=28)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # actualizar un registro
    # persona1 = Persona(1, 'Juan Jose', 'Pena', 'jjpena@mail')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Insertar un registro
    # persona1 = Persona(nombre='Homero', apellido='Ramos', email='homeror@mail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)