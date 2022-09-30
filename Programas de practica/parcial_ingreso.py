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



ventas_discos = False
acumulador_importe = 0
contador_ventas = 0
contador_ventas_memoria = 0


while True:

    nombre_producto = ingresar_dato ("Ingrese el nombre del producto: ", "^[a-z A-Z]+$")
    while nombre_producto == -1:
        nombre_producto = ingresar_dato ("Error! Ingrese un nombre!: ", "^[a-z A-Z]+$")


    genero_producto = ingresar_dato ("Ingrese el genero del producto (Memoria/Disco/Motherboard): ", "^(memoria|disco|motherboard)$")
    while genero_producto == -1:
        genero_producto = ingresar_dato ("Error! Ingrese un genero! (Memoria/Disco/Motherboard): ", "^(memoria|disco|motherboard)$")


    tipo_de_venta = ingresar_dato ("Ingrese el tipo de venta (Online/Local): ", "^(online|local)$")
    while tipo_de_venta == -1:
        tipo_de_venta = ingresar_dato ("Error! Ingrese un tipo de venta! (Online--Local): ", "^(online|local)$")


    importe_producto = float(ingresar_dato("Ingrese el importe de la venta (Maximo 30000): ", "^[0-9]+(\.[0-9]+)?$"))
    while importe_producto < 1 or importe_producto > 30000:
        importe_producto = float(ingresar_dato("Error! Ingrese un importe dentro del rango (Maximo 30000): ", "^[0-9]+(\.[0-9]+)?$"))
        

    
    if contador_ventas == 0 or importe_producto > importe_maximo:
        importe_maximo = importe_producto
        nombre_maximo = nombre_producto

    match genero_producto:
        
        case "disco":
            if ventas_discos == False or importe_producto < importe_minimo_discos:
                importe_minimo_discos = importe_producto
                nombre_minimo_discos = nombre_producto
                ventas_discos = True

        case "memoria":
            if importe_producto < 850:
                contador_ventas_memoria += 1

        case "motherboard":
            pass

    acumulador_importe += importe_producto
    contador_ventas += 1

    if (contador_ventas > 1):
        confirmacion = input ("Ingrese 'S' para dejar de cargar ventas: ")
        if confirmacion == 'S':
            break
    


promedio_importe_por_venta = acumulador_importe / contador_ventas

mensaje_datos_ventas = "El producto del importe mas caro es '{0}' con un precio de {1}".format(nombre_maximo, importe_maximo)
mensaje_datos_ventas += "\nEl promedio de importe por venta es de {0:.2f}".format(promedio_importe_por_venta)

if ventas_discos:
    mensaje_datos_ventas += "\nEl disco con menor importe es '{0}' con un precio de {1}".format(nombre_minimo_discos,importe_minimo_discos)
else:
    mensaje_datos_ventas += "\nNo se compro ningun disco"

if contador_ventas_memoria > 0:
    mensaje_datos_ventas += "\nLa cantidad de ventas de memorias con un precio menor a 850 es de: {0}".format(contador_ventas_memoria)
else:
    mensaje_datos_ventas += "\nNo se vendieron memorias con un precio menor a 850"


print(mensaje_datos_ventas)