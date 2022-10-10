import json
import re
import copy
from functools import reduce

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


def castear_claves_numericas(personaje: dict) -> list:
    '''
    Parametros:
    - Un diccionario con datos del personaje

    Retorno:
    - El diccionario con las claves numericas casteadas
    '''
    personaje["height"] = int (personaje["height"])
    personaje["mass"] = int (personaje["mass"])

    return personaje


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
    lista_ordenada = copy.deepcopy(personajes)
    lista_ordenada.sort(key = lambda elemento : elemento[clave])
    imprimir_nombre_con_dato(lista_ordenada, clave)

    return lista_ordenada


def imprimir_personaje_mas_alto(personajes: list, genero: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - El genero del cual se imprimira el personaje mas alto

    Funcion:
    - Se crea una lista de un elemento con el personaje de mayor altura del genero
    pasado como parametro
    - Se imprime el personaje con mayor altura del genero pasado como parametro
    '''
    lista_genero = list(filter(lambda elemento : elemento["gender"] == genero, personajes))
    mayor_altura_genero = reduce(lambda maximo, elemento : elemento if elemento["height"] > maximo["height"] else maximo, lista_genero)
    lista_mayor_altura = [mayor_altura_genero]
    
    print("Personaje mas alto de genero '{0}'".format(genero))
    imprimir_nombre_con_dato(lista_mayor_altura, "height")
    print("\n")


def imprimir_personajes_busqueda(personajes: list):
    '''
    Parametros:
    - Una lista de diccionarios con nombres de los personajes
    
    Funcion:
    - Se pide al usuario que realice la busqueda
    - Se imprimen en consola los personajes cuyo nombre coincida
    con la busqueda realizada por el usuario.
    - En caso de no haber coincidencia de busqueda, se imprimira
    un mensaje informando de la situacion
    '''
    ingreso = input ("Realice la busqueda: ")
    lista_coincidencias = list(filter(lambda elemento : re.search(ingreso, elemento["name"], re.IGNORECASE) != None, personajes))
    if len(lista_coincidencias) > 0:
        print("Resultados: ")
        imprimir_nombre_con_dato(lista_coincidencias, "gender")
    else:
        print("Ningun personaje coincide con la busqueda realizada")


def archivar_lista(personajes: list, direccion: str):
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - La direccion donde se guardara la lista

    Funcion:
    - Guarda la lista en formato csv
    - Se escribe las claves de los diccionarios
    - Se itera la lista de los personajes
    - Se escribe los datos de cada personaje, cada uno
    ocupa una linea
    - En caso que la lista no pase las validaciones, se informara
    por consola
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

            print("Lista archivada!")
    else:
        print("No hay informacion para archivar")