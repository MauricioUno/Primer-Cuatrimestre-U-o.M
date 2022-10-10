import re

#-------- Validar lista con diccionarios ---------#
def validar_lista_con_diccionarios(lista: list) -> bool:
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
    if type(lista) == type([]) and len(lista) > 0:
        for elemento in lista:
            if type(elemento) != type({}):
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


#-------- Validar Rango Entero ---------#
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


#-------- Entrar en un while hasta que se ingrese el dato correcto ---------#
def exigir_dato_valido(texto_input: str, texto_error: str, reg_ex) -> str:
    '''
    Parametros:
    - El texto que le informara al usuario que debe ingresar
    - El texto que se mostrara en caso que el usuario ingrese algo
    no valido
    - La expresion regular que define las opciones validas

    Funcion:
    - Pedira un dato al usuario hasta que sea ingresado algo
    considerado valido en funcion de la expresion regular pasada
    como parametro

    Retorno:
    - El dato ingresado
    '''
    dato_ingresado = ingresar_dato(texto_input, reg_ex)
    while dato_ingresado == -1:
        dato_ingresado = ingresar_dato(texto_error, reg_ex)
    
    return dato_ingresado

