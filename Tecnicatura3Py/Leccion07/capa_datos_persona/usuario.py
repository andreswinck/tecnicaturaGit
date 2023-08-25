class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password
    
    def __str__(self):
        return f'Id usuario: {self.id_usuario} \nUsername: {self.username} \nPassword: {self.password}'
    
    # Metodos Get y Set
    @property
    def id_usuario(self):
        return self.__id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    


