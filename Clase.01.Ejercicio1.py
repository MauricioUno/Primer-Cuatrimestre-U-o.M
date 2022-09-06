''' Uño Mauricio Ejericio 1
La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
    El tipo (validar "barbijo", "jabón" o "alcohol")
    El precio: (validar entre 100 y 300)
    La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
    La marca y el Fabricante.
    
Se debe informar lo siguiente:
    Del más caro de los barbijos, la cantidad de unidades y el fabricante.
    Del ítem con más unidades, el fabricante.
    Cuántas unidades de jabones hay en total.

'''

flag_barbijos = True
contador_jabones = 0
for i in range(5):

    # Validacion de las variables a utilizar
    tipo_ingresado = input ("Ingrese el tipo de producto (barbijo - jabon - alcohol): ")
    while ( tipo_ingresado != "barbijo" and tipo_ingresado != "jabon" and tipo_ingresado != "alcohol"):
        tipo_ingresado = input ("ERROR! INGRESE UN TIPO VALIDO! (barbijo - jabon - alcohol): ")
        
    precio_ingresado = input ("Ingrese el precio del producto (100 a 300): ")
    if precio_ingresado.isnumeric() == True :
        precio_ingresado = int(precio_ingresado)

    while ( (type(precio_ingresado) != int) or (precio_ingresado < 100) or (precio_ingresado > 300) ):
        precio_ingresado = input ("ERROR! INGRESE UN PRECIO VALIDO! (100 a 300): ")
        if precio_ingresado.isnumeric() == True :
            precio_ingresado = int(precio_ingresado)

    cantidad_ingresada = input ("Ingrese la cantidad que desea comprar: ")
    if cantidad_ingresada.isnumeric() == True :
        cantidad_ingresada = int(cantidad_ingresada)

    while ( (type(cantidad_ingresada) != int) or (cantidad_ingresada < 1) or (cantidad_ingresada > 1000) ):
        cantidad_ingresada = input ("ERROR! INGRESE UNA CANTIDAD VALIDA: ")
        if cantidad_ingresada.isnumeric() == True :
            cantidad_ingresada = int(cantidad_ingresada)

    marca_ingresada = input ("Ingrese la marca del producto: ")
    fabricante_ingresado = input ("Ingrese el fabricante del producto: ")

    # Punto B Item con mas unidades
    if (i == 0) or (cantidad_ingresada > cantidad_item_mas_vendido):
        tipo_item_mas_vendido = tipo_ingresado
        cantidad_item_mas_vendido = cantidad_ingresada
        fabricante_item_mas_vendido = fabricante_ingresado

    # Punto A El barbijo mas caro
    if tipo_ingresado == "barbijo":    
        if (flag_barbijos == True or precio_ingresado > precio_barbijo_caro):
                
            precio_barbijo_caro = precio_ingresado
            cantidad_barbijo_caro = cantidad_ingresada
            fabricante_barbijo_caro = fabricante_ingresado
            flag_barbijos = False

    # Punto C La cantidad de jabones comprados en total
    elif tipo_ingresado == "jabon":
        contador_jabones += cantidad_ingresada


mensajeMasVendido = "El tipo del item mas vendido es: " + tipo_item_mas_vendido 
mensajeMasVendido += "\nCon una cantidad de: " + str(cantidad_item_mas_vendido)
mensajeMasVendido += "\nSu fabricante es: " + fabricante_item_mas_vendido


if not flag_barbijos:
    mensajeBarbijos = "El barbijo mas caro tiene un precio de: " + str(precio_barbijo_caro)
    mensajeBarbijos += "\nSe compraron " + str(cantidad_barbijo_caro) + " unidades"
    mensajeBarbijos += "\nSu fabricante es: " + fabricante_barbijo_caro
else:
    mensajeBarbijos = "NO SE COMPRARON BARBIJOS!"

if contador_jabones > 0:
    mensajeJabones = "Se compraron " + str(contador_jabones) + " unidades de jabon"
else:
    mensajeJabones = "NO SE COMPRO NINGUN JABON!"

print (mensajeMasVendido + "\n" + mensajeBarbijos + "\n" + mensajeJabones)
