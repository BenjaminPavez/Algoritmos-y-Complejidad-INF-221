# -----------------------------------------------------------------------------
#
# Resolucion Problema 2 mediante Programacion Dinamica
#
# -----------------------------------------------------------------------------

import sys


'''
La funcion calcula la suma minima de los gaps al cuadrado de forma dinamica

    Parametros:
        ladrillos (list): Lista que contiene los ladrillos
        longitud (int): Entero que contiene la longitud de la pared

    Retorno:
        memo[n] (int): Entero que contiene la suma minima de los gaps al cuadrado
'''
def dinamica(ladrillos, longitud):
    n = len(ladrillos)
    #Inicializar la tabla que contiene las soluciones
    memo = [float('inf')] * (n + 1)
    #Caso base: si no hay ladrillos, la suma minima es 0
    memo[0] = 0

    #Llenar la tabla con las soluciones
    for i in range(1, n + 1):
        longitud_actual = 0
        for j in range(i, 0, -1):
            longitud_actual += ladrillos[j - 1]
            if longitud_actual > longitud:
                break
            gap = longitud - longitud_actual
            memo[i] = min(memo[i], memo[j - 1] + gap ** 2)

    return memo[n]


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
            longitud_pared, num_ladrillos = map(int, line.strip().split())
            ladrillos = list(map(int, file.readline().strip().split()))

            #Aqui se toma la suma minima de los gaps
            resultado = dinamica(ladrillos, longitud_pared)
            print(resultado)

    
if __name__ == "__main__":
    main()