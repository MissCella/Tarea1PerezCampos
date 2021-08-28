# Elaborado por: Francella Campos Alfaro y Gonzalo Pérez Solis
# Fecha de Creación: 25/08/2021 15:00
# Fecha de última Modificación: 27/08/21 18:15
#####################################################################

# Importacion de modulos/librerias
import time
import threading
import argparse

# Definicion de subclase New Thread


class NewThread (threading.Thread):
    """
        Funcionamiento: Override los argumentos anteriores
        Argumentos: threadid (int), name (str), arr (list)
        Metodos: run (Instrucciones para el hilo al inicializarse)
    """
    def __init__(self, threadid, name, arr):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = name
        self.arr = arr

    def run(self):
        """
            Funcionamiento: Instrucciones para cada hilo
            Entradas: self (class)
            Salidas: NA
        """
        potencia(self.arr)


def potencia(arr):
    """
        Funcionamiento: Calcula la potencia de cada elemento de un array
        Entradas: arr (lista)
        Salidas: NA
    """
    arrpot = []
    for i in arr:
        pot = i**2
        arrpot.append(pot)
        # Se agrega un sleep para sincornizar los elementos internos
        time.sleep(0.0001)
    return


# Argparse
parser = argparse.ArgumentParser(description='Calcular potencia cuadradada de cada elemento del array. ')
"""
    Funcionamiento: Argparse permite correr el script desde el shell con facilidades al usuario
    Argumentos: size (int, obligatorio), -t o --txt (opcional, envia resultados a un .txt file)
"""
parser.add_argument('size', type=int, help='Tamaño del Array')
parser.add_argument('-t', '--txt', action='store_true', help='Escribir los tiempos en un .txt')
# Variable para inicializar a parser y sus argumentos:
args = parser.parse_args()

# Variable del tamaño del array
x = args.size
# Creacion del array respecto al tamaño indicado
Arr = list(range(x))
print("Array = [ 0:", x-1, "]")


# Singlethread -------------------------------------------

# Inicializacion del hilo y medicion del tiempo de calculo
start1 = time.time()
potencia(Arr)
tim1 = (time.time()-start1)


# Multithreaded -----------------------------------------

# Se definen los limites de los arrays para cada hilo
x1 = x//4
x2 = x//2
x3 = 3*x//4

# Definicion de cada hilo utilizando la clase NewThread
thread1 = NewThread(1, "Thread1", Arr[0:x1])
thread2 = NewThread(2, "Thread2", Arr[x1:x2])
thread3 = NewThread(3, "Thread3", Arr[x2:x3])
thread4 = NewThread(4, "Thread4", Arr[x3:x])

# Inicializacion de cada hilo y medicion del tiempo de calculo
start4 = time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

tim4 = (time.time()-start4)
# Finalizacion del tiempo de calculo

# Implementacion del argumento para impresion de .txt del Argparse
if args.txt:
    # El nombre del archivo corresponde a "Tiempo"
    file = open("Tiempo.txt", "w")
    # Su unica funcion es sobreescribir en el archivo
    file.write("Tiempo de ejecución de cálculo para un hilo: " + str(tim1) + " \n")
    file.write("Tiempo de ejecución de cálculo para 4 hilos: " + str(tim4) + " \n")
    print('Tiempos escritos en archivo .txt')

else:
    # De lo contrario se imprimen los tiempos en pantalla
    print("Tiempo de ejecución de cálculo para un hilo: ", tim1)
    print("Tiempo de ejecución de cálculo para 4 hilos: ", tim4)
