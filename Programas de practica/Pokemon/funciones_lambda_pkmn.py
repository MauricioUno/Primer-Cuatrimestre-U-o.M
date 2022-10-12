import json
import re
import copy
from functools import reduce

#-------- Extraer lista de un archivo json --------#
def extraer_lista(direccion: str) -> list:
    '''
    Parametros:
    - La direccion del archivo.json a leer

    Funcion:
    - Abre el archivo en modo lectura, y carga el diccionario con
    ayuda de la biblioteca json

    Retorno:
    - La lista adentro del diccionario
    '''
    with open(direccion, 'r') as archivo:
        diccionario = json.load(archivo)

    return diccionario["pokemones"]

#-------- Validar lista con diccionarios ---------#
def validar_lista_con_diccionarios(pokemones: list) -> bool:
    '''
    Parametros:
    - Una lista

    Funcion:
    - Verifica que la lista pasada como parametro tenga almenos
    un elemento y que todos sus elementos sean del tipo diccionario

    Retorno:
    - True en caso que se cumplan todas las validaciones
    - False si ocurre un error
    '''
    validar_lista = True
    if type(pokemones) == type([]) and len(pokemones) > 0:
        for pokemon in pokemones:
            if type(pokemon) != type({}):
                validar_lista = False
                break     
    else:
        validar_lista = False

    return validar_lista

#-------- Validar con expresion regular --------#
def validar_dato(dato_ingresado: str, reg_ex_opciones: str):
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

#-------- Pedir dato al usuario --------#
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

#-------- Imprimir nombre y dato ---------#
def imprimir_nombres_y_dato(pokemones: list, dato: str, dato_es_lista = False):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los pokemon
    - El dato junto al cual se imprimira el nombre del pokemon
    - Un parametro opcional que nos indica si el valor de la clave es una lista

    Funcion:
    - Itera la lista e imprime los nombres de los pokemon junto con su dato correspondiente
    - En caso que el dato sea una lista, se transformara la lista en un string
    '''
    for pokemon in pokemones:
        mensaje_datos = "nombre: {0} | {1}: ".format(pokemon["nombre"], dato)
        if dato_es_lista:
            valor_dato = ", ".join(pokemon[dato])
        else:
            valor_dato = "{0}".format(pokemon[dato])

        mensaje_datos += valor_dato
        print(mensaje_datos)



# Punto 1
#-------- Listar ultimos N pokemones --------#
def listar_e_imprimir_ultimos_N_pokemon(pokemones: list):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los pokemon

    Funcion:
    - Se pide al usuario ingresar la cantidad de ultimos pokemon de la lista
    que desea listar e imprimir.
    - Se valida que la cantidad ingresada sea un entero y no supere el largo
    de la lista
    - Se crea una nueva lista con los ultimos N pokemon
    - Imprime los nombres de la lista junto con su id

    Retorna:
    - La nueva lista con los ultimos N pokemon
    - Una lista vacia en caso de error
    '''
    copia_pokemones = copy.deepcopy(pokemones)
    numero = int (ingresar_dato("Ingrese la cantidad: ", "^[+-]?[0-9]+$"))
    if (validar_rango_entero(numero, 1, len(copia_pokemones))):

        lista_generada = copy.deepcopy(pokemones[len(copia_pokemones) - numero:])
        imprimir_nombres_y_dato(lista_generada, "id")
    else:
        print("Error! No se ingreso un numero valido!")
        lista_generada = []

    return lista_generada
    


