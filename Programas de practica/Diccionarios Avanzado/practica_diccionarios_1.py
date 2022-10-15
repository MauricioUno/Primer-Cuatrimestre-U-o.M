import re
lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'


# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)


# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios


# Punto 4: imprimir el listado de frutas (solo su nombre)


# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

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



def punto_uno():
    producto_buscado = input("Ingrese el producto que desea buscar: ")
    datos_producto = lista_precios.get(producto_buscado)
    if datos_producto != None:
        print("Precio: {0} | Stock: {1}".format(datos_producto["precio"], datos_producto["stock"]))
    else:
        print("El producto no se encuentra en la lista")

def punto_dos():
    producto_buscado = input("Ingrese el producto que desea comprar: ")
    datos_producto = lista_precios.get(producto_buscado)

    if datos_producto != None:
        print("Precio: {0} | Stock: {1}".format(datos_producto["precio"], datos_producto["stock"]))
        
        cantidad = int (ingresar_dato("Ingrese la cantidad a llevar({0}): ".format(datos_producto["unidad_medida"]), "^[0-9]+$" ))
        if validar_rango_entero(cantidad, 1, datos_producto["stock"]):
            print("El costo de la compra es: {0}".format(datos_producto["precio"] * cantidad))
        else:
            print("Cantidad ingresada no valida!")
        
    else:
        print("El articulo no se encuentra en la lista")

def punto_tres():
    fruta_ingresada = exigir_dato_valido("Ingrese una nueva fruta a la lista de productos: ", "Error! Ingrese un producto!: ", "^[a-z A-Z]+$")
    diccionario_producto = {fruta_ingresada : {}}

    diccionario_producto[fruta_ingresada]["precio"] = 0
    while diccionario_producto[fruta_ingresada]["precio"] < 1:
        diccionario_producto[fruta_ingresada]["precio"] = int(exigir_dato_valido("Ingrese el precio de la fruta: ", 
                                                                                "Error! Ingrese un precio valido!: ", "^[0-9]+$"))


    diccionario_producto[fruta_ingresada]["unidad_medida"] = exigir_dato_valido("Ingrese la unidad de medida (kg/unidad): ", 
                                                                                "Error! Ingrese kg o unidad: ", "^(kg|unidad)$")

    diccionario_producto[fruta_ingresada]["stock"] = 0
    while diccionario_producto[fruta_ingresada]["stock"] < 1:
        diccionario_producto[fruta_ingresada]["stock"] = int(exigir_dato_valido("Ingrese el stock de la fruta: ", 
                                                                                "Error! Ingrese un stock valido!: ", "^[0-9]+$"))
    
    lista_precios.update(diccionario_producto)
    print("Nueva fruta agregada a la lista!")

def punto_cuatro():  
    for fruta in lista_precios.keys():
        print(fruta)

def punto_cinco():
    producto_buscado = input("Ingrese el producto que desea eliminar: ")
    datos_producto = lista_precios.get(producto_buscado)
    if datos_producto != None:
        lista_precios.pop(producto_buscado)
        print("Producto eliminado de la lista")
    else:
        print("El articulo no se encuentra en la lista")
