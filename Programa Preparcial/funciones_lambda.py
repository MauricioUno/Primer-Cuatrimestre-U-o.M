import json
import re
from copy import deepcopy
from functools import reduce


def importar_lista(direccion: str):
    '''
    Parametros:
    - La direccion de la base de datos con la que se trabajara

    Lee el archivo.json y lo almacena en una variable

    Retorna:
    - La lista dentro del diccionario
    '''
    with open(direccion, "r") as archivo:
        diccionario = json.load(archivo)

    return diccionario["heroes"]

#-------- Validar con expresion regular --------#
def validar_string(opcion: str, reg_ex_opciones: str):
    '''
    Parametros: 
    - Un string que corresponde a algo ingresado por el usuario
    - La expresion regular de lo que considerado valido 

    Elimina los espacios vacios del string y verifica que 
    corresponda a la expresion regular, 

    Retorna:
    - El string ingresado pasado a minusculas
    - -1 Si no corresponde a la regEx
    '''
    opcion = opcion.strip()
    valor_retorno = -1
    if re.search(reg_ex_opciones, opcion, re.IGNORECASE):
        valor_retorno = opcion.lower()

    return valor_retorno

def ingresar_dato(texto_input: str, dato_buscado: str) -> str:
    '''
    Parametros:
    - El texto informando al usuario que debe ingresar
    - La expresion regular correspondiente a las opciones permitidas

    Se pide al usuario que ingrese algo, el texto ingresado sera validado
    en funcion de la expresion regular pasada como parametro

    Retorna:
    - El string validado si lo ingresado esta dentro de la expresion regular
    - -1 en caso que no sea lo pedido
    '''
    string_ingresado = input (texto_input)
    string_ingresado = validar_string(string_ingresado, dato_buscado)

    return string_ingresado

