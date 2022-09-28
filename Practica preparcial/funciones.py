import json
import re
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

# -------- Punto Uno -------- #
def validar_rango(numero: int, personajes: list):
    '''
    Parametros:
    - Un numero entero
    - Una lista

    Verifica que el numero pasado como parametro no supere al largo de la lista

    Retorna:
    - True si no lo supera
    - False si lo supera
    '''
    numero_valido = False
    if numero > 0 and numero < len(personajes) + 1:
        numero_valido = True

    return numero_valido

def listar_heroes(personajes: list, cantidad: int) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes
    - La cantidad de personajes que se listaran (empezando desde indice 0)

    La funcion listara la cantidad de personajes pasada como parametro

    Retorna:
    - La nueva lista
    '''
    lista_recibida = personajes[:cantidad].copy()
    return lista_recibida



# -------- Punto Dos y Tres -------- #
def validar_string(opcion: str, reg_ex_opciones: str):
    '''
    Parametros: 
    - Un string que corresponde a una de las opciones
    - La expresion regular de las opciones

    Verifica que el string corresponda a una de las opciones

    Retorna:
    - True en caso que sea igual
    - -1 si no es igual
    '''
    opcion = opcion.strip()
    valor_retorno = -1
    if re.search(reg_ex_opciones, opcion, re.IGNORECASE):
        valor_retorno = opcion

    return valor_retorno


def buscar_max_min(lista: list, calculo: str, dato: str):
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - El string que determina que tipo de busqueda se realizara (minimo/maximo)
    - Sobre que dato del diccionario se realizara la busqueda

    La funcion buscara en la lista la posicion del personaje con el dato minimo o maximo segun
    corresponda.

    Retorna:
    - La posicion correspondiente 
    '''
    lista_recibida = lista.copy()
    indice_min_max = 0
    for indice in range(len(lista_recibida)):
        if (calculo == "asc" and lista_recibida[indice][dato] < lista_recibida[indice_min_max][dato]):
            indice_min_max = indice
        elif (calculo == "desc" and lista_recibida[indice][dato] > lista_recibida[indice_min_max][dato]):
            indice_min_max = indice

    return indice_min_max


def ordenar_y_listar_segun_dato(personajes: list, tipo_de_ordenamiento: str, dato: str) -> list:
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes
    - La forma en la que se ordenara la lista (ascendente, descendente)
    - El dato del diccionario sobre el que se realizara el ordenamiento

    Ordena la lista recibida segun los parametros dados

    Retorna:
    - La lista ordenada
    '''
    lista_recibida = personajes.copy()

    for indice in range(len(lista_recibida)-1):
        indice_minimo = buscar_max_min(lista_recibida[indice:], tipo_de_ordenamiento, dato) + indice
        lista_recibida[indice], lista_recibida[indice_minimo] = lista_recibida[indice_minimo], lista_recibida[indice]

    return lista_recibida

# -------- Punto Cuatro-------- #
def calcular_promedio(personajes: list, dato: str) -> float:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes
    - El dato del cual se calculara el promedio

    Hace una suma con todos los valores del dato pasado como parametro en los
    diccionarios, despues lo divide por la cantidad de personajes en la lista

    Retorna:
    - El promedio del dato pasado como parametro
    '''
    acumulador_datos = 0
    for personaje in personajes:
        acumulador_datos += personaje[dato]

    promedio = acumulador_datos / len(personajes)
    return promedio


def lista_ordenados_segun_el_promedio(personajes: list, dato: str, orden: str)-> list:
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - El dato de los diccionarios del cual se calculara el promedio y por
    el cual se ordenara a los personajes
    - El orden determina si los personajes que seran incluidos en la lista 
    deben tener un valor mayor o menor al promedio del dato

    Se crea una lista, se recorre la lista pasada como parametro y agrega
    a la nueva lista los personajes con valores mayor o menor al promedio, segun 
    corresponda

    Retorna:
    - La nueva lista
    '''
    lista_ordenada = []
    promedio_dato = calcular_promedio(personajes, dato)
    for personaje in personajes:
        if (orden == "mayor" and personaje[dato] > promedio_dato) or (orden == "menor" and personaje[dato] < promedio_dato):
            lista_ordenada.append(personaje)

    return lista_ordenada

# -------- Punto Cinco-------- #
def lista_por_tipo_de_inteligencia(personajes: list, inteligencia: str):
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes
    - El tipo de inteligencia buscado

    Crea una lista a las que se iran agregando los personajes que tengan
    el mismo tipo de inteligencia pasado como pasado como parametro

    Retorna:
    - La nueva lista
    '''
    lista_inteligencia = []
    for personaje in personajes:
        if (personaje["inteligencia"] == inteligencia):
            lista_inteligencia.append(personaje)

    return lista_inteligencia


