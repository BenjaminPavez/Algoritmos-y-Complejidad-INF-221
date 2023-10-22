'''
La funcion AlturaMaxima resuelve por fuerza bruta recursiva el problema de la altura maxima apilando una serie de cajas, esta funcion itera por cada una de las Cajas dentro de Cajas, en caso de que la lista CajasElegidas este vacia, realiza una nueva llamada a la funcion
pero añadiendo la Caja a la lista newCajasElegidas y removiendola de la lista newCajas, en caso de que la lista CajasElegidas no este vacia, verifica que la base de la Caja sea mas pequeña que la ultima caja añadida a las CajasElegidas, en caso de que la base sea mas pequeña realiza el mismo procedimiento
de añadirla a la lista newCajasElegidas y removiendola de la lista newCajas.

    Parametros:
        Cajas : Lista que contiene todas las cajas que pueden ser utilizadas para crear la torre de cajas.
        CajasElegidas : Lista que contiene todas las cajas que ya fueron utilizadas para crear la torre de cajas.

    Return:
        altura : Entero que corresponde a la altura maxima que pudo ser alcanzada apilando las cajas.
'''
def AlturaMaxima(Cajas, CajasElegidas):
    altura = 0
    for Caja in Cajas:
        if len(CajasElegidas) == 0:
            newCajas = list(Cajas)
            newCajas.remove(Caja)
            newCajasElegidas = list(CajasElegidas)
            newCajasElegidas.append(Caja)
            altura = max(altura, Caja[0] + AlturaMaxima(newCajas, newCajasElegidas))
        else:
            if Caja[1] < CajasElegidas[-1][1] and Caja[2] < CajasElegidas[-1][2] or Caja[1] < CajasElegidas[-1][2] and Caja[2] < CajasElegidas[-1][1]:
                newCajas = list(Cajas)
                newCajas.remove(Caja)
                newCajasElegidas = list(CajasElegidas)
                newCajasElegidas.append(Caja)
                altura = max(altura, Caja[0] + AlturaMaxima(newCajas, newCajasElegidas))
    return altura



'''
La funcion GirarCajas recibe la lista inicial de Cajas leidas desde el archivo "input.dat" y le añade a esta lista las versiones 
giradas de cada una de las cajas que nos interesan para el problema.

    Parametros:
        Cajas : Lista que contiene todas las cajas que fueron leidas desde el archivo input.
        
    Retorno:
        La funcion no retorna nada
'''
def GirarCajas(Cajas):
    CajasGiradas = []
    for i in range(0, len(Cajas)):
        CajaGirada1 = (Cajas[i][1], Cajas[i][0], Cajas[i][2])
        CajaGirada2 = (Cajas[i][2], Cajas[i][1], Cajas[i][0])
        CajasGiradas.append(CajaGirada1)
        CajasGiradas.append(CajaGirada2)
    for Caja in CajasGiradas:
        Cajas.append(Caja)



