# Ejercicio 4: Calculadora de impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Fórmula: pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
# Proporcione el pago sin impuestos: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def pago_con_impuesto(pago_sin_impuestos, impuesto):
    pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
    return pago_total


pago_sin_impuestos = float(input("Ingrese el importe de la compra sin impuestos: "))
impuesto = float(input("Ingrese el porcentaje de impuesto: "))
print(f"El pago con impuesto incluido es de: {pago_con_impuesto(pago_sin_impuestos, impuesto)}")