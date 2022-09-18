# Mauricio Uño Ejercicio 8

from data_stark import lista_personajes

# Punto 0
def stark_normalizar_datos(lista: list, dato: str, tipo_de_casteo: type):
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que hace referencia a una clave del diccionario
    Tipo de casteo que se efectuara

    Recorrera la lista y en caso de ser necesario casteara
    el dato al tipo que se paso como parametro.
    '''

    if type (lista) == type ([]) and len(lista) > 0 and type(dato) == type("") and type(tipo_de_casteo) == type(type):
        datos_normalizados = 0
        for personaje in lista:
            if type(personaje[dato]) == type(""):
                personaje[dato] = tipo_de_casteo(personaje[dato])
                datos_normalizados += 1

        if datos_normalizados > 0:
            print("Cantidad de datos '{0}' normalizados : {1}".format(dato, datos_normalizados))
        else:
            print("Ningun dato '{0}' fue normalizado".format(dato))


    else:
        print ("ESTO NO ES UNA LISTA!")

stark_normalizar_datos(lista_personajes, "altura", float)   
stark_normalizar_datos(lista_personajes, "peso", float)
stark_normalizar_datos(lista_personajes, "fuerza", int)

# Punto 1.1
def obtener_nombre(diccionario: dict) -> str:
    '''
    Parametros:
    Diccionario con datos del personaje

    Se declara un string que incluye el nombre del personaje

    Retorna:
    El nuevo string
    '''
    nombre = "Nombre: {0}".format(diccionario["nombre"])
    return nombre



# Punto 1.2
def imprimir_dato(mensaje_a_imprimir: str):
    '''
    Parametros:
    Un string

    Imprime el string
    '''
    print(mensaje_a_imprimir)



# Punto 1.3
def stark_imprimir_nombres(lista: list):
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente

    Verifica que sea una lista por lo menos con 1 elemento;
    Si esto se cumple, imprimira el nombre de todos los personajes

    Retorna:
    -1 en caso que no se cumpla la condicion
    '''
    if type (lista) == type ([]) and len(lista) > 0:
        for diccionario in lista:
            mensaje_nombre = obtener_nombre(diccionario)
            imprimir_dato(mensaje_nombre)
    else:
        return -1



# Punto 2
def obtener_nombre_dato(diccionario: dict, dato: str) -> str:
    '''
    Parametros:
    Diccionario con datos del personaje
    String que hace referencia a una clave del diccionario

    Se declara un string que representa el nombre del personaje junto al dato que se pidio

    Retorna:
    El nuevo string
    '''
    nombre = obtener_nombre(diccionario)
    mensaje_nombre_dato = "{0} | {1}: {2}".format(nombre, dato, diccionario[dato])

    return mensaje_nombre_dato



# Punto 3
def stark_imprimir_nombres_alturas(lista: list):
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente

    Verifica que sea una lista por lo menos con 1 elemento;
    Si esto se cumple, imprimira los nombres de todos los personajes junto con su altura

    Retorna:
    -1 en caso que no se cumpla la condicion  
    '''
    if type (lista) == type ([]) and len(lista) > 0:
        for diccionario in lista:
            mensaje_nombre_altura = obtener_nombre_dato(diccionario, "altura")
            imprimir_dato(mensaje_nombre_altura)
    else:
        return -1




# Punto 4.1

def calcular_max_dato(lista: list, dato: str) -> dict:
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que hace referencia a una clave del diccionario

    Determina que personaje tiene el mayor valor del dato pasado como
    parametro

    Retorna:
    El diccionario con los datos del personaje elegido
    '''
    flag_primer_personaje = True
    for diccionario in lista:
        if flag_primer_personaje or diccionario[dato] > diccionario_max[dato]:
            diccionario_max = diccionario
            flag_primer_personaje = False

    return diccionario_max


# Punto 4.2
def calcular_min_dato(lista: list, dato: str) -> dict:
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que hace referencia a una clave del diccionario del personaje

    Determina que personaje tiene el menor valor del dato pasado como
    parametro

    Retorna:
    El diccionario con los datos del personaje elegido
    '''
    flag_primer_personaje = True
    for diccionario in lista:
        if flag_primer_personaje or diccionario[dato] < diccionario_min[dato]:
            diccionario_min = diccionario
            flag_primer_personaje = False

    return diccionario_min


# Punto 4.3
def calcular_max_min_dato(lista: list, calculo: str, dato: str) -> dict:
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que indicara que tipo de calculo se realizara ('maximo' o 'minimo')
    String que hace referencia al dato con el que se realizara el calculo

    Calculara el maximo o minimo del dato pasado como parametro

    Retorna:
    El diccionario con los datos del personaje que cumple
    con los parametros
    '''
    if calculo == "maximo":
        diccionario = calcular_max_dato(lista, dato)
    elif calculo == "minimo":
        diccionario = calcular_min_dato(lista, dato)
    
    return diccionario


