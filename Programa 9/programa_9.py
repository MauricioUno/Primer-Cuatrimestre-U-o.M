from data_stark import lista_personajes
import re
# Punto 1.1
def extraer_iniciales(nombre_personaje: str) -> str:
    '''
    Parametros:
    - Un string que representa el nombre del personaje

    Si el string no se encuentra vacio:
    Se creara un nuevo string con las iniciales del 
    nombre del personaje, omitiendo ciertas palabras y caracteres
    
    Retorna:
    - El string que representa las iniciales
    - 'N/A' si el string se encuentra vacio
    '''
    if len(re.findall("[A-Za-z]+", nombre_personaje)) > 0:
        
        nombre_personaje = nombre_personaje.upper()

        if nombre_personaje.count("-") > 0:
            nombre_personaje = re.sub("-", " ", nombre_personaje)

        if nombre_personaje.count("THE") > 0:
            nombre_personaje = re.sub("THE ", "", nombre_personaje)

        nombre_personaje = nombre_personaje.strip()
        palabras = re.findall("[A-Z]+",nombre_personaje)

        iniciales = ""
        for palabra in palabras:
            iniciales += palabra[0] + "."

    else:
        iniciales= "N/A"        

    return iniciales



# Punto 1.2
def definir_iniciales_nombre(personaje: dict) -> bool:
    '''
    Parametros:
    Un diccionario con los datos del personaje

    Se comprueba si se le paso un diccionario como parametro y si tiene
    una clave 'nombre'. En caso de que se cumplan las condiciones se agrega
    una nueva clave llamada 'iniciales'

    Retorna:
    True en caso de que la funcion se ejecute sin problemas
    False si no se cumple la condicion
    '''
    if type(personaje) == type({}) and personaje.get("nombre") != None: 
        personaje["iniciales"] = extraer_iniciales(personaje["nombre"])
        inicial_definida = True
    else:
        inicial_definida = False

    return inicial_definida


# Punto 1.3
def agregar_iniciales_nombre(personajes: list) -> bool:
    '''
    Parametros:
    Una lista de diccionarios con los datos del personaje correspondiente

    Se valida si el parametro es una lista y si tiene almenos un elemento,
    en caso de que se cumpla la condicion, comenzara a agregar un nuevo dato;
    'iniciales' a cada personaje de la lista
    Imprimira un mensaje en caso de que el diccionario del personaje no tenga
    la clave 'nombre'

    Retorna:
    True; si pudo agregar el dato a todos los personajes
    False; si hubo un error al intentar agregar los datos
    '''
    if type (personajes) == type ([]) and len(personajes) > 0:
        for personaje in personajes:
            iniciales_agregadas = definir_iniciales_nombre(personaje)
            if not iniciales_agregadas:
                print("El origen de datos no contiene el formato correcto")
                break

    else:
        iniciales_agregadas = False

    return iniciales_agregadas


# Punto 1.4
def stark_imprimir_nombres_con_iniciales(personajes: list):
    '''
    Parametros:
    Una lista de diccionarios con los datos del personaje correspondiente

    Se valida si el parametro es una lista y si tiene almenos un elemento,
    imprime mensajes con el nombre y las iniciales de los personajes, se notificara
    en caso de error.

    '''
    if type (personajes) == type ([]) and len(personajes) > 0:
        iniciales_agregadas = agregar_iniciales_nombre(personajes)
        if iniciales_agregadas:
            for personaje in personajes:
                mensaje_nombre_iniciales = "* {0} ({1})".format(personaje["nombre"], personaje["iniciales"])
                print(mensaje_nombre_iniciales)
        
    else:
        print("NO ME PASASTE UNA LISTA!")




