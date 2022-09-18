# Uño Mauricio Ejercicio 6

from data_stark import lista_personajes

# Casteo de todos los datos numericos (estan todos en str)
for datos_personaje in lista_personajes:
    datos_personaje["altura"] = float(datos_personaje["altura"]) / 100
    datos_personaje["peso"] = float (datos_personaje["peso"])
    datos_personaje["fuerza"] = int (datos_personaje["fuerza"])

# Lista de nombres (B)
def lista_nombre_personajes():
    for datos_personaje in lista_personajes:
        print("Nombre: {0}".format(datos_personaje["nombre"]))

# Lista nombres y alturas (C)
def lista_nombre_y_altura():
    for datos_personaje in lista_personajes:
        print("Nombre: {0}  Altura: {1:.2f} M".format(datos_personaje["nombre"], datos_personaje["altura"]))


#  Altura maxima (D)
def calculo_altura_maxima():
    altura_maxima = lista_personajes[0]["altura"]
    for datos_personaje in lista_personajes:
        if datos_personaje["altura"] > altura_maxima:
            altura_maxima = datos_personaje["altura"]

    print("Altura maxima: {0:.2f} M".format(altura_maxima))


# Altura minima (E)
def calculo_altura_minima():
    altura_minima = lista_personajes[0]["altura"]
    for datos_personaje in lista_personajes:
        if datos_personaje["altura"] < altura_minima:
            altura_minima = datos_personaje["altura"]

    print("Altura minima: {0:.2f} M".format(altura_minima))


# Altura Promedio de los personajes (F)
def calculo_promedio_altura():
    acumulador_alturas = 0
    contador_personajes = len(lista_personajes)
    for datos_personaje in lista_personajes:
        acumulador_alturas += datos_personaje["altura"]

    promedio_alturas = acumulador_alturas / contador_personajes
    print("Promedio de altura: {0:.2f} Metros".format(promedio_alturas))

# Datos de personajes correspondientes a la altura maxima y minima (G)
def datos_altura_max_y_min():
    datos_altura_maxima = lista_personajes[0]
    datos_altura_minima = lista_personajes[0]
    for datos_personaje in lista_personajes:
        if datos_personaje["altura"] > datos_altura_maxima["altura"]:
            datos_altura_maxima = datos_personaje

        elif datos_personaje["altura"] < datos_altura_minima["altura"]:
            datos_altura_minima = datos_personaje

    print("Nombre personaje mas alto: {0}  Altura: {1:.2f} M".format(datos_altura_maxima["nombre"], datos_altura_maxima["altura"]))
    print("Nombre personaje mas bajo: {0}  Altura: {1:.2f} M".format(datos_altura_minima["nombre"], datos_altura_minima["altura"]))


# Datos de personajes correspondientes al peso maximo y minimo (H)
def datos_peso_max_y_min():
    datos_peso_maximo = lista_personajes[0]
    datos_peso_minimo = lista_personajes[0]
    for datos_personaje in lista_personajes:

        if datos_personaje["peso"] > datos_peso_maximo["peso"]:
            datos_peso_maximo = datos_personaje
        
        elif datos_personaje["peso"] < datos_peso_minimo["peso"]:
            datos_peso_minimo = datos_personaje

    print("Nombre personaje mas pesado: {0}  peso: {1:.2f} KG".format(datos_peso_maximo["nombre"], datos_peso_maximo["peso"]))
    print("Nombre personaje menos pesado: {0}  peso: {1:.2f} KG".format(datos_peso_minimo["nombre"], datos_peso_minimo["peso"]))


while True:
    opcion = input  (
                    "\nOPCIONES:\n"
                    "'B': Lista de nombres\n"
                    "'C': Lista de nombres y alturas correspondientes\n"
                    "'D': Altura maxima de la lista\n"
                    "'E': Altura minima de la lista\n"
                    "'F': Promedio de altura\n"
                    "'G': Nombre y altura de los personajes con mayor altura y menor altura\n"
                    "'H': Nombre y peso del personajes con mayor peso y menor peso\n"
                    "'S': Salir del menu\n"
                    "Ingrese su opcion: "
                    )
    if opcion == "B":
        lista_nombre_personajes()
    elif opcion == "C":
        lista_nombre_y_altura()
    elif opcion == "D":
        calculo_altura_maxima()
    elif opcion == "E":
        calculo_altura_minima()
    elif opcion == "F":
        calculo_promedio_altura()
    elif opcion == "G":
        datos_altura_max_y_min()
    elif opcion == "H":
        datos_peso_max_y_min()
    elif opcion == "S":
        print("ADIOS!")
        break
    else:
        print("INGRESE UNA OPCION VALIDA!")

