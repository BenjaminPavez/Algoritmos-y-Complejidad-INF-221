# La funcion AlturaMaxima calcula la altura maxima de forma recursiva usando fuerza bruta, es decir prueba
# todas las soluciones y se queda con la mejor

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

# La funcion GirarCajas hace que agreguen a las lista Cajas las rotaciones donde el valor de h_i cambia

def GirarCajas(Cajas):
    CajasGiradas = []
    for i in range(0, len(Cajas)):
        CajaGirada1 = (Cajas[i][1], Cajas[i][0], Cajas[i][2])
        CajaGirada2 = (Cajas[i][2], Cajas[i][1], Cajas[i][0])
        CajasGiradas.append(CajaGirada1)
        CajasGiradas.append(CajaGirada2)
    for Caja in CajasGiradas:
        Cajas.append(Caja)


# La funcion GuardarCajas saca la informacion de los archivos input, y los guarda en
# la variable Cajas

def GuardarCajas(nombre_arch):
    Cajas = []
    with open(nombre_arch, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Elimina los caracteres de espacio en blanco(" "), como saltos de línea y espacios en blanco al principio y al final
            if len(linea.split(" ")) == 1:
                num_cajas = linea.split(" ")
                Cajas.append(int(num_cajas[0]))
            elif len(linea.split(" ")) == 3:
                altura, ancho, profundidad = linea.split(" ")
                Cajas.append((int(altura), int(ancho), int(profundidad)))
            else:
                print("Error en la línea:", linea)
    return Cajas

# Va recorriendo sobre los elementos para calcular la altura maxima, version fuerza bruta

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


# Va recorriendo sobre los elementos para calcular la altura maxima, version programacion dinamica

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
            value = AlturaMaxima_progamacion_dinamica(lista_aux_ord, memo) #Mando la lista a AlturaMaxima_progamacion_dinamica
            print(value)
        else:
            print("Error 1")
            i += 1

# Empieza desde la segunda caja hasta la ultima caja y encuentra la maxima altura que se puede hacer con
# las cajas si entra al if mas interno significa que la caja i se puede apilar con la caja j

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


#Para probar la funcion cambie el nombre del parametro de GuardarCajas 

Cajas = GuardarCajas('input-3.dat')
DatosCajas(Cajas)
print("\n\n")
DatosCajas_dinamico(Cajas)
