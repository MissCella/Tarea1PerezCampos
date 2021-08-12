# Elaborado por: Francella Campos Alfaro y Gonzalo Pérez Solis
# Fecha de Creación: 10/08/2021 11:00
# Fecha de última Modificación: 11/08/2021 18:06
# Versión: 3.9.6
#####################################################################

# importación de librerias:
import math


# Definicion de funciones:
def multiple_op(x):
    """
    Funcionamiento: Verificar que la entrada corresponde a un numero entero y
                    realizar distintas operaciones: a) Multiplicacion x*x
                                                    b) Potencia 2^x
                                                    c) Factorial x!
    Entradas: x(int)
    Salidas: array_salida(lista)
    """
    if type(x) == int:  # Se identifica si la entrada corresponde a un numero-
        # entero de lo contrario retorna el código de error único 0.
        array_salida = []  # Define el array de salida
        # En las siguientes lineas ocurren las 3 operaciones:
        a = x*x
        b = 2**x
        c = math.factorial(x)
        # Se agregan las operaciones al array de salida.
        array_salida = [a, b, c]
        return array_salida
    else:
        return 0


def verify_array_op(x):
    """
    Funcionamiento: Verificar que todos los elementos del arrary correspondan a
            numeros enteros positivos, de lo contrario retorna un código
            de error único. Para cada elemento del array utiliza multiple_op().

    Entradas: x (lista de tipo int)
    Salidas: array_salida(lista de listas de tipo int)
    """
    array_salida = []  # Define el array de salida
    for e in x:  # e stands for elemento de x
        if type(e) == int:  # Verifica que cada componente de x, sea un-
            # numero entero de lo contrario retorna un codigo-
            # de error unico.
            A = multiple_op(e)
            array_salida.append(A)  # Se agrega al array de salida, un nuevo-
            # array generado por multiple_op de cada elemento de x.
        else:
            return 0
    return (array_salida)
