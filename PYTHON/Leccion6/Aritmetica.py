class Aritmetica:
    """
    El nombre de este tipo de comentarios es DocString
    esto es documentación de la clase en python
    Vamos a hacer en esta clase algunas operaciones de + - * y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    #  método para sumar

    def suma(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB



aritmetica1 = Aritmetica(7, 9)
print(f"la suma es: {aritmetica1.suma()}")
print(f"la resta es: {aritmetica1.resta()}")
print(f"la multiplicación es: {aritmetica1.multiplicar()}")
print(f"la división es: {aritmetica1.dividir():.2f}")