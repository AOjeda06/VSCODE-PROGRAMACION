#Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y 
# qué operación se desea realizar con ellos. Las operaciones disponibles son sumar, restar, 
# multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta,
# 3 para la multiplicación y 4 para la división. La función devolverá el resultado de la operación mediante un número real.

def calculadora(operando1, operando2, operacion):
    resultado = None
    if operacion == 1:
        resultado = operando1 + operando2
    elif operacion == 2:
        resultado = operando1 - operando2
    elif operacion == 3:
        resultado = operando1 * operando2
    elif operacion == 4:
        if operando2 != 0:
            resultado = operando1 / operando2
        else:
            resultado = "Error: División por cero"
    else:
        resultado = "Operación no válida"
    return resultado