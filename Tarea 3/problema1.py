# -----------------------------------------------------------------------------
#
# Resolucion Problema 1 mediante Fuerza Bruta
#
# -----------------------------------------------------------------------------

import sys


'''
La funcion calcula la suma minima de los gaps al cuadrado de forma recursiva

    Parametros:
        ladrillos (list): Lista que contiene los ladrillos
        fila_actual (int): Entero que contiene la fila actual
        longitud_actual (int): Entero que contiene la longitud actual
        longitud_maxima (int): Entero que contiene la longitud máxima

    Retorno:
        suma_minima (int): Entero que contiene la suma minima de los gaps al cuadrado
'''
def recursivo(ladrillos, fila_actual, longitud_actual, longitud_maxima):
    #Caso base: si hemos colocado todos los ladrillos, calculamos la suma de los gaps al cuadrado
    if fila_actual == len(ladrillos):
        return (longitud_maxima - longitud_actual) ** 2
    
    #Inicializamos la suma minima con un valor alto ya que siempre querremos la suma mínima
    suma_minima = 10000
    
    #Se coloca el ladrillo que sigue a la fila
    if longitud_actual + ladrillos[fila_actual] <= longitud_maxima:
        #Si el ladrillo cabe, recursivamente probamos la próxima configuración
        suma_minima = recursivo(ladrillos, fila_actual + 1, longitud_actual + ladrillos[fila_actual], longitud_maxima)
    
    #Nueva fila con el siguiente ladrillo
    gap = longitud_maxima - longitud_actual
    nueva_suma = gap ** 2 + recursivo(ladrillos, fila_actual + 1, ladrillos[fila_actual], longitud_maxima)
    
    #Aqui se toma la suma minima de los gaps
    suma_minima = min(suma_minima, nueva_suma)
    return suma_minima


'''
La funcion representa el main del programa

    Parametros:
        No recibe parametros

    Retorno:
        No retorna nada
'''
def main():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            # Leer la longitud de la pared y la cantidad de ladrillos
            longitud_pared, num_ladrillos = map(int, line.strip().split())

            #num_ladrillos no se ocupa ya que con un simple len se puede obtener dicho valor de la lista

            ladrillos = list(map(int, file.readline().strip().split()))
            suma_minima = recursivo(ladrillos, 0, 0, longitud_pared)
            print(suma_minima)


if __name__ == "__main__":
    main()