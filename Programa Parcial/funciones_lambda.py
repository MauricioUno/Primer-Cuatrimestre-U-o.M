import json
import re
import copy
from functools import reduce
from random import shuffle

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

def agregar_clave_genero(personaje: dict) -> dict:
    '''
    Parametros:
    - Un diccionario con datos del personajes

    Funcion:
    - Si el personaje no contiene la clave 'gender' se actualizara
    el diccionario del personaje con el valor dentro de la clave
    'data'
    - La clave 'data' contiene un diccionario con la clave 'gender'
    - Se elimina la clave 'data'

    Return:
    - El personaje actualizado
    '''
    if not "gender" in personaje.keys():
        diccionario_genero = personaje.pop("data")
        personaje.update(diccionario_genero)

    return personaje


def validar_dato(dato_ingresado: str, reg_ex_opciones: str) -> str:
    '''
    Parametros: 
    - Un string que corresponde al dato ingresado por el usuario
    - La expresion regular de lo que es considerado valido 

    Funcion:
    - Elimina los espacios vacios del string
    - Verifica que corresponda a la expresion regular.

    Retorna:
    - El string ingresado pasado a minusculas
    - -1 Si no corresponde a la regEx
    '''
    dato_ingresado = dato_ingresado.strip()
    valor_retorno = -1
    if re.search(reg_ex_opciones, dato_ingresado, re.IGNORECASE):
        valor_retorno = dato_ingresado.lower()

    return valor_retorno

def ingresar_dato(texto_input: str, reg_ex_opciones: str) -> str:
    '''
    Parametros:
    - El texto informando al usuario que debe ingresar
    - La expresion regular correspondiente a las opciones validas

    Funcion:
    - Se pide al usuario que ingrese algo
    - Valida lo ingresado en funcion de la expresion regular pasada como
    parametro

    Retorno:
    - El string ingresado
    - -1 en caso que no este dentro de la expresion regular
    '''
    dato_ingresado = input (texto_input)
    dato_ingresado = validar_dato(dato_ingresado, reg_ex_opciones)

    return dato_ingresado

def imprimir_datos_personajes_lista(personajes: list):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes

    Funcion:
    - Itera la lista de personajes imprimiendo todos sus datos
    '''
    for personaje in personajes:
        datos_personaje = ""
        for item in personaje.items():
            datos_personaje += "|{0}: {1}|".format(item[0].capitalize(),item[1])
        print(datos_personaje)

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
    - Se pregunta al usuario de que manera ordenara la lista (asc/desc)
    - Se valida si lo ingresado por el usuario es una de las opciones validas
    - Se crea una lista ordenada segun el dato pasado como parametro
    - Se imprime los nombres de los personajes junto con el dato correspondiente

    Retorno:
    - La lista ordenada
    - Una lista vacia si no paso la validacion
    '''
    dato_ingresado = ingresar_dato("Forma de ordenar la lista(asc/desc): ", "^(asc|desc)$")
    if dato_ingresado != -1:
        if dato_ingresado == "desc":
            orden = True
        else:
            orden = False

        lista_ordenada = copy.deepcopy(personajes)
        lista_ordenada.sort(key = lambda elemento : elemento[clave], reverse = orden)
        imprimir_nombre_con_dato(lista_ordenada, clave)
    else:
        print("Forma ingresada no valida!")
        lista_ordenada = []
    return lista_ordenada

def listar_por_genero(personajes: list, genero: str, imprimir = False) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - El genero el cual se buscara en la lista
    - Parametro opcional; si se desea imprimir se debera pasar un True, por defecto
    esta en False

    Funcion:
    - Crea la expresion regular del genero pasado como parametro
    - Crea una nueva lista de personajes conformada por aquellos cuyo valor de 'gender'
    corresponda a la expresion regular
    - Si 'imprimir' es True se imprimiran todos los datos de la lista fitrada

    Retorno:
    - La lista filtrada por genero
    '''
    reg_ex_genero = "^" + genero + "$"
    lista_genero = list(filter(lambda personaje : re.search(reg_ex_genero, personaje["gender"], re.IGNORECASE) != None, personajes))
    if imprimir:
        imprimir_datos_personajes_lista(lista_genero)
    return lista_genero

def imprimir_personaje_mas_alto(personajes: list, genero: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - El genero del cual se imprimira el personaje mas alto

    Funcion:
    - Se busca el personaje del genero pasado como parametro con mayor altura
    - Se imprime el personaje con mayor altura del genero pasado como parametro
    '''
    lista_genero = listar_por_genero(personajes, genero)
    mayor_altura_genero = reduce(lambda maximo, elemento : elemento if elemento["height"] > maximo["height"] else maximo, lista_genero)

    print("Personaje mas alto de genero '{0}'".format(genero))
    imprimir_nombre_con_dato([mayor_altura_genero], "height")
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
        imprimir_datos_personajes_lista(lista_coincidencias)
    else:
        print("Ningun personaje coincide con la busqueda realizada")


def imprimir_ultimo_personaje_lista_mezclada(personajes: list):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes

    Funcion:
    - Se crea una copia profunda de la lista pasada como parametro
    - Se mezcla el orden de los elementos de la nueva lista
    - Se imprimen todos los datos del ultimo personaje de la nueva lista
    '''
    personajes_mezclados = copy.deepcopy(personajes)
    shuffle(personajes_mezclados)
    imprimir_datos_personajes_lista([personajes_mezclados[-1]])


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