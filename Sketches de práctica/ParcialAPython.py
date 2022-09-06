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



ventas_discos = False
acumulador_importe = 0
contador_ventas = 0
contador_ventas_memoria = 0

while True:

    nombre_producto = input ("Ingrese el nombre del producto: ")
    while nombre_producto.isnumeric():
        nombre_producto = input ("Error! Ingrese un nombre!: ")


    genero_producto = input ("Ingrese el genero del producto (Memorias--Discos--Motherboards): ")
    genero_producto = genero_producto.lower()
    while (genero_producto != "memorias" and genero_producto != "discos" and genero_producto != "motherboards"):
        genero_producto = input ("Error! Ingrese un genero! (Memorias--Discos--Motherboards): ")
        genero_producto = genero_producto.lower()


    tipo_de_venta = input ("Ingrese el tipo de venta (Online--Local): ")
    tipo_de_venta = tipo_de_venta.lower()
    while (tipo_de_venta != "online" and tipo_de_venta != "local"):
        tipo_de_venta = input ("Error! Ingrese un tipo de venta! (Online--Local): ")
        tipo_de_venta = tipo_de_venta.lower()


    importe_producto = input ("Ingrese el importe de la venta (Maximo 30000): ")
    if importe_producto.isdecimal():
        importe_producto = int (importe_producto)
    while(type(importe_producto) != int or importe_producto < 1 or importe_producto > 30000):
        importe_producto = input ("Error! Ingrese un importe dentro del rango (Maximo 30000): ")
        if importe_producto.isdecimal():
            importe_producto = int (importe_producto)

    
    if contador_ventas == 0 or importe_producto > importe_maximo:
        importe_maximo = importe_producto
        nombre_maximo = nombre_producto

    match genero_producto:
        
        case "discos":
            if ventas_discos == False or importe_producto < importe_minimo_discos:
                importe_minimo_discos = importe_producto
                nombre_minimo_discos = nombre_producto
                ventas_discos = True

        case "memorias":
            if importe_producto < 850:
                contador_ventas_memoria += 1

        case "motherboards":
            pass

    acumulador_importe += importe_producto
    contador_ventas += 1

    if (contador_ventas > 1):
        confirmacion = input ("Ingrese 'S' para dejar de cargar ventas: ")
        if confirmacion == 'S':
            break
    


promedio_importe_por_venta = acumulador_importe / contador_ventas

mensaje_datos = "El producto del importe mas caro es '{0}' con un precio de {1}".format(nombre_maximo, importe_maximo)
mensaje_datos += "\nEl promedio de importe por venta es de {0:.2f}".format(promedio_importe_por_venta)

if ventas_discos:
    mensaje_datos += "\nEl disco con menor importe es '{0}' con un precio de {1}".format(nombre_minimo_discos,importe_minimo_discos)
else:
    mensaje_datos += "\nNo se compro ningun disco"

if contador_ventas_memoria > 0:
    mensaje_datos += "\nLa cantidad de ventas de memorias con un precio menor a 850 es de: {0}".format(contador_ventas_memoria)
else:
    mensaje_datos += "\nNo se vendieron memorias con un precio menor a 850"


print(mensaje_datos)