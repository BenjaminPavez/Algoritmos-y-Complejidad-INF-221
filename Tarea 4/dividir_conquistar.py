import sys
import math

#Función para calcular la distancia euclidiana entre dos puntos
#punto[0] representa el eje x
#punto[1] representa el eje y
def euclides(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

#Funcion para encontrar la distancia minima del caso base
def distancia_minima(puntos):
    min_distancia = float('inf')
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            distancia = euclides(puntos[i], puntos[j])
            if distancia < min_distancia:
                min_distancia = distancia
    return min_distancia

#Funcion para encontrar la distancia minima de las dos mitades para combinar el resultado
#Fase de la conquista del problema
def conquista_mitades(mitad, dist):
    dist_min = dist 
    for i in range(len(mitad)):
        j = i + 1
        while j < len(mitad) and (mitad[j][1] - mitad[i][1]) < dist_min:
            dist = euclides(mitad[i], mitad[j])
            if dist < dist_min:
                dist_min = dist
            j += 1
            
    return dist_min

#Funcion principal que implementa el enfoque de dividir y conquistar, basados en Mergesort con una lista auxiliar para guardar los resultados
#y tiempo de ejecucion para el mejor y peor de los casos Theta n log n
def dividir_conquistar(puntos):
    cantidad = len(puntos)
    if cantidad <= 2:
        return distancia_minima(puntos)
    
    #se divide a lista en dos mitades
    mid = cantidad // 2
    mitad_izquierda = puntos[:mid]
    mitad_derecha = puntos[mid:]
    
    #Llamado recursivo de cada mitad hasta llegar al caso base
    d_izquierda = dividir_conquistar(mitad_izquierda)
    d_derecha = dividir_conquistar(mitad_derecha)
    
    #Nos quedaremos con el minimo valor del valor obtenido en la distancia minima sobre las mitades
    distancia = min(d_izquierda, d_derecha)
    
    #Aqui se construye la lista de las dos grandes mitades para despues comparar sus distancias
    #Como la lista esta ordenada mediante el eje x crearemos una lista auxiliar con aquel indice

    mid_x = puntos[mid][0]
    mitad = []
    for punto in puntos:
        if abs(punto[0] - mid_x) < distancia:
            mitad.append(punto)
    
    #distancia minima dentro de las mitades
    distancia_mitad = conquista_mitades(mitad, distancia)
    
    return min(distancia, distancia_mitad)

#Función para redondear hacia abajo, recibiendo el valor a truncar y los decimales que se quieren dejar
def funcion_piso(valor, decimales):
    factor = 10 ** decimales
    return math.floor(valor * factor) / factor


#Lectura de la entrada estandar para calcular las distancias mínimas
filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()

i = 0
resultados = []
while i < len(lines):
    n = int(lines[i].strip())
    i += 1
    coordenadas = list(map(int, lines[i].strip().split()))
    i += 1
    estrellas = []
    for j in range(0, len(coordenadas), 2):
        x = coordenadas[j]
        y = coordenadas[j+1]
        estrellas.append((x, y))

    distancia_min = dividir_conquistar(estrellas)
    redondeo = funcion_piso(distancia_min, 2)
    resultados.append(f"{redondeo:.2f}")
    
for resultado in resultados:
    print(resultado)
