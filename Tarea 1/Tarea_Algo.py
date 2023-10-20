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

def GirarCajas(Cajas):
    CajasGiradas = []
    for i in range(0, len(Cajas)):
        CajaGirada1 = (Cajas[i][1], Cajas[i][0], Cajas[i][2])
        CajaGirada2 = (Cajas[i][2], Cajas[i][1], Cajas[i][0])
        CajasGiradas.append(CajaGirada1)
        CajasGiradas.append(CajaGirada2)
    for Caja in CajasGiradas:
        Cajas.append(Caja)

def GuardarCajas(nombre_arch):
    Cajas = []
    with open(nombre_arch, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Eliminar caracteres de espacio en blanco, como saltos de línea y espacios en blanco al principio y al final
            if len(linea.split(" ")) == 1:
                num_cajas = linea.split(" ")
                Cajas.append(int(num_cajas[0]))
            elif len(linea.split(" ")) == 3:
                altura, ancho, profundidad = linea.split(" ")
                Cajas.append((int(altura), int(ancho), int(profundidad)))
            else:
                print("Error en la línea:", linea)
    return Cajas

def DatosCajas(cajitas):
    i = 0
    while i < len(cajitas):
        listaaux = []
        if isinstance(cajitas[i], int): #Se verifica si el elemento de la lista es un entero que representa a la cantidad de tuplas
            num_cajas = cajitas[i]
            print(f"Cantidad de Cajas: {num_cajas}")
            i += 1
            for j in range(num_cajas):
                if i < len(cajitas) and isinstance(cajitas[i], tuple): #Se verifica que el elemento en la lista es una tupla
                    print(f"Caja {j + 1}: Alto: {cajitas[i][0]}  Ancho: {cajitas[i][1]}  Profundidad: {cajitas[i][2]}") 
                    listaaux.append(cajitas[i])
                    i += 1
                else:
                    print("Error")
                    return
            GirarCajas(listaaux)
            print(listaaux)
            CajasElegidas = []
            value = AlturaMaxima(listaaux, CajasElegidas) #Mando la lista a LIS
            print(value)
        else:
            print("Error")
            i += 1

#####
#####  Nuevas funciones
#####

def DatosCajas_dinamico(cajitas):
    i = 0
    while i < len(cajitas):
        listaaux = []
        if isinstance(cajitas[i], int): #Se verifica si el elemento de la lista es un entero que representa a la cantidad de tuplas
            num_cajas = cajitas[i]
            print(f"Cantidad de Cajas: {num_cajas}")
            i += 1
            for j in range(num_cajas):
                if i < len(cajitas) and isinstance(cajitas[i], tuple): #Se verifica que el elemento en la lista es una tupla
                    print(f"Caja {j + 1}: Alto: {cajitas[i][0]}  Ancho: {cajitas[i][1]}  Profundidad: {cajitas[i][2]}") 
                    listaaux.append(cajitas[i])
                    i += 1
                else:
                    print("Error 2")
                    return
            GirarCajas(listaaux)
            #print("lista         : " + str(listaaux))
            lista_aux_ord = sorted(listaaux, key =lambda listaaux : listaaux[1] * listaaux [2], reverse=True)  # Se ordena por la base 
            #print("lista ordenada: " + str(lista_aux_ord))
            n = len(lista_aux_ord)
            memo = [0] * n    # Llenamos el arreglo de 0
            for x in range (n):
                memo[x] = lista_aux_ord[x][0] # LLenamos cada posicion del arreglo con la altura correspondiente
            #print(memo)
            value = AlturaMaxima_progamacion_dinamica(lista_aux_ord, memo) #Mando la lista a AlturaMaxima_progamacion_dinamica
            print(value)
        else:
            print("Error 1")
            i += 1

def AlturaMaxima_progamacion_dinamica(Cajas, memo):
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




Cajas = GuardarCajas('input-1.dat')
DatosCajas(Cajas)
DatosCajas_dinamico(Cajas)
