'''
La funcion encuentra cual es la pila de cajas mas alta que se puede hacer utilizando las Cajas

    Parametros:
        Cajas (str): Lista de tuplas enteras que almacena la Altura, Ancho y Profundida de cada caja
        Pos_anterior Entero que representa la posicion en la lista de la caja anterior

    Retorno:
        max(max_altura, max_altura2) (int): Entero que representa el numero maximo
'''
max_altura = 0  #Guarda el maximo global

def LIS(Cajas, Pos_anterior):
    global max_altura  #max_altura es global

    if Pos_anterior >= len(Cajas):
        return 0

    for i in range(Pos_anterior, len(Cajas)):
        if (Cajas[Pos_anterior][1] > Cajas[i][1]) and (Cajas[Pos_anterior][2] > Cajas[i][2]):
            altura_con_caja = Cajas[Pos_anterior][0] + LIS(Cajas, i)
            max_altura = max(max_altura, altura_con_caja)
        else:
            Cajas2_intercambiadas = [(caja[1], caja[2], caja[0]) for caja in Cajas]
            LIS(Cajas2_intercambiadas, Pos_anterior + 1)

    max_altura2 = LIS(Cajas, Pos_anterior + 1)


    return max(max_altura, max_altura2)



'''
La funcion printea las cajas (PARA PROBAR EL FUNCIONAMIENTO)

    Parametros:
        cajitas (int): Lista de tuplas enteras que almacena la Altura, Ancho y Profundida de cada caja

    Retorno:
        La funcion no retorna nada
'''
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
            print(listaaux)
            value = LIS(listaaux,0) #Mando la lista a LIS
            print(f"Pila mas alta: {value}")
        else:
            print("Error")
            i += 1



'''
La funcion abre el archivo .dat que almacena los datos de entrada y los guarda en una lista de tuplas

    Parametros:
        nombre_arch (str): String que contiene el nombre del archivo, por defecto sera 'input-1.dat'

    Retorno:
        Cajas (int): Lista de enteros y tuplas con la Altura, Ancho y Profundida de cada caja
'''
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

cajitas = GuardarCajas('input-1.dat')
print(cajitas)
DatosCajas(cajitas)