# Punto 2 y 3
#-------- Ordenar por clave numerica --------#
def listar_e_imprimir_por_clave_numerica(pokemones: list, dato: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los pokemon
    - El dato por el cual se ordenara la lista

    Funcion:
    - Se pide al usuario ingresar de que manera quiere ordenar la lista (asc/desc).
    - Se valida que el tipo de orden ingresado corresponda a una de las opciones
    - Se crea una nueva lista ordenada de manera asc/desc segun corresponda respecto
    del dato pasado como parametro
    - Imprime los nombres y el dato pedido

    Retorno:
    - La lista ordenada
    - Una lista vacia en caso de error
    '''
    copia_pokemones = copy.deepcopy(pokemones)
    tipo_de_orden = ingresar_dato("Ingrese de que manera ordenara la lista (asc/desc): ", "^(asc|desc)$")
    if tipo_de_orden != -1:
        if tipo_de_orden == "asc":
            copia_pokemones.sort(key = lambda pokemon : pokemon[dato])
        else:
            copia_pokemones.sort(key = lambda pokemon : pokemon[dato], reverse = True)
        lista_generada = copia_pokemones
        imprimir_nombres_y_dato(lista_generada, dato)
    else:
        print("Tipo de orden no valido!")
        lista_generada = []

    return lista_generada


# Punto 4
#-------- Listar segun mayor/menor al Promedio de elementos --------#
def listar_e_imprimir_segun_el_promedio(pokemones: list) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los pokemon

    Funcion:
    - Se pide al usuario que ingrese una clave de los diccionarios cuyo
    valor sea una lista
    - Luego se pide a que pokemon quiere listar respecto al promedio de elementos
    en las claves (mayor/menor)
    - Se crea una lista con los pokemon cuyos elementos sean mayor/menor al promedio
    segun corresponda
    - Se imprime los nombres junto con los elementos de la clave correspondiente

    Retorno:
    - La lista creada 
    - Una lista vacia si ocurre un error
    '''
    copia_pokemones = copy.deepcopy(pokemones)
    lista_generada = []
    reg_ex_claves = "^(tipo|evoluciones|fortaleza|debilidad)$"
    clave = ingresar_dato("Ingrese una de las clave lista (tipo/evoluciones/fortaleza/debilidad): ", reg_ex_claves)
    if clave != -1:
        tipo = ingresar_dato("Ingrese los pokemon a listar respecto al promedio (mayor/menor): ", "^(mayor|menor)$")
        if tipo != -1:
            
            lista_cantidad_elementos = list(map(lambda pokemon : len(pokemon[clave]), copia_pokemones))
            cantidad_elementos = reduce(lambda acumulador, elementos : acumulador + elementos, lista_cantidad_elementos)
            promedio_elementos = cantidad_elementos / len(copia_pokemones)

            if tipo == "mayor":
                lista_generada = list(filter(lambda pokemon: len(pokemon[clave]) > promedio_elementos, copia_pokemones))
            else:
                lista_generada = list(filter(lambda pokemon: len(pokemon[clave]) < promedio_elementos, copia_pokemones))

            if validar_lista_con_diccionarios(lista_generada):
                imprimir_nombres_y_dato(lista_generada, clave, True)
            else:
                print("Ningun pokemon tiene elementos {0} al promedio".format(tipo))
        else:
            print("Error!, Ingrese mayor o menor!")
    else:
        print("Error! Clave ingresada no valida!")

    return lista_generada


# Punto 5
#-------- Buscar pokemon por tipo --------#
def listar_e_imprimir_pokemon_por_tipo(pokemones:list):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los pokemon

    Funcion:
    - Se pide al usuario que ingrese el tipo del pokemon que esta buscando
    - Crea una nueva lista con los pokemon que poseen ese tipo
    - Imprime los nombres de los pokemon junto con su tipo
    - En caso de error imprime otro mensaje
    '''
    copia_pokemones = copy.deepcopy(pokemones)

    tipos_de_pokemon = "(planta|fuego|agua|acero|volador|electrico|fantasma|veneno|hielo|lucha|psiquico|dragon|oscuridad|piedra|tierra|bicho|normal|hada)"
    reg_ex_tipos = "^" + tipos_de_pokemon + "$"
    mensaje_input = "Ingrese el tipo del pokemon a buscar: \n" + tipos_de_pokemon + "\n>> "

    tipo_buscado = ingresar_dato(mensaje_input, reg_ex_tipos)
    if tipo_buscado != -1:
        
        lista_generada = list(filter(lambda pokemon: tipo_buscado in pokemon["tipo"], copia_pokemones))
        if validar_lista_con_diccionarios(lista_generada):
            imprimir_nombres_y_dato(lista_generada, "tipo", True)
        else:
            print("No hay ningun pokemon del tipo buscado")
    else:
        print("Error! Tipo ingresado no valido!")


# Punto 6
#-------- Archivar lista en un csv --------#
def archivar_lista(pokemones: list, direccion: str):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los pokemones
    - La direccion y nombre del archivo

    Funcion:
    - Valida que sea una lista de diccionarios
    - Escribe en el archivo la lista generada en los puntos [1-4]
    - Escribe en el archivo las diferentes claves de los diccionarios
    - Itera la lista, conviertiendo toda la informacion de la lista en formato
    csv, se escribe una linea por cada pokemon
    '''
    copia_pokemones = pokemones.copy()
    if validar_lista_con_diccionarios(copia_pokemones):
        
        with open(direccion, "w") as archivo:
            archivo.write("id, nombre, tipo, evoluciones, poder, fortaleza, debilidad\n")
            for pokemon in copia_pokemones:
                mensaje = ""
                for clave in pokemon:
                    mensaje += "{0}, ".format(pokemon[clave])

                mensaje = re.sub(", $", "\n", mensaje)
                archivo.write(mensaje)  
            print("Lista archivada")
    else:
        print("No hay informacion para archivar")


