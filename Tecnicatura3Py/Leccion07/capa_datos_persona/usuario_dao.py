from usuario import Usuario
from logger_base import log
from cursor_del_pool import CursorDelPool

class UsuarioDao:
    '''
    DAO -> Data Access Object
    CRUD -> Create, Read, Update, Delete
    '''
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR   = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Insertando usuario: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Actualizando usuario: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Eliminando usuario: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    # Eliminar usuario
    usuario = Usuario(id_usuario=3)
    usuario_eliminado = UsuarioDao.eliminar(usuario)
    log.debug(f'Usuarios eliminados: {usuario_eliminado}')

    # Actualizar usuario
    usuario = Usuario(id_usuario=1, username='', password='369')
    usuario_modificado = UsuairioDao.actualizar(usuario)
    log.debug(f'Usuarios actualizados: {usuario_modificado}')

    # Insertar Usuario
    usuario = Usuario(username='Kely', password='321')
    usuario_insertado = UsuairioDao.insertar(usuario)
    log.debug(f'Usuario insertado: {usuario_insertado}')

    # Listar o seleccionar
    usuarios = UsuairioDao.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
    




