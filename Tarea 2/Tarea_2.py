import sys



'''
La funcion ReadInt recibe el nombre del archivo input, el cual se lee y saca la informacion del numero de cajas y las dimensiones de las cajas.

    Parametros:
        A : Lista de listas de enteros que contiene los intervalos
        
    Retorno:
        max_sup : Entero que contiene la superposicion mas grande entre todos los pares de intervalos
'''
def MaxSup(A):
    A = [tuple(interval) for interval in A]
    
    #Ordenar la lista de tuplas
    A.sort(key=lambda x: x[0])
    max_sup = 0

    def go(alo, ahi):
        nonlocal max_sup
        if alo >= ahi:
            return
        amid = alo + ((ahi - alo) >> 1)
        a = A[amid]
        go(alo, amid)
        for i in range(amid + 1, ahi + 1):
            b = A[i]
            overlap = min(a[1], b[1]) - max(a[0], b[0])
            if overlap > max_sup:
                max_sup = overlap
        go(amid + 1, ahi)

    go(0, len(A) - 1)

    return max_sup



'''
La funcion ReadInt recibe el nombre del archivo input, el cual se lee y saca la informacion del numero de cajas y las dimensiones de las cajas.

    Parametros:
        La funcion no recibe ningun parametro
        
    Retorno:
        La funcion no retorna nada
'''
def ReadInt():
    intervalos = []
    tam = 0
    for linea in sys.stdin:
        cadena = linea.split()
        if len(cadena) == 1:
            tam = int(cadena[0])
        else:
            i = 0
            while i < (tam * 2):
                sublista = []
                sublista.append(int(cadena[i]))
                sublista.append(int(cadena[i + 1]))
                intervalos.append(sublista)
                i += 2
            result = MaxSup(intervalos)
            
            # Cambia la lógica de impresión para reflejar la cantidad de intervalos con superposición
            print(result + 1 if result > 0 else 0)
            intervalos.clear()



#Inicio del programa
ReadInt()