# Punto 2.1
def generar_codigo_personaje(id: int, genero: str) -> str:
    '''
    Parametros:
    Un entero correspondiente al id del personaje
    Un string correspondiente al genero del personaje

    Genera un string que representa el genero y el numero id del personaje

    Retorna:
    El string creado
    "N/A" si no tiene genero o id
    '''
    if type(id) == int and len(re.findall("M|F|NB", genero)) == 1:
        mensaje_genero = "{0}-".format(genero)
        mensaje_id = "{0}".format(id).zfill(10 - len(mensaje_genero))
        mensaje_genero_e_id = mensaje_genero + mensaje_id
    else:
        mensaje_genero_e_id = "N/A"

    return mensaje_genero_e_id


# Punto 2.2
def agregar_codigo_personaje(personaje: dict, id: int) -> bool:
    '''
    Parametros:
    Un diccionario con los datos del personaje
    Un entero que representa el id del personaje

    Se valida que sea un diccionario con alguna clave, en caso de serlo
    creara una nueva clave llamada 'codigo' con un valor string
    que representa el codigo
    
    Retorna:
    True si cargo a 'codigo' con el string correspondiente
    False si ocurrio algun error
    '''
    generar_codigo = False
    if type(personaje) == type({}) and personaje != {}: 
        personaje["codigo"] = generar_codigo_personaje(id, personaje["genero"])
        if len (personaje["codigo"]) == 10:
            generar_codigo = True

    return generar_codigo


# Punto 2.3
def stark_generar_codigos_personaje(personajes: list):
    '''
    Parametros:
    Una lista de diccionarios con los datos de los personajes

    La funcion genera un ID para cada personaje, esta ID es dependiente de la posicion
    del personaje en la lista, luego pasara como parametro el diccionario con los datos
    del personaje y la ID generada a las funciones que se encargaran de generar el CODIGO

    En caso de que todo se ejecute correctamente, informara cuantos codigos fueron generados, seguido
    del primer y ultimo codigo generado
    En caso de haber un error se notificara echandole la culpa a la base de datos
    '''
    if type (personajes) == type ([]) and len(personajes) > 0:

        id_personaje = 1
        for personaje in personajes:
            if type (personaje) == type({}) or personaje.get("genero") != None:
                generacion_de_codigos = agregar_codigo_personaje(personaje, id_personaje)

            else:
                generacion_de_codigos = False
            
            if not generacion_de_codigos:
                break
            
            id_personaje += 1
        
        if generacion_de_codigos:    
            mensaje_codigos = "Se asignaron {0} codigos".format(len(lista_personajes))
            mensaje_codigos += "\nEl codigo del primer heroe es: {0}".format(lista_personajes[0]["codigo"])
            mensaje_codigos += "\nEl codigo del ultimo heroe es: {0}".format(lista_personajes[-1]["codigo"])
            print(mensaje_codigos)
        else:
            print("El origen de datos no contiene el formato correcto!")


# Punto 3.1
def sanitizar_entero(numero_str: str)-> int:
    '''
    Parametros:
    Un string que representa un posible numero entero

    La funcion eliminara los espacios vacios que el string tenga en 
    el inicio o en el fin, si es que los tiene.
    En caso de que el string represente un numero entero lo casteara
    a ese tipo de dato.

    Retorna:
    El string casteado Si el numero es positivo
    -1 Si hay un caracter no numerico
    -2 Si el string casteado es negativo
    -3 Si el string esta vacio
    '''
    if re.findall("^ | $", numero_str) != []:
        numero_str = numero_str.strip()

    if len (numero_str) > 0:

        re_entero = "^-?[0-9]+$"
        lista_numero = re.findall(re_entero, numero_str)
        if len(lista_numero) == 1 and lista_numero[0] == numero_str:
           
            numero_str = int (numero_str)
            if numero_str > 0:
                return numero_str # String representa un numero positivo
            else:
                return -2 # String no representa un numero positivo

        else:
            return -1  # Caracter no numerico presente

    else:
        return -3 # String vacio



print(sanitizar_entero("hola 23"))