# Punto 4.4
def stark_imprimir_max_min(lista: list, calculo: str, dato: str):
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que indicara que tipo de calculo se realizara ('maximo' o 'minimo')
    String que hace referencia al dato con el que se realizara el calculo

    Verifica que sea una lista por lo menos con 1 elemento y el calculo sea 'maximo' o 'minimo'
    Si esto se cumple imprimira un mensaje dependiente del dato y calculo pasados como parametro

    Retorna:
    -1 En caso de que no se cumpla la condicion
    '''
    if type(lista) == type([]) and len(lista) > 0 and (calculo == "maximo" or calculo == "minimo"):
        personaje_max_min = calcular_max_min_dato(lista, calculo, dato)
        nombre_y_dato_max_min = obtener_nombre_dato(personaje_max_min, dato)

        if calculo == "maximo":
            mensaje_max_min = "Mayor {0}:\n{1}".format(dato, nombre_y_dato_max_min)
        elif calculo == "minimo":
            mensaje_max_min = "Menor {0}:\n{1}".format(dato, nombre_y_dato_max_min)

        imprimir_dato(mensaje_max_min)
    else:
        return -1




# Punto 5.1
def sumar_dato(lista: list, dato: str) -> float:
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que hace referencia al dato con el que se realizara la suma

    Se inicializara un acumulador al que se le sumara el valor del dato pasado como parametro

    Retorna:
    El acumulador de los valores del dato pasado como parametro
    '''
    acumulador_suma_datos = 0
    for diccionario in lista:
        if type(diccionario) == type({}) and diccionario != {}:
            acumulador_suma_datos += diccionario[dato]
        
    return acumulador_suma_datos

# Punto 5.2
def dividir(dividendo: float, divisor: int) -> float:
    '''
    Parametro:
    Un dividendo y un divisor

    Si el divisor no es cero, realizara la division

    Retorna:
    El resultado de la division
    0 si no se cumple la condicion
    '''
    if divisor != 0:
        resultado = dividendo / divisor
        return resultado
    else:
        return 0

    
# Punto 5.3
def calcular_promedio(lista: list, dato: str) -> float:
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    String que hace referencia al dato del que se calculara el promedio

    Calcula el promedio

    Retorna:
    El promedio
    '''
    suma_datos = sumar_dato(lista, dato)
    contador_personajes = len(lista)

    promedio_datos = dividir(suma_datos, contador_personajes)

    return promedio_datos

# Punto 5.4
def stark_imprimir_promedio_altura(lista: list):
    '''
    Parametros:
    Lista de diccionarios con datos del personaje correspondiente
    
    Verifica que sea una lista por lo menos con 1 elemento y el calculo sea 'maximo' o 'minimo'
    Obtiene el promedio de la altura de los personajes e imprime un mensaje

    Retorna:
    -1 En caso de que no se cumpla la condicion
    '''
    if type (lista) == type ([]) and len(lista) > 0:
        
        promedio_altura = calcular_promedio(lista, "altura")
        mensaje_promedio_altura = "Altura promedio:\n{0:.2f}".format(promedio_altura)
        imprimir_dato(mensaje_promedio_altura)
    
    else:
        print("ERROR!")
        return -1




# Punto 6.1
def imprimir_menu():
    menu =  '''
            OPCIONES:
            1) Imprimir nombres
            2) Imprimir nombres con sus alturas correspondientes
            3) Determinar altura maxima
            4) Determinar altura minima
            5) Determinar el promedio de altura
            6) Imprimir nombres de los personajes con mayor y menor altura
            7) Imprimir nombres de los personajes con mayor y menor peso
            8) Salir
            Ingrese su opcion: 
            '''
    imprimir_dato(menu)


# Punto 6.2
def validar_numero(numero: str) -> bool:
    '''
    Parametros:
    Un string

    Retorna:
    True si el string es numerico, False si no lo es
    '''
    if numero.isnumeric():
        return True
    else:
        return False


# Punto 6.3
def stark_menu_principal():
    '''
    Se muestra el menu al usuario y este tendra que elegir una opcion
    En caso de recibir un numero, se lo casteara a entero

    Retorna:
    El numero ingresado convertido a int
    -1 si no se cumple la condicion
    '''
    imprimir_menu()
    opcion_ingresada = input (">>")
    
    if validar_numero(opcion_ingresada):
        opcion_ingresada = int (opcion_ingresada)
        return opcion_ingresada
    else:
        return -1



# Punto 7
def stark_marvel_app(lista_marvel: list):
    '''
    Parametro:
    Lista de diccionarios con datos del personaje correspondiente

    Es la funcion "principal"; recibira la opcion que el usuario ingreso ya casteada,
    en base a eso, llamara a las funciones correspondientes
    En caso de no ingresar ninguna opcion valida, se informara al usuario
    
    '''
    while True:
        numero_elegido = stark_menu_principal()

        match numero_elegido:
            case 1:
                stark_imprimir_nombres(lista_marvel)
            case 2:
                stark_imprimir_nombres_alturas(lista_marvel)
            case 3:
                stark_imprimir_max_min(lista_marvel, "maximo", "altura")
            case 4:
                stark_imprimir_max_min(lista_marvel, "minimo", "altura")
            case 5:
                stark_imprimir_promedio_altura(lista_marvel)
            case 6:
                stark_imprimir_max_min(lista_marvel, "maximo", "altura")
                stark_imprimir_max_min(lista_marvel, "minimo", "altura")
            case 7:
                stark_imprimir_max_min(lista_marvel, "maximo", "peso")
                stark_imprimir_max_min(lista_marvel, "minimo", "peso")
            case 8:
                print("ADIOS!")
                break
            case _:
                print("INGRESE UNA DE LAS 8 OPCIONES!")


stark_marvel_app(lista_personajes)