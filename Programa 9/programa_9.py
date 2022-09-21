# Uño Mauricio Ejercicio 9

from data_stark import lista_personajes
import re

#-------- Primera Parte --------#
# Auxiliar Punto 1.1
def reemplazar_en_string(valor_viejo: str, valor_nuevo, el_string: str) -> str:
    '''
    Parametros:
    - el_string: La variable pasada como parametro
    - valor_viejo: Lo que buscaremos en el_string
    - valor_nuevo: Lo que reemplazara a valor_viejo en el_string, en caso de encontrarlo.

    Retorna:
    - El string con los valores reemplazados
    - El string sin cambios, si no encuentra a valor_viejo dentro del texto               
    '''
    if re.search(valor_viejo, el_string) != None:
            el_string = re.sub(valor_viejo, valor_nuevo, el_string)

    return el_string

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
    - 'N/A' si hay un error
    '''
    if re.search("[A-Za-z]+", nombre_personaje) != None:
        
        nombre_personaje = nombre_personaje.upper()

        nombre_personaje = reemplazar_en_string("-", " ", nombre_personaje)
        nombre_personaje = reemplazar_en_string("THE ", "", nombre_personaje)

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
    if type(personaje) == type({}) and "nombre" in personaje.keys(): 
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
        print("Error, el parametro dado no es una lista!")



#-------- Segunda Parte --------#

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
    if type(id) == int and re.search("^(M|F|NB){1}$", genero) != None:
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

        validacion_diccionario = True
        for personaje in personajes:
            if type (personaje) != type({}) or not("genero" in personaje.keys()):
                validacion_diccionario = False
                break
                
        if validacion_diccionario:
            id_personaje = 1
            for personaje in personajes:
                codigo_generado = agregar_codigo_personaje(personaje, id_personaje)
                if not codigo_generado:
                    break
                id_personaje += 1

            if codigo_generado:    
                mensaje_codigos ="Se generaron {0} codigos\
                                \nEl codigo del primer personaje es: {1}\
                                \nEl codigo del ultimo personaje es: {2}\
                                ".format(len(lista_personajes), lista_personajes[0]["codigo"], lista_personajes[-1]["codigo"])
                print(mensaje_codigos)

            else:
                print("Uno de los personajes no tiene un genero valido")
        else:
            print("Error, uno de los elementos de la lista no es un diccionario con la clave 'genero'")
    else:
        print("Error, el parametro dado no es una lista!")



#-------- Tercera Parte --------#
# Auxiliar sanitizaciones 1
def eliminar_vacio(el_string: str) -> str:
    '''
    Retorna el string pasado como parametro 
    con los espacios vacios eliminados, si es que los hay
    '''
    if re.search("^ | $", el_string) != None:
        el_string = el_string.strip()
    
    return el_string

# Auxiliar sanitizaciones 2
def sanitizar_numero(tipo_numero: type, reg_ex: str, numero_str: str) -> int:
    '''
    Parametros:
    - tipo_numero: El tipo de numero al que se casteara el string
    - reg_ex: Un string representa la expresion regular del tipo de numero a castear
    - numero_str: El posible numero en tipo string

    Retorna:
    - El numero sanitizado en caso que sea mayor a 0
    - -1 Si el numero sanitizado no es positivo
    - -2 Si hay un caracter que no corresponda al de la expresion regular
    - -3 Si el string esta vacio 
    '''
    if len (numero_str) > 0:

        if re.search(reg_ex, numero_str) != None:
            numero_str = tipo_numero (numero_str)
            if numero_str > 0:
                numero_sanitizado = numero_str # String representa un numero positivo
            else:
                numero_sanitizado = -2 # String representa un numero negativo o cero

        else:
            numero_sanitizado = -1  # Caracter no correspondiente a la reg_ex presente

    else:
        numero_sanitizado = -3 # String vacio
    
    return numero_sanitizado

# Punto 3.1
def sanitizar_entero(numero_str: str) -> int:
    '''
    Parametros:
    Un string que representa un posible numero entero

    La funcion eliminara los espacios vacios que el string tenga en 
    el inicio o en el fin, si es que los tiene.
    En caso de que el string represente un numero entero lo casteara
    a ese tipo de dato.

    Retorna:
    - El string casteado si el numero es positivo
    - -1 Si hay un caracter no correspondiente a un numero entero
    - -2 Si el string casteado es negativo
    - -3 Si el string esta vacio
    '''
    numero_str = eliminar_vacio(numero_str)

    numero_sanitizado = sanitizar_numero(int, "^[+-]?[0-9]+$", numero_str)
    return numero_sanitizado


# Punto 3.2
def sanitizar_flotante(numero_str: str)-> float:
    '''
    Parametros:
    Un string que representa un posible numero flotante

    La funcion eliminara los espacios vacios que el string tenga en 
    el inicio o en el fin, si es que los tiene.
    En caso de que el string represente un numero flotante lo casteara
    a ese tipo de dato.

    Retorna:
    - El string casteado Si el numero es positivo
    - -1 Si hay un caracter no correspondiente a un numero flotante
    - -2 Si el string casteado es negativo
    - -3 Si el string esta vacio
    '''
    numero_str = eliminar_vacio(numero_str)

    numero_sanitizado = sanitizar_numero(float, "^[+-]?[0-9]+(\.[0-9]+)?$", numero_str)
    return numero_sanitizado


# Punto 3.3
def sanitizar_string(texto_str: str, valor_default = "-") -> str:
    '''
    Parametros:
    Un string que es posible represente palabras
    Otro string que se usara en caso que el primer string sea vacio

    Elimina los espacios vacios o las '/', si es
    que los hay. Dependiendo lo que represente el string, el valor
    de retorno cambia

    Retorna:
    El string pasado a minuscula Si solo hay letras
    El string de 'respaldo' si el primer string esta vacio
    'N/A' Si hay otro tipo de caracter en el string
    '''
    
    texto_str = reemplazar_en_string("/", " ", texto_str)
    texto_str = eliminar_vacio(texto_str)

    
    if len (texto_str) > 0:
        reg_ex_palabras = "^[a-z A-Z()-]+$"
        if re.search(reg_ex_palabras, texto_str) != None:
            texto_str = texto_str.lower()
            texto_sanitizado = texto_str # String representa palabras
        else:
            texto_sanitizado = "N/A" # String tiene un caracter que no es una letra

    else:
        valor_default = eliminar_vacio(valor_default)
        texto_sanitizado = valor_default.lower() # El primer string esta vacio y se usa el string opcional
    
    return texto_sanitizado


# Punto 3.4
def sanitizar_dato(personaje: dict, clave: str, tipo_dato: str) -> bool:
    '''
    Parametros:
    Un diccionario que representa los datos del personaje
    Un string que representa un dato del personaje
    Otro string que determina el tipo de sanitizacion

    Verifica que la clave pasada como parametro exista en el diccionario y
    que el tipo de sanitizacion sea valido. Si todas las condiciones se cumplen,
    se llama a una de las funciones sanitizar, si no hay inconvenientes el dato es
    normalizado y se asigna ese valor a la clave del diccionario correspondiente

    Retorna:
    True; Si el dato es normalizado con exito
    False; Si hubo un error
    '''
    dato_normalizado = False
    if not (clave in personaje.keys()):
        print ("La clave especificada no existe en el personaje")
        
    else:
        tipo_dato = tipo_dato.lower()
        match (tipo_dato):
            case "string":
                dato_sanitizado = sanitizar_string(personaje[clave], "Undefined")
                if dato_sanitizado != "N/A":
                    dato_normalizado = True
                    
            case "flotante":
                dato_sanitizado = sanitizar_flotante(personaje[clave])
                if dato_sanitizado > 0:
                    dato_normalizado = True
                    
            case "entero":
                dato_sanitizado = sanitizar_entero(personaje[clave])
                if dato_sanitizado > 0:
                    dato_normalizado = True
            case _:
                print("Tipo de dato no renocido")
                        
    if dato_normalizado:
        personaje[clave] = dato_sanitizado

    return dato_normalizado


# Auxiliar Punto 3.5
def normalizar_dato(personaje, clave, tipo_dato):
    '''
    En caso de que haya un error al normalizar, se informara el personaje
    y el dato que provoco el error, eso no detendra la normalizacion de los
    datos de los demas personajes
    '''
    dato_normalizado = sanitizar_dato(personaje, clave, tipo_dato)
    if not dato_normalizado:
         print("Error al normalizar {0} de {1}".format(clave,personaje["nombre"]))
# Punto 3.5
def stark_normalizar_datos(personajes: list):
    '''
    Parametros:
    Una lista de diccionarios con los datos de los personajes

    Validara si la lista pasada como parametro tiene almenos un elemento
    Normaliza los datos de los personajes a traves de las funciones anteriores
    Despues de terminar de normalizar los datos, imprimira un mensaje
    Informa en caso de error
    '''
    if type(personajes) == type([]) and len(personajes) > 0:
        
        for personaje in personajes:
            normalizar_dato(personaje, "altura", "flotante")
            normalizar_dato(personaje, "peso", "flotante")
            normalizar_dato(personaje, "fuerza", "entero")
            normalizar_dato(personaje, "color_ojos", "string")
            normalizar_dato(personaje, "color_pelo", "string")
            normalizar_dato(personaje, "inteligencia", "string")

        print("Datos normalizados")
    else:
        print("Error, el parametro dado no es una lista")



#-------- Cuarta Parte --------#

# Punto 4.1
def generar_indice_nombres(personajes: list) -> list:
    '''
    Parametros:
    Una lista de diccionarios con los datos de los personajes

    La funcion almacenara cada palabra de todos los nombres en una 
    nueva lista, para hacer esto validara si el parametro pasado es una
    lista con algun elemento y tambien si suss elementos son un diccionario 
    con la clave 'nombre'

    Retorna:
    La lista de palabras
    Nada en caso de error
    '''
    retornar_lista = True
    if type(personajes) == type([]) and len(personajes) > 0:

        validacion_diccionario = True
        for personaje in personajes:
            if type (personaje) != type({}) or not("nombre" in personaje.keys()):
                validacion_diccionario = False
                break

        if validacion_diccionario:
            lista_palabras = []
            for personaje in personajes:
                palabras_nombre = re.findall("[a-zA-Z]+",personaje["nombre"])
                for palabra in palabras_nombre:
                    lista_palabras.append(palabra)
        else:
            retornar_lista = False
    else:
        retornar_lista = False

    if retornar_lista:
        return lista_palabras
    else:
        print("El origen de datos no contiene el formato correcto")       
    

# Punto 4.2
def stark_imprimir_indice_nombre(personajes: list):
    '''
    Parametros:
    Una lista de diccionarios con los datos de los personajes

    Imprimira un mensaje con todas las palabras de los nombres
    separadas por un guion (-)
    '''
    lista_palabras = generar_indice_nombres(personajes)
    if lista_palabras != None:
        mensaje_palabras_nombres = "-".join(lista_palabras)
        print(mensaje_palabras_nombres)



#-------- Quinta Parte --------#

# Punto 5.1
def centimetro_a_metro(numero_cm: float)-> float:
    '''
    Parametros:
    Un numero flotante que representa una medida en centimetros

    La funcion dividira por 100 al parametro recibido para que mida
    en metros.

    Retorna:
    El numero flotante convertido
    -1 En caso que el numero no sea mayor a 0
    '''
    if (type(numero_cm) == float or type(numero_cm) == int) and numero_cm > 0:
        numero_metros = numero_cm / 100
        return numero_metros
    else:
        return -1

    
# Punto 5.2
def generar_separador(patron: str, largo: int, imprimir = True) -> str:
    '''
    Parametros:
    - String con 1 a 2 caracteres representando el patron del separador
    - Entero representando el largo del separador
    - Un booleano que determina si imprimos el separador antes de retornarlo

    La funcion creara un string que representa al separador, que se genera
    en funcion de los parametros patron y largo.

    Retorna:
    - El string separador
    - 'N/A' En caso de haber algun error
    '''
    separador = "N/A"
    if type(largo) == int and largo > 0 and largo < 236:

        if re.search("^.{1,2}$", patron) != None:
            separador = ""
            while len(separador) < largo:
                separador += patron

    if imprimir:
        print(separador)

    return separador
    

# Punto 5.3
def generar_encabezado(titulo: str) -> str:
    '''
    Parametros:
    - String que representa el titulo del encabezado

    Todas las letras del titulo se pasaran a mayuscula, se generara
    un string que represente al titulo entre dos separadores (el encabezado)

    Retorna:
    - El string encabezado
    '''
    titulo = titulo.upper()
    separador = generar_separador("*",60, False)
    encabezado = separador + "\n" + titulo + "\n" + separador 
    return encabezado
    

# Punto 5.4
def imprimir_ficha_personaje(personaje: dict):
    '''
    Parametros:
    - Un diccionario con los datos de un personaje

    Imprime un string en forma de ficha que representa 
    varios datos del personaje. La altura del personaje
    se representa en metros
    '''
    altura_personaje = centimetro_a_metro(personaje["altura"])
    
    datos_principales = generar_encabezado("Datos principales")
    datos_principales += "\
            \nNombre del heroe:       {0} ({4})\
            \nIdentidad secreta:      {1}\
            \nConsultora:             {2}\
            \nCódigo de heroe:        {3}\
            \n".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["codigo"], personaje["iniciales"])

    fisico = generar_encabezado("Fisico")
    fisico += "\
            \nAltura:                 {0:.2f} Metros\
            \nPeso:                   {1} KG\
            \nFuerza:                 {2}\
            \n".format(altura_personaje, personaje["peso"], personaje["fuerza"])

    señas_particulares = generar_encabezado("Señas particulares")
    señas_particulares += "\
            \nColor de ojos:          {0}\
            \nColor de pelos:         {1}\
            \n".format(personaje["color_ojos"], personaje["color_pelo"])

    ficha_del_heroe = datos_principales + fisico + señas_particulares
    print(ficha_del_heroe)


# Punto 5.5
def stark_navegar_fichas(personajes):
    '''
    Parametros:
    - Lista de diccionarios con datos del personaje correspondiente

    Mediante un menu de opciones permite navegar entre las
    fichas de los personajes. En caso de seleccionar 'S' se volvera
    al menu principal. Se informara si se elige una opcion no valida
    '''
    indice = 0
    while True:    
        imprimir_ficha_personaje(personajes[indice])
        opcion = input("[1] A la izquierda   [2] A la derecha   [S] Salir \n>> ")
        opcion = opcion.upper()

        match (opcion):

            case "1":
                indice -= 1
                
            case "2":
                indice += 1

            case "S":
                print("Volviendo al menu principal...")
                break
            
            case _:
                print("Ingrese una opcion valida!")
        
        if indice == len(personajes) or indice == -len(personajes):
            indice = 0


#-------- Sexta Parte --------#

# Punto 6.1
def imprimir_menu():
    '''
    Imprime las opciones del menu principal
    '''
    menu_principal = "\nOpciones:\
            \n1- Imprimir nombres de los personajes junto con sus iniciales\
            \n2- Generar codigo para cada personaje\
            \n3- Normalizar datos\
            \n4- Imprimir indice de nombres\
            \n5- Navegar fichas\
            \nS- Salir"

    print(menu_principal)


# Punto 6.2
def stark_menu_principal() -> str:
    '''
    Llama a la funcion imprimir_menu, luego de eso espera la eleccion
    del usuario

    Retorna:
    - Un string que representa la opcion del usuario
    '''
    imprimir_menu()
    opcion = input(">> ")

    return opcion


# Punto 6.3
def stark_marvel_app(personajes):
    '''
    Parametros:
    - Una lista de diccionarios con los datos del personaje correspondiente

    En funcion del dato ingresado por el usuario se llamaran
    a distintas funciones
    \nNota:
    - La opcion '3' solo se podra ejecutar una vez
    - La funcion de la opcion '5' solo se podra ejecutar cuando se hayan
      ejecutado las opciones '1', '2' y '3'
    '''
    iniciales = False
    codigos = False
    normalizados = False
    while True:
        opcion = stark_menu_principal()
        opcion = opcion.upper()
        match opcion:
            case "1":
                stark_imprimir_nombres_con_iniciales(personajes)
                iniciales = True

            case "2":
                stark_generar_codigos_personaje(personajes)
                codigos = True

            case "3":
                if not normalizados:
                    stark_normalizar_datos(personajes)
                    normalizados = True
                else:
                    print("Los datos ya estan normalizados!")

            case "4":
                stark_imprimir_indice_nombre(personajes)

            case "5":
                if iniciales and codigos and normalizados:
                    stark_navegar_fichas(personajes)
                else:
                    print("Antes de navegar las fichas se deben seleccionar las opciones 1, 2 y 3")

            case "S":
                print("Adios!")
                break
            
            case _:
                print("Ingrese una opcion correcta")
        



stark_marvel_app(lista_personajes)