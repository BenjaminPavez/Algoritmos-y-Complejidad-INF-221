def encontrar_superposicion_mas_grande(intervals):
    if len(intervals) <= 1:
        return 0

    medio = len(intervals) // 2
    izquierda = intervals[:medio]
    derecha = intervals[medio:]

    superposicion_izquierda = encontrar_superposicion_mas_grande(izquierda)
    superposicion_derecha = encontrar_superposicion_mas_grande(derecha)

    return superposicion_entre_conjuntos(izquierda, derecha) + superposicion_izquierda + superposicion_derecha



def superposicion_entre_conjuntos(izquierda, derecha):
    i, j = 0, 0
    superposicion = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][1] < derecha[j][0]:
            i += 1
        elif izquierda[i][0] > derecha[j][1]:
            j += 1
        else:
            superposicion += min(izquierda[i][1], derecha[j][1]) - max(izquierda[i][0], derecha[j][0]) + 1
            if izquierda[i][1] < derecha[j][1]:
                i += 1
            else:
                j += 1

    return superposicion



def GuardarCajas(nombre_arch):
    intervalos = []
    tam = 0
    with open(nombre_arch, 'r') as archivo:
        tam = 0
        for linea in archivo:
            cadena = linea.split()
            if(len(cadena) == 1):
                tam = int(cadena[0])
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
                result = encontrar_superposicion_mas_grande(intervalos)
                print(result)
                intervalos.clear() #Borro la lista para que no se acumulen los intervalos


def main():
    try:
        while True:
            n = int(input())
            intervals = [list(map(int, input().split())) for _ in range(n)]

            result = encontrar_superposicion_mas_grande(intervals)
            print(result)

    except EOFError:
        pass
            



GuardarCajas('input-1.dat')
