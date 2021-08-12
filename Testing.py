# Elaborado por: Francella Campos Alfaro y Gonzalo Pérez Solis
# Fecha de Creación: 10/08/2021 11:00
# Fecha de última Modificación: 11/08/2021 18:06
# Versión: 3.9.6
#####################################################################

# importación de librerias:
from Funciones import multiple_op, verify_array_op
import random
import math


# Definicion de funciones:
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menu al usuario.
    Entradas: NA
    Salidas: Resultado segun lo solicitado.
    - Explicación para los pasos a realizar en el test:
    1. Aparecerá un menú con las opciones de test.
    2. El usuario deberá escoger, mediante inputs, el test que desee comprobar.
    3. El test se generará automáticamente, y mostrará el resultado.
    4. Si elije un caso negativo, el código mostrará el error.
    5. Despues de un caso negativo se debe llamar de nuevo el menú.
    Esto para seguir con las comprobaciones.
    6. Al finalizar se debe elegir la opción 0, o se sale automáticamente
    con un código de error.
    """

    # Los siguientes prints presentan las pruebas:
    print("\n**********\n")
    print("Pruebas de funciones mediante Pytest")
    print("\n**********\n")
    print("1. Éxito para multiple_op")
    print("2. Éxito para verify_array_op")
    print("3. Caso negativo del punto a de multiple_op")
    print("4. Caso negativo del punto a de verify_array_op")
    print("0. Terminar")
    opcion = int(input("Escoja una opción: "))
    if opcion >= 0 and opcion <= 4:
        if opcion == 1:

            print("\n")
            x = random.randint(0, 10)  # Se genera una entrada aleatoria
            # para multiple_op.
            print("Random number is:", x)
            array1 = multiple_op(x)
            print("Operations result:", array1)
            # En forma de testbench, para verificar que sea
            # un caso de exito
            for e in array1:  # e stands for element in array.
                assert type(e) == int, "Array contiene un elemento incorrecto"
                assert array1[0] == x*x, "La multiplicación resultó incorrecta"
                assert array1[1] == 2**x, "La potencia resultó incorrecta"
                assert array1[2] == math.factorial(x), "Factorial erróneo"
            print("\n")

        elif opcion == 2:

            print("\n")
            array2 = []
            for i in range(3):  # Tamaño de array fijo de 3 elementos.
                y = random.randint(0, 10)  # genera array de valores aleatorios
                array2.append(y)
            print("Random Array:", array2)
            array_salida = verify_array_op(array2)
            print("Operations result:", array_salida)
            # En forma de testbench, para verificar que sea un caso de exito
            cont = 0
            for e in array_salida:
                assert e[0] == array2[cont] * array2[cont], "Operación errónea"
                assert e[1] == 2 ** array2[cont], "Operación errónea"
                assert e[2] == math.factorial(array2[cont]), "Operación mala"
                cont += 1
                for elem in e:
                    assert type(elem) == int, "Array con elemento incorrecto"
            print("\n")

        elif opcion == 3:

            print("\n")
            print("Input is 'x'")
            z = "x"  # Para caso negativo se define la entrada como un string
            array_error1 = multiple_op(z)
            assert array_error1 != 0, "ERROR, la entrada debe ser un número"
            print("\n")

        elif opcion == 4:

            print("\n")
            print("Input is '[2, 3.3, 'e']'")
            w = [2, 3.3, 'e']  # Para el caso negativo se agrega la letra e
            array_error2 = verify_array_op(w)
            assert array_error2 != 0, "ERROR, la entrada debe ser un número"
            print("\n")
            menu()

        else:
            return
    else:
        print("Opción inválida")
    menu()


# inicio del Programa Principal
menu()