'''
La funcion GuardarCajas recibe el nombre del archivo input, el cual se lee y saca la informacion del numero de cajas y las dimensiones de las cajas.

    Parametros:
        nombre_arch : String que contiene el nombre del archivo, por defecto sera 'input-1.dat'
        
    Retorno:
        Cajas : Lista que contiene todas las cajas que fueron leidas desde el archivo input.
'''
def GuardarCajas(nombre_arch):
    Cajas = []
    with open(nombre_arch, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Elimina los caracteres de espacio en blanco (" "), como saltos de línea y espacios en blanco al principio y al final
            if len(linea.split(" ")) == 1:
                num_cajas = linea.split(" ")
                Cajas.append(int(num_cajas[0]))
            elif len(linea.split(" ")) == 3:
                altura, ancho, profundidad = linea.split(" ")
                Cajas.append((int(altura), int(ancho), int(profundidad)))
            else:
                print("Error en la línea:", linea)
    return Cajas



'''
La funcion DatosCajas va recorriendo sobre la lista cajitas, y va resolviendo los problemas que se lean del input, y calcula
la altura maxima 

    Parametros:
        cajitas : Lista que contiene todas las cajas leidas del input.

    Retorno:
        La funcion no retorna nada
'''
def DatosCajas(cajitas):
    i = 0
    while i < len(cajitas):
        listaaux = []
        if isinstance(cajitas[i], int): #Se verifica si el elemento de la lista es un entero que representa a la cantidad de tuplas
            num_cajas = cajitas[i]
            #print(f"Cantidad de Cajas: {num_cajas}")
            i += 1
            for j in range(num_cajas):
                if i < len(cajitas) and isinstance(cajitas[i], tuple): #Se verifica que el elemento en la lista es una tupla
                    #print(f"Caja {j + 1}: Alto: {cajitas[i][0]}  Ancho: {cajitas[i][1]}  Profundidad: {cajitas[i][2]}") 
                    listaaux.append(cajitas[i])
                    i += 1
                else:
                    print("Error")
                    return
            GirarCajas(listaaux)
            CajasElegidas = []
            value = AlturaMaxima(listaaux, CajasElegidas) #Mando la lista a AlturaMaxima
            print(value)
        else:
            print("Error")
            i += 1



'''
La funcion DatosCajas_dinamico va recorriendo sobre la lista cajitas, y va resolviendo los problemas que se lean del input, y calcula
la altura maxima, version programacion dinamica.

    Parametros:
        cajitas : Lista que contiene todas las cajas leidas desde el input.

    Retorno:
        La funcion no retorna nada
'''
def DatosCajas_dinamico(cajitas):
    i = 0
    while i < len(cajitas):
        listaaux = []
        if isinstance(cajitas[i], int): #Se verifica si el elemento de la lista es un entero que representa a la cantidad de tuplas
            num_cajas = cajitas[i]
            #print(f"Cantidad de Cajas: {num_cajas}")
            i += 1
            for j in range(num_cajas):
                if i < len(cajitas) and isinstance(cajitas[i], tuple): #Se verifica que el elemento en la lista es una tupla
                    #print(f"Caja {j + 1}: Alto: {cajitas[i][0]}  Ancho: {cajitas[i][1]}  Profundidad: {cajitas[i][2]}") 
                    listaaux.append(cajitas[i])
                    i += 1
                else:
                    print("Error 2")
                    return
            GirarCajas(listaaux)        
            lista_aux_ord = sorted(listaaux, key =lambda listaaux : listaaux[1] * listaaux [2], reverse=True)  # Se ordena por la base 
            n = len(lista_aux_ord)
            memo = [0] * n    # Llenamos el arreglo de 0's
            for x in range (n):
                memo[x] = lista_aux_ord[x][0] # LLenamos cada posicion del arreglo con la altura correspondiente
            value = AlturaMaxima_programacion_dinamica(lista_aux_ord, memo) #Mando la lista a AlturaMaxima_programacion_dinamica
            print(value)
        else:
            print("Error 1")
            i += 1


"""
La funcion AlturaMaxima_programacion_dinamica() resuelve por programacion dinamica el problema de la altura maxima apilando una serie de cajas, esta
funcion va recorriendo el arreglo, el primer for parte desde la primera caja, y el segundo for parte desde 0 hasta la caja anterior a la actual,
el primer if verifica que la caja j pueda apilarse debajo de la caja i, luego si entra verifica si la altura que ya tenia el arreglo de memoria
es menor a la que se va a guardar, si es asi se guarda la nueva altura. Despues se itera sobre la lista memo y se saca el maximo.

    Parametros:
        Cajas: lista que contiene todas las cajas que pueden ser utilizadas para crear la torre de cajas.
        memo: lista que contiene todas las alturas, que pueden ser conseguidas por la respectiva caja.

    Retorno:
        max: entero que corresponde a la altura maxima que pudo ser alcanzada apilando las cajas.
"""

def AlturaMaxima_programacion_dinamica(Cajas, memo):
    n = len(Cajas)
    for i in range(1, n):
        for j in range(i): 
            if ((Cajas[j][1] > Cajas[i][1]) and (Cajas[j][2] > Cajas[i][2])) or ((Cajas[j][1] > Cajas[i][2]) and (Cajas[j][2] > Cajas[i][1])): #Ancho y profundidad
                if (memo[i] < memo[j] + Cajas[i][0]):
                    memo[i] = memo[j] + Cajas[i][0]    
    max = -1
    for i in range(n):
        if (max < memo[i]):
            max = memo[i]
    return max



#Para probar la funcion cambie el nombre del parametro de GuardarCajas 
Cajas = GuardarCajas('input-1.dat')
print("Resolucion con Fuerza Bruta Recursiva: ")
DatosCajas(Cajas)
print("Resolucion con Programacion Dinamica: ")
DatosCajas_dinamico(Cajas)