#--------- Mostrar informacion de lista en consola ---------#
def imprimir_nombres_y_dato(personajes: list, dato: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - El dato que se imprimira junto con el nombre

    Funcion:
    - Imprime los nombres de los personajes dentro de la lista junto con el
    dato pasado como parametro
    '''
    for personaje in personajes:
        mensaje = "Nombre: {0} | {1}: {2}".format(personaje["nombre"], dato.capitalize(), personaje[dato]) 
        print(mensaje)

#-------- Validar Rango ---------#
def validar_rango_entero(numero: int, minimo: int, maximo: int) -> bool:
    '''
    Parametros:
    - Un entero representando el numero validar
    - El limite minimo del rango (incluye el numero)
    - El limite maximo del rango (incluye el numero)

    Funcion:
    - Verifica que el numero pasado como parametro este dentro del
    rango

    Retorno:
    - True en caso que se encuentre dentro del rango
    - False si esta fuera del rango
    '''
    numero_validado = False
    if (numero > minimo-1) and (numero < maximo+1):
        numero_validado = True

    return numero_validado


# -------- Punto Uno -------- #
def guardar_imprimir_cantidad_personajes(personajes: list) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes

    Funcion:
    - Se pide al usuario que ingrese la cantidad de personajes que desea
    mostrar en pantalla
    - Se verifica que la cantidad no supere el largo de la lista
    pasada como parametro
    - Creara una lista nueva con la cantidad de personajes ingresada por el usuario.
    - Imprime los nombres de los personajes de la nueva lista

    Retorna:
    - La nueva lista generada
    - Lista vacia en caso de error
    '''
    cantidad = int(ingresar_dato("Ingrese la cantidad de personajes a listar: ", "^[0-9]+$"))

    if validar_rango_entero(cantidad, 1, len(personajes)):
        lista_generada = deepcopy(personajes[:cantidad])
        imprimir_nombres_y_dato(lista_generada, "identidad")
    else:
        print("Error!, valor ingresado no valido!")
        lista_generada = []
    
    return lista_generada


# -------- Punto Dos y Tres -------- #
def guardar_imprimir_personajes_ordenados(personajes: list, dato: str, orden = False) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes
    - El dato por el cual se ordenara a los personajes

    Funcion:
    - Se pide al usuario de que manera desea ordenar la lista
    - Ordena la lista de manera ascendente o descendente segun 
    la opcion ingresada y el dato pasado como parametro
    - Imprime en consola los nombres de los personajes de la nueva lista
    junto al valor del dato correspondiente

    Retorna:
    - Una nueva lista ordenada
    - Lista vacia en caso de error
    '''
    ordenar = ingresar_dato("Ingrese la manera de ordenar la lista (asc/desc): ", "^(asc|desc)$")
    if ordenar != -1:
        if ordenar == "desc":
            orden = True
        lista_generada = deepcopy(personajes)
        lista_generada.sort(key = lambda personaje : personaje[dato], reverse = orden)
        imprimir_nombres_y_dato(lista_generada, dato)           
    else:
        print("Error!, tipo de orden no valido!")
        lista_generada = []
    return lista_generada


# -------- Punto Cuatro -------- #
def guardar_imprimir_personajes_segun_el_promedio(personajes: list) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes

    Funcion:
    - Se pide al usuario que ingrese el dato por el cual se creara la lista
    - Se pide al usuario que ingrese de que manera ordenara la lista (mayor/menor) 
    respecto del promedio
    - Se crea una nueva lista que incluye a los personajes que sean mayor o menor al promedio
    del dato pasado como parametro, segun corresponda
    - Se imprime los nombres de los personajes de la nueva lista junto con el valor
    del dato correspondiente

    Retorna:
    - La nueva lista generada
    - Lista vacia en caso de error
    '''

    lista_generada = []
    clave = ingresar_dato("Ingrese la clave numerica (altura/fuerza/peso): ", "^(altura|fuerza|peso)$")
    if clave != -1:
        orden = ingresar_dato("Ingrese si desea listar segun los mayores o menores al promedio(mayor/menor): ", "^(mayor|menor)$")
        if orden != -1:
            lista_valores = list(map(lambda elemento : elemento[clave], personajes))
            suma_valores = reduce(lambda acumulador, elemento : acumulador + elemento, lista_valores)
            promedio_valores = suma_valores / len(lista_valores)
            
            if orden == "mayor":
                lista_generada = list(filter(lambda elemento : elemento[clave] > promedio_valores, personajes))
            else:
                lista_generada = list(filter(lambda elemento : elemento[clave] < promedio_valores, personajes))
                
            imprimir_nombres_y_dato(lista_generada, clave)
        else:
            print("Error!, tipo de orden no valido!")
    else:
        print("Error! clave ingresada no valida!")
    
    return lista_generada


# -------- Punto Cinco-------- #
def imprimir_personajes_por_inteligencia(personajes: list):
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes

    Funcion:
    - Pide al usuario ingresar el tipo de inteligencia que buscara en la lista
    - Crea una nueva lista con los personajes que tengan el mismo tipo de inteligencia
    ingresado
    - Imprime los nombres de los personajes de la nueva lista en consola
    - En caso de error imprime un mensaje distinto
    '''

    inteligencia = ingresar_dato("Ingrese la inteligencia por la que listara a los personajes(good/average/high): ",
                                  "^(good|average|high)$")
    if inteligencia != -1:
        lista_generada = list(filter(lambda elemento : elemento["inteligencia"] == inteligencia, personajes))

        print("Personajes con inteligencia '{0}': ".format(inteligencia))
        imprimir_nombres_y_dato(lista_generada, "identidad")
    else:
        print("Error!, inteligencia no valida")


# -------- Punto Seis-------- #
def archivar_lista(personajes: list, path: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La direccion y nombre del archivo

    Valida si es una lista con almenos un elemento
    La funcion guarda en un string una linea de texto por cada personaje, 
    en la linea se incluiran todos los datos del personaje
    Cuando se escriben todos los datos de los personajes, se guardara
    el string generado en un archivo csv
    '''
    copia_personajes = personajes.copy()
    if type (copia_personajes) == type([]) and len(copia_personajes) > 0 :

        mensaje = ""
        for personaje in copia_personajes:
            for clave in personaje:
                mensaje += "{0}, ".format(personaje[clave])
            mensaje = re.sub(", $", "\n", mensaje)
            
        
        with open(path, "w") as archivo:
            archivo.write("Nombre, Identidad, Altura, Peso, Fuerza, Inteligencia\n")
            archivo.write(mensaje)  
        print("Lista archivada")
    else:
        print("No hay informacion para archivar")
