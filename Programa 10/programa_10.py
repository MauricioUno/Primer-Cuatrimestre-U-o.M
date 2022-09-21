import json
import re


#-----------Primera parte-----------#

# Funcion imprimir_dato
def imprimir_dato(mensaje_a_imprimir: str):
    '''
    Parametros:
    Un string

    Imprime el string
    '''
    print(mensaje_a_imprimir)

# Punto 1.1
def imprimir_menu_desafio_cinco():
    '''
    Imprime el menu de opciones
    '''
    menu_desafio = "Opciones:\
            \nA- Imprimir nombres de los personajes de género femenino\
            \nB- Imprimir nombres de los personajes de género masculino\
            \nC- Determinar el personaje mas alto (género M)\
            \nD- Determinar el personaje mas alto (género F)\
            \nE- Determinar el personaje mas bajo (género M)\
            \nF- Determinar el personaje mas bajo (género M)\
            \nG- Determinar el promedio de altura (género M)\
            \nH- Determinar el promedio de altura (género F)\
            \nI- Imprimir nombre de los personajes con mayor y menor altura de cada genero\
            \nJ- Determinar la cantidad de personajes para cada tipo de color de ojo\
            \nK- Determinar la cantidad de personajes para cada tipo de color de pelo\
            \nL- Determinar la cantidad de personajes para cada tipo de inteligencia\
            \nM- Imprimir personajes ordenados por tipo de color de ojo\
            \nN- Imprimir personajes ordenados por tipo de color de pelo\
            \nO- Imprimir personajes ordenados por tipo de inteligencia\
            \nZ- Salir"

    imprimir_dato(menu_desafio)


# Punto 1.2
def stark_menu_principal_cinco() -> str:
    '''
    Llama a la funcion imprimir_menu y pide al usuario ingresar
    una letra.

    Retorna:
    La letra ingresada
    -1 Si se ingresa algo distinto de una letra
    '''
    imprimir_menu_desafio_cinco()
    opcion_elegida = input("> ")
    if re.search("^[a-oA-OzZ]$", opcion_elegida) != None:
        opcion_elegida = opcion_elegida.upper()
        valor_retorno = opcion_elegida

    else:
        valor_retorno = -1

    return valor_retorno


# Punto 1.3
def stark_marvel_app_cinco(personajes):
    '''
    Parametros:
    Una lista de diccionarios con los datos de los personajes

    Llama a la funcion stark_menu_principal.
    En funcion de la opcion elegida, se llamaran a distintas funciones
    '''
    while True:
        opcion_elegida = stark_menu_principal_cinco()

        match (opcion_elegida):
            case "A":
                imprimir_dato("Eligio A")
            case "B":
                imprimir_dato("Eligio B")
            case "C":
                imprimir_dato("Eligio C")
            case "D":
                imprimir_dato("Eligio D")
            case "E":
                imprimir_dato("Eligio E")
            case "F":
                imprimir_dato("Eligio F")
            case "G":
                imprimir_dato("Eligio G")
            case "H":
                imprimir_dato("Eligio H")
            case "I":
                imprimir_dato("Eligio I")
            case "J":
                imprimir_dato("Eligio J")
            case "K":
                imprimir_dato("Eligio K")
            case "L":
                imprimir_dato("Eligio L")
            case "M":
                imprimir_dato("Eligio M")
            case "N":
                imprimir_dato("Eligio N")
            case "O":
                imprimir_dato("Eligio O")
            case "Z":
                imprimir_dato("Adios!")
                break
            case -1:
                imprimir_dato("Ingrese una opción valida!")

    
# Punto 1.4
def leer_archivo(nombre_archivo: str) -> list:
    '''
    Parametros:
    Un string que representa la dirección del archivo a leer

    Se carga el archivo a un diccionario cuya clave hace referencia
    a la lista de diccionario con los datos de los personajes.
    
    Se inicializa una lista y se le asigna la lista adentro del diccionario

    Retorna:
    La lista de diccionarios de los personajes
    '''
    with open(nombre_archivo, 'r') as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["heroes"]

    return lista

lista_personajes = leer_archivo('Programa 10\data_stark.json')


# Punto 1.5
def guardar_archivo(nombre_archivo: str, datos_a_guardar: str) -> bool:
    '''
    Parametros:
    Un string que representa el nombre del archivo en el que se escribira
    Un string que representa los datos que se guardaran en el archivo

    Retorna:
    True en caso de que se haya guardado con exito
    False en caso de error (Tambien imprimira un mensaje informando del error)
    '''
    valor_retorno = True
    if re.search("(.json|.csv)$", nombre_archivo) != None:
        with open(nombre_archivo, 'w') as archivo:
            datos_guardados = archivo.write(datos_a_guardar)
            if datos_guardados != len(datos_a_guardar):
                imprimir_dato("No se guardaron los datos correctamente")
                valor_retorno = False
    else:
        imprimir_dato("El tipo de archivo no es valido!")
        valor_retorno = False

    return valor_retorno


# Punto 1.6
def capitalizar_palabras(string_a_capitalizar: str) -> str:
    '''
    Parametros:
    Un string

    La funcion capitalizara las palabras que encuentre en el string
    pasado como parametro

    Retorna:
    Un nuevo string con las palabras capitalizadas
    '''
    lista_palabras = set(re.findall("[a-zA-Z]+", string_a_capitalizar))

    for palabra in lista_palabras:
        palabra_capitalizada = palabra.capitalize()
        string_a_capitalizar = re.sub(palabra, palabra_capitalizada, string_a_capitalizar)


    return string_a_capitalizar


# Punto 1.7
def obtener_nombre_capitalizado(personaje: dict) -> str:
    '''
    Parametros:
    Un diccionario con los datos de un personaje

    La funcion genera un string que representa el nombre del personaje

    Retorna:
    El string generado
    '''
    nombre_capitalizado = capitalizar_palabras(personaje["nombre"])
    mensaje_nombre = "Nombre: " + nombre_capitalizado
    return mensaje_nombre


# Punto 1.8
def obtener_nombre_y_dato(personaje: dict, dato: str) -> str:
    '''
    Parametros:
    Diccionario con los datos del personaje
    String que representa una clave del diccionario (un dato del personaje)

    La funcion genera un string que representa el nombre y el dato pasado como parametro
    del personaje

    Retorna:
    El string generado
    '''
    mensaje_nombre = obtener_nombre_capitalizado(personaje)
    mensaje_dato = capitalizar_palabras(dato) + ": {}".format(personaje[dato]) 
    
    mensaje_nombre_y_dato = mensaje_nombre + " | " + mensaje_dato

    return mensaje_nombre_y_dato


#-----------Segunda parte-----------#

# Punto 2.1