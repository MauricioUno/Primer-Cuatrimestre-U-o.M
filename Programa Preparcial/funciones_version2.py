#-------- Imprimir datos en consola ---------#
def imprimir_nombre_y_dato(lista_recibida: list, clave: str):
    '''
    Parametros:
    - Una lista de diccionarios
    - La clave que se imprimira

    Funcion:
    - Iterila la lista e imprime un string representando el nombre del personaje junto
    al dato que corresponde a la clave
    '''
    personajes = lista_recibida.copy()
    for personaje in personajes:
        print("Nombre: {0} | {1}: {2}".format(personaje["nombre"], clave.capitalize(), personaje[clave]))


def listar_N_elementos(lista_recibida: list, elementos: int) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con informacion de los personajes
    - Los elementos

    Retorno:
    - Un slice de la lista pasada como parametro
    '''
    personajes = lista_recibida[:elementos].copy
    return personajes

def listar_e_imprimir_personajes_por_cantidad(lista_recibida: list) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes

    Funcion:
    - Se pide al usuario que ingrese un numero, se valida que no supere
    el tamaño de la lista
    - Lista los primeros 'cantidad ingresada' personajes de la lista
    - Imprime los nombres junto con su identidad

    Retorna:
    - La nueva lista generada
    - Una lista vacia en caso de error
    '''
    personajes = lista_recibida.copy()
    cantidad = int(ingresar_dato("Ingrese la cant. personajes a listar: ", "^[0-9]+$"))
    if validar_rango_entero(cantidad, 1, len(personajes)):
        lista_generada = listar_N_elementos(cantidad)
        imprimir_nombre_y_dato(lista_generada, "identidad")
    else:
        print("Error! No se ingreso un numero valido!")
        lista_generada = []
    
    return lista_generada



def buscar_indice_max_min(lista_recibida: list, clave: str, calculo: str) -> int:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La clave sobre la cual se realizara la busqueda
    - El tipo de busqueda a realizar descendente = maximo, ascendente = minimo

    Funcion:
    - Itera la lista buscando el indice minimo/maximo de la clave pasada como parametro
    segun corresponda

    Retorna:
    - El indice correspondiente
    '''
    personajes = lista_recibida.copy()
    indice_max_min = 0

    for indice in range(len(personajes)):
        if calculo == "desc" and personajes[indice][clave] > personajes[indice_max_min][clave]:
            indice_max_min = indice
        elif calculo == "asc" and personajes[indice][clave] < personajes[indice_max_min][clave]:
            indice_max_min = indice
    
    return indice_max_min

def ordenar_lista_segun_dato(lista_recibida: list, clave: str, calculo: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La clave por la cual se ordenara la lista
    - La manera en la que ordenara la lista (asc/desc)

    Funcion:
    - Itera la lista, buscando el indice maximo/minimo segun corresponda
    - Cambia de lugares al elemento que se encuentra en el indice de la iteracion
    con el elemento de indice max/min
    - Cada vez que se ejecuta un swapeo, la busqueda del indice max/min se hace 
    desde una sublista que no tiene en cuenta a los elementos ya ordenados

    Retorna:
    - La lista ordenada
    '''
    personajes = lista_recibida.copy()

    for indice in range(len(personajes)-1):
        indice_max_min = buscar_indice_max_min(personajes[indice:], clave, calculo) + indice
        personajes[indice], personajes[indice_max_min] = personajes[indice_max_min], personajes[indice]

    return personajes

def listar_e_imprimir_personajes_segun_dato(lista_recibida: list, clave: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con nombres 

    Funcion:
    - Se pide al usuario ingresar la forma en la que ordenara la lista (asc/desc)
    - Se ordena la lista segun la clave pasada como parametro
    - Se imprime los nombres de los personajes junto con la clave pasada como parametro

    Retorno:
    - Una nueva lista ordenada
    - Una lista vacia
    '''
    personajes = lista_recibida.copy()
    calculo = ingresar_dato("Ingrese la forma a ordenar la lista (asc/desc): ", "^(asc|desc)$")
    if calculo != -1:
        lista_generada = ordenar_lista_segun_dato(personajes, clave, calculo)
        imprimir_nombre_y_dato(lista_generada, clave)
    else:
        print("Error! Ingrese un orden valido!")
        lista_generada = []

    return lista_generada



def calcular_promedio_clave(lista_recibida: list, clave: str) -> float:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La clave numerica de la cual se calculara el promedio

    Funcion:
    - Itera la lista, agregando en un acumulador el valor de la clave
    pasada como parametro dentro de los diccionarios de la lista
    - Calcula el promedio, dividiendo el acumulador de datos con la
    cantidad de personajes en la lista

    Retorna:
    - El promedio del dato por personaje
    '''
    personajes = lista_recibida.copy()
    
    acumulador_elementos = 0
    for personaje in personajes:
        acumulador_elementos += personaje[clave]

    promedio_elementos = acumulador_elementos / len(personajes)
    return promedio_elementos

def listar_personajes_respecto_al_promedio(lista_recibida: list, clave: str, calculo: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La clave numerica de la que se calculara el promedio
    - El calculo que se realizara; (mayor/menor) al promedio

    Funcion:
    - Calcula el promedio de la clave, luego lista a los personajes con
    un valor mayor/menor al promedio segun corresponda.

    Retorna:
    - La lista con los personajes correspondiente
    '''
    personajes = lista_recibida.copy()
    lista_promedio = []
    promedio = calcular_promedio_clave(personajes, clave)
    for personaje in personajes:
        if calculo == "mayor" and personaje[clave] > promedio or calculo == "menor" and personaje[clave] < promedio:
            lista_promedio.append(personaje)
    
    return lista_promedio

def listar_e_imprimir_segun_el_promedio(lista_recibida: list) -> list:
    '''
    Parametros:
    - Una lista de diccionario con los datos de los personajes

    Funcion:
    - Se pide al usuario ingresar una de las clave numericas y si desea
    ordenar la lista con personajes con valor mayor/menor al promedio de la clave
    elegida.
    - Se crea una lista con los personajes que correspondan a los parametros ingresados
    - Se imprime nombre y datos de los personajes de la lista

    Retorno:
    - La nueva lista
    - Una lista vacia en caso de error
    '''
    personajes = lista_recibida.copy()
    lista_generada = []
    clave = ingresar_dato("Ingrese la clave numerica (altura/peso/fuerza): ", "^(altura|fuerza|peso)$")
    if clave != -1:
        calculo = ingresar_dato("Listar mayor o menor al promedio de la clave?: ", "^(mayor|menor)$")
        if calculo != -1:
            lista_generada = listar_personajes_respecto_al_promedio(personajes, clave, calculo)
            if validar_lista_con_diccionarios(lista_generada):
                imprimir_nombre_y_dato(lista_generada, clave)
            else:
                print("Ningun personaje tiene {0} {1} al promedio".format(clave, calculo))
        else:
            print("Error! Orden ingresado no valido!")
    else:
        print("Error! Clave ingresada no valida!")

    return lista_generada
