''' Uño Mauricio, Parcial a Python
Enunciado:
Una casa de computación que se especializa en venta de insumos importados desea calcular 
ciertas métricas en base a las ventas de sus productos. Se ingresa de cada venta: (Ingresa mínimo 5 ventas)
-Nombre del producto.
-Género: (Memorias - Discos - Motherboards)
-Tipo de Venta: (Online - Local)
-Importe: (No pueden ser números negativos ni mayor a los 30000)
Se pide:
A- El más barato de “Discos” con su importe .
B- De la venta más cara, el nombre del producto.
C- El importe promedio del total.
D- La cantidad de ventas que sean de “Memorias” y cuesten menos de $850.
'''
import re
from functools import reduce
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


def exigir_dato_valido(texto_input: str, texto_error: str, reg_ex):
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


acumulador_importe = 0
lista_ventas = []
while True:
    print("\nCompra número {0}".format(len(lista_ventas) + 1))
    diccionario_ventas = {}

    diccionario_ventas["producto"] = exigir_dato_valido("Ingrese el nombre del producto: ", 
                                                        "Error! Ingrese un nombre!: ", 
                                                        "^[a-z A-Z]+$")

    diccionario_ventas["genero"] = exigir_dato_valido("Ingrese el genero del producto (Memoria/Disco/Motherboard): ", 
                                                    "Error! Ingrese un genero! (Memoria/Disco/Motherboard): ", 
                                                    "^(memoria|disco|motherboard)$")

    diccionario_ventas["venta"] = exigir_dato_valido("Ingrese el tipo de venta (Online/Local): ", 
                                                    "Error! Ingrese un tipo de venta! (Online/Local): ", 
                                                    "^(online|local)$")

    diccionario_ventas["importe"] = float(exigir_dato_valido("Ingrese el importe de la venta (Maximo 30000): ", 
                                                            "Error! Ingrese un importe dentro del rango (Maximo 30000): ",
                                                            "^[0-9]+(\.[0-9]+)?$"))
    

    acumulador_importe += diccionario_ventas["importe"]
    lista_ventas.append(diccionario_ventas)


    if (len(lista_ventas) > 1):
        confirmacion = input ("Ingrese 'S' para dejar de cargar ventas: ")
        if re.search("[sS]", confirmacion):
            break
    

importe_maximo = reduce(lambda maximo, venta : venta if venta["importe"] > maximo ["importe"] else maximo, lista_ventas)
ventas_discos = list(filter(lambda venta : venta["genero"] == "disco", lista_ventas))
ventas_memorias_baratas = list(filter(lambda venta : venta["genero"] == "memoria" and venta["importe"] < 850, lista_ventas))
promedio_importe_por_venta = acumulador_importe / len(lista_ventas)


mensaje_datos_ventas = "\nDatos de las ventas registradas: "
mensaje_datos_ventas += "\nEl producto del importe mas caro es '{0}' con un precio de {1}".format(importe_maximo["producto"], importe_maximo["importe"])
mensaje_datos_ventas += "\nEl promedio de importe por venta es de {0:.2f}".format(promedio_importe_por_venta)

if len(ventas_discos) > 0:
    disco_minimo = reduce(lambda minimo, venta : venta if venta["importe"] < minimo ["importe"] else minimo, ventas_discos)
    mensaje_datos_ventas += "\nEl disco con menor importe es '{0}' con un precio de {1}".format(disco_minimo["producto"], disco_minimo["importe"])
else:
    mensaje_datos_ventas += "\nNo se compro ningun disco"

if len(ventas_memorias_baratas) > 0:
    mensaje_datos_ventas += "\nLa cantidad de ventas de memorias con un precio menor a 850 es de: {0}".format(len(ventas_memorias_baratas))
else:
    mensaje_datos_ventas += "\nNo se vendieron memorias con un precio menor a 850"

print(mensaje_datos_ventas)