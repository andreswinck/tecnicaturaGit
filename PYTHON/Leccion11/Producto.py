class Producto:
    contador_productos = 0  # variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1  # Aumento para la variable de clase
        self._id_producto = Producto.contador_productos  # Asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio
    # Métodos setters and getters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio
    # Sobreescribimos el método STR
    def __str__(self):
        return f"Id producto: {self._id_producto}, Nombre: {self._nombre}, Precio : {self._precio}"


if __name__ == "__main__":  # Solo sera visible si la prueba se ejecuta desde aquí
    prducto1 = Producto("Camiseta", 100.00)
    prducto2 = Producto("Pantalon", 150.00)

# clase 15.1 videos 2s122

