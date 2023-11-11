#QUITAR COMENTARIO AL ENVIAR
############################################################
       #OBS: Funcion nacho modificada por mi y chagpt
############################################################
'''
La funcion ReadInt recibe el nombre del archivo input, el cual se lee y saca la informacion del numero de cajas y las dimensiones de las cajas.

    Parametros:
        A : Lista de listas de enteros que contiene los intervalos
        
    Retorno:
        max_sup : Entero que contiene la superposicion mas grande entre todos los pares de intervalos
'''
def max_overlap(A):
    #Convertir la lista de listas en una lista plana de tuplas
    A = [tuple(interval) for interval in A]

    #Ordenar la lista de tuplas
    A.sort(key=lambda x: x[0])

    #Inicializar la superposición máxima
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
        nombre_arch : String que contiene el nombre del archivo, por defecto sera 'input-1.dat'
        
    Retorno:
        La funcion no retorna nada
'''
def ReadInt(nombre_arch):
    print("----------------------------------------------------------------")
    print("Archivo :",nombre_arch)
    intervalos = []
    tam = 0
    with open(nombre_arch, 'r') as archivo:
        tam = 0
        for linea in archivo:
            cadena = linea.split()
            if(len(cadena) == 1):
                tam = int(cadena[0])
                print("----------------------------------------------------------------")
                print("Cantidad de intervalos",tam)
            else:
                i = 0
                while(i<(tam*2)-1):
                    sublista = []
                    sublista.append(int(cadena[i]))
                    sublista.append(int(cadena[i+1]))
                    intervalos.append(sublista)
                    i+=2
                print("Intervalos :",intervalos)
                result = max_overlap(intervalos)
                print("Superposicion mas grande :",result)
                intervalos.clear() #Borro la lista para que no se acumulen los intervalos


def ReadDir():
    import os
    contenido = os.listdir('./')
    for nombre_arch in contenido:
        if(nombre_arch[-4:] == '.dat'):
            ReadInt(nombre_arch)
            print("\n")
        


ReadDir()
#ReadInt('input-1.dat') #Prueba 1