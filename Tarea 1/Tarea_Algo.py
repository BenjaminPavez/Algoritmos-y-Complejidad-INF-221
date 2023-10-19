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

Cajas = GuardarCajas('input-1.dat')
DatosCajas(Cajas)