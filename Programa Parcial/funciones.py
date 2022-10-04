import json
import re
import copy

def cargar_json(direccion: str) -> list:
    '''
    Parametros:
    - La direccion de donde se extraera la lista

    Funcion:
    - Utiliza la biblioteca json para extraer la lista de la
    base de datos

    Retorno:
    - La lista del archivo json
    '''
    with open (direccion, "r") as archivo:
        diccionario = json.load(archivo)

    return diccionario ["results"]


def convertir_numeros_lista(personajes: list) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes

    Funcion:
    - Crea una copia de la lista y convierte los valores de las claves
    numericas a enteros/flotantes segun corresponda

    Retorno:
    - Nueva lista con los valores casteados
    '''
    copia_personajes = copy.deepcopy(personajes)
    for personaje in copia_personajes:
        personaje["height"] = int (personaje["height"])
        personaje["mass"] = int (personaje["mass"])

    return copia_personajes



def imprimir_nombre_con_dato(personajes: list, clave: str):
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - El dato con el que se imprimira

    Funcion:
    - Imprime el nombre de los personajes junto con su dato pasado como
    parametros
    '''
    for personaje in personajes:
        print("Nombre: {0} | {1}: {2}".format(personaje["name"], clave.capitalize(), personaje[clave]))



def calcular_maximo(personajes: list, clave: str) -> int:
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - La clave por la cual se ordenara a los personajes

    Funcion:
    - Itera la lista buscando el indice del personaje con el valor
    max 

    Retorno:
    - El indice del personaje buscado
    '''  
    indice_max = 0
    for indice in range(len(personajes)):
        if personajes[indice][clave] > personajes[indice_max][clave]:
            indice_max = indice
    
    return indice_max

def ordenar_lista_segun_dato(personajes: list, clave: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La clave por la que se ordenara a los personajes (mass/height)

    Funcion:
    - Itera la lista de los personajes, swapeando el personaje
    con indice maximo con el personaje que señala el indice de la 
    iteracion
    - Al buscar el proximo maximo, solo se buscara el maximo en los elementos
    de la lista que aun no fueron ordenados

    Retorno:
    - La lista ordenada
    '''
    copia_personajes = copy.deepcopy(personajes)

    for indice in range(len(copia_personajes)-1):
        calcular_max = calcular_maximo(copia_personajes[indice:], clave) + indice
        copia_personajes[indice], copia_personajes[calcular_max] = copia_personajes[calcular_max], copia_personajes[indice]
    
    return copia_personajes

def imprimir_lista_ordenada(personajes: list, clave: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La clave por la que se ordenara los personajes

    Funcion:
    - Se crea una lista ordenada segun el dato pasado como parametro
    - Se imprime los nombres de los personajes junto con el dato correspondiente

    Retorno:
    - La lista ordenada
    '''
    lista_ordenada = ordenar_lista_segun_dato(personajes, clave)
    imprimir_nombre_con_dato(lista_ordenada, clave)

    return lista_ordenada



def crear_lista_por_genero(personajes: list, genero: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - El genero buscado
    
    Funcion:
    - Crea una lista con los personajes del genero pasado como parametro

    Retorna:
    - La nueva lista con los personajes correspondientes
    '''
    lista_genero = []
    for personaje in personajes:
        if personaje["gender"] == genero:
            lista_genero.append(personaje)
    
    return lista_genero

def imprimir_personaje_mas_alto(personajes: list, genero: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - El genero del cual se imprimira el personaje mas alto

    Funcion:
    - Se crea una lista de un elemento con el personaje de mayor altura del genero
    pasado como parametro
    - Se imprimen los personajes con mayor altura del genero pasado como parametro
    '''
    mayor_altura_genero = []
    lista_genero = crear_lista_por_genero(personajes, genero)
    indice_mayor_altura_genero = calcular_maximo(lista_genero, "height")
    mayor_altura_genero.append(lista_genero[indice_mayor_altura_genero])

    print("Personaje mas alto de genero '{0}'".format(genero))
    imprimir_nombre_con_dato(mayor_altura_genero, "height")
    print("\n")



def buscador_de_personajes(personajes: list, busqueda: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La busqueda realizada por el usuario
    
    Funcion:
    -Agregara a una lista los personajes que coincidan con la busqueada realizada
    por el usuario

    Retorno:
    - La lista con personajes cuyo nombre corresponda a la busqueda del
    usuario
    '''
    lista_coincidencias = []
    busqueda = busqueda.strip()
    for personaje in personajes:
        if re.search(busqueda, personaje["name"], re.IGNORECASE):
            lista_coincidencias.append(personaje)

    return lista_coincidencias

def imprimir_personajes_busqueda(personajes: list):
    '''
    Parametros:
    - Una lista de diccionarios con nombres de los personajes
    
    Funcion:
    - Se pide al usuario que ingrese a quien desea buscar
    - Se imprimen en consola los perosnajes cuyo nombre coincida
    con la busqueda realizada por el usuario junto con su genero.
    - En caso de no haber coincidencia de busqueda, se imprimira
    un mensaje informando de la situacion
    '''

    ingreso = input ("Realice la busqueda: ")
    lista_resultados = buscador_de_personajes(personajes, ingreso)
    if len(lista_resultados) > 0:
        print("Resultados: ")
        imprimir_nombre_con_dato(lista_resultados, "gender")
    else:
        print("Ningun personaje coincide con la busqueda realizada")


def archivar_lista(personajes: list, direccion: str):
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - La direccion donde se guardara la lista

    Funcion:
    - Se guarda la lista en formato csv, 
    - Primero se escribe las claves de los diccionarios
    - Se itera la lista de los personajes
    - Debajo de la primer linea con las claves, se escribe los datos
    de los personajes, cada personaje ocupa una linea
    '''
    if type(personajes) == type ([]) and len(personajes) > 0:

        with open (direccion, "w") as archivo:
            archivo.write("name, height, mass, gender\n")
            for personaje in personajes:
                datos_personaje = ""
                for clave in personaje:
                    datos_personaje += "{0}, ".format(personaje[clave])

                datos_personaje = re.sub(", $", "\n", datos_personaje)
                archivo.write(datos_personaje)

            print("Lista archivada! ")
    else:
        print("No hay informacion para archivar")


    