# -------- Punto Seis-------- #
def guardar_lista(personajes: list):
    '''
    Parametros:
    - Una lista de diccionarios con datos de los personajes

    La funcion guarda en un string una linea de texto por cada personaje, 
    en la linea se incluiran todos los datos del personaje
    Cuando se escriben todos los datos de los personajes, se guardara
    el string generado en un archivo csv
    '''
    mensaje = ""
    for personaje in personajes:
        for clave in personaje:
            mensaje += "{0}: {1}, ".format(clave, personaje[clave])
        mensaje = re.sub(", $", "", mensaje)
        mensaje += "\n"

    with open("lista_generada.csv", "w") as archivo:
        archivo.write(mensaje)
    print("Lista guardada")

# Pedir dato al usuario
def dato_ingresado(texto_input: str, dato_buscado: str) -> str:
    '''
    Parametros:
    - El texto informando al usuario que debe ingresar
    - La expresion regular correspondiente al dato que estamos buscando

    Se pide al usuario que ingrese una opcion, el texto ingresado sera validado
    en funcion de la expresion regular pasada como parametro

    Retorna:
    - El string validado si lo ingresado esta dentro de la expreison regular
    - -1 en caso que no sea lo pedido
    '''
    string_ingresado = input (texto_input)
    string_ingresado = validar_string(string_ingresado, dato_buscado)

    return string_ingresado

# Punto 1
def imprimir_n_personajes(personajes: list) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes

    Funcion:
    - Se pide al usuario que ingrese la cantidad de personajes que desea
    mostrar en pantalla
    - Se verifica que la cantidad no supere el largo de la lista
    pasada como parametro
    - Creara una lista nueva con la cantidad de personajes ingresada por el usuario.
    - Imprime los nombres en consola

    Retorna:
    - La nueva lista generada
    - Lista vacia si la cantidad ingresada no es valida 
    '''
    cantidad = int(dato_ingresado("Ingrese la cantidad de personajes a listar: ", "^[+-]?[0-9]+$"))
    lista_generada = []
    if validar_rango(cantidad, personajes):
        lista_generada = listar_heroes(personajes, cantidad)
        imprimir_nombres(lista_generada)
    else:
        print("Error!, valor ingresado no valido!")
    
    return lista_generada


# Punto 2 y 3
def imprimir_personajes_ordenados(personajes: list, dato: str) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes
    - El dato por el cual se ordenara a los personajes

    Funcion:
    - Se pide al usuario de que manera desea ordenar la lista
    - Ordena la lista de manera ascendente o descendente segun 
    la opcion ingresada y el dato pasado como parametro
    - Imprime en consola los personajes ordenados junto al valor del dato

    Retorna:
    - Una nueva lista ordenada
    - Lista vacia en caso de no ingresar un tipo de orden valido
    '''
    lista_generada = []
    ordenar = dato_ingresado("Ingrese la manera de ordenar la lista (asc/desc): ", "^(asc|desc)$")
    if ordenar != -1:
        lista_generada = ordenar_y_listar_segun_dato(personajes, ordenar, dato)
        imprimir_nombres_dato(lista_generada, dato)           
    else:
        print("Error!, tipo de orden no valido!")

    return lista_generada

# Punto 4
def imprimir_personajes_por_promedio(personajes: list) -> list:
    '''
    Parametros:
    - La lista de diccionarios con datos de los personajes

    Funcion:
    - Se pide al usuario que ingrese el dato por el cual se creara la lista
    - Se pide al usuario que ingrese de que manera ordenara la lista (mayor/menor) 
    respecto del promedio
    - Se crea una nueva lista que incluye a los personajes que sean mayor o menor al promedio
    del dato pasado como parametro, segun corresponda

    Retorna:
    - La nueva lista generada
    - Una lista vacia si ingresa algo no valido

    '''
    lista_generada = []
    clave = dato_ingresado("Ingrese la clave numerica (altura/fuerza/peso): ", "^(altura|fuerza|peso)$")
    if clave != -1:
        orden = dato_ingresado("Ingrese si desea listar segun los mayores o menores al promedio(mayor/menor): ", "^(mayor|menor)$")
        if orden != -1:
            lista_generada = lista_ordenados_segun_el_promedio(personajes, clave, orden)
            imprimir_nombres_dato(lista_generada, clave)
        else:
            print("Error!, tipo de orden no valido!")
    else:
        print("Error! clave ingresada no valida!")
    
    return lista_generada


# Punto 5
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
    inteligencia = dato_ingresado("Ingrese la inteligencia por la que listara a los personajes(good/average/high): ",
                                  "^(good|average|high)$")
    if inteligencia != -1:
        lista_generada = lista_por_tipo_de_inteligencia(personajes, inteligencia)

        print("Tipo de inteligencia '{0}': ".format(inteligencia))
        imprimir_nombres(lista_generada)
    else:
        print("Error!, inteligencia no valida")


def imprimir_nombres(personajes: list):

    for personaje in personajes:
        mensaje = "Nombre: {0}".format(personaje["nombre"])
        print(mensaje)

def imprimir_nombres_dato(personajes: list, dato: str):

    for personaje in personajes:
        mensaje = "Nombre: {0} | {1}: {2}".format(personaje["nombre"], dato.capitalize(), personaje[dato]) 
        print(mensaje)