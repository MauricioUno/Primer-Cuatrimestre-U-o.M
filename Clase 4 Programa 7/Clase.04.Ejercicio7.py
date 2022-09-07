# Uño Mauricio Ejercicio 7

from data_stark import lista_personajes

# Casteo de todos los datos numericos (estan todos en str)
for datos_personaje in lista_personajes:
    # La altura se pasa a metros
    datos_personaje["altura"] = float(datos_personaje["altura"]) / 100
    datos_personaje["peso"] = float (datos_personaje["peso"])
    datos_personaje["fuerza"] = int (datos_personaje["peso"])


# Lista de nombres segun el genero elegido (Punto A y B)
def lista_de_nombres_genero(genero_elegido):
    mensaje = ""    
    for datos_personaje in lista_personajes:
        if datos_personaje["genero"] == genero_elegido:
            mensaje += "{0}\n".format(datos_personaje["nombre"])

    print (mensaje)
            

#  Altura maxima del genero elegido (Punto C y D)
def calculo_altura_max_genero(genero_elegido):
    flag_primer_personaje = True
    for datos_personaje in lista_personajes:
        if datos_personaje["genero"] == genero_elegido:
            if flag_primer_personaje or datos_personaje["altura"] > altura_maxima:
                altura_maxima = datos_personaje["altura"]
                flag_primer_personaje = False

    mensaje = "{0:.2f} metros".format(altura_maxima)

    print (mensaje)


# Altura minima del genero elegido (Punto E y F)
def calculo_altura_min_genero(genero_elegido):
    flag_primer_personaje = True
    for datos_personaje in lista_personajes:
        if datos_personaje["genero"] == genero_elegido:
            if flag_primer_personaje or datos_personaje["altura"] < altura_minima:
                altura_minima = datos_personaje["altura"]
                flag_primer_personaje = False

    mensaje = "{0:.2f} metros".format(altura_minima)

    print (mensaje)

# Promedio de altura del genero elegido (Punto G y H)
def promedio_altura_genero (genero_elegido):
    acumulador_altura = 0
    contador_personajes = 0
    for datos_personaje in lista_personajes:
        if datos_personaje["genero"] == genero_elegido:
            acumulador_altura += datos_personaje["altura"]
            contador_personajes += 1
        
    promedio_altura = acumulador_altura / contador_personajes
    mensaje = "{0:.2f} metros".format(promedio_altura)

    print (mensaje)


# Datos de los personajes mas altos y mas bajos de cada genero (I)
def datos_personajes_altura_max_min():
    flag_primer_masculino = True
    flag_primer_femenino = True
    for datos_personaje in lista_personajes:

        if datos_personaje["genero"] == "M":
            if flag_primer_masculino:
                masculino_mas_alto = datos_personaje
                masculino_mas_bajo = datos_personaje
                flag_primer_masculino = False
            else:
                if(datos_personaje["altura"] > masculino_mas_alto["altura"]):
                    masculino_mas_alto = datos_personaje
                elif(datos_personaje["altura"] < masculino_mas_bajo["altura"]):
                    masculino_mas_bajo = datos_personaje

        elif datos_personaje["genero"] == "F":
            if flag_primer_femenino:
                femenino_mas_alto = datos_personaje
                femenino_mas_bajo = datos_personaje
                flag_primer_femenino = False
            else:
                if(datos_personaje["altura"] > femenino_mas_alto["altura"]):
                    femenino_mas_alto = datos_personaje
                elif(datos_personaje["altura"] < femenino_mas_bajo["altura"]):
                    femenino_mas_bajo = datos_personaje

    mensaje = "El personaje masculino mas alto es {0}".format(masculino_mas_alto["nombre"])
    mensaje += "\nEl personaje masculino mas bajo es {0}".format(masculino_mas_bajo["nombre"])
    mensaje += "\nEl personaje femenino mas alto es {0}".format(femenino_mas_alto["nombre"])
    mensaje += "\nEl personaje femenino mas bajo es {0}".format(femenino_mas_bajo["nombre"])
    
    print (mensaje)

# Cantidad de personajes con los distintos tipos del dato elegido (J, K y L)
def cant_personajes_por_tipo_de(dato):
    contadores_dato = {}
    for datos_personaje in lista_personajes:
        datos_personaje[dato] = datos_personaje[dato].lower()
        if datos_personaje[dato] == "":
            datos_personaje[dato] = "No definido"
        contadores_dato [datos_personaje[dato]] = 0
    
    for datos_personaje in lista_personajes:
        contadores_dato [datos_personaje[dato]] += 1

    mensaje = ""
    for tipo in contadores_dato:
        cantidad = contadores_dato[tipo]
        mensaje += "Tipo '{0}': {1}\n".format(tipo, cantidad)

    print (mensaje)

# Lista de los personajes ordenados por los tipos del dato elegido (M, N y O)
def personajes_ordenados_por_tipo_de(dato):
    
    diccionario_tipos_de_dato = {}
    for datos_personaje in lista_personajes:
        datos_personaje[dato] = datos_personaje[dato].lower()
        if datos_personaje[dato] == "":
            datos_personaje[dato] = "No definido"
        diccionario_tipos_de_dato[datos_personaje[dato]] = 0


    for tipo_de_dato in diccionario_tipos_de_dato:
        
        personajes_tipo_de_dato = []
        for datos_personaje in lista_personajes:
            if datos_personaje[dato] == tipo_de_dato:
                personajes_tipo_de_dato.append(datos_personaje["nombre"])

        diccionario_tipos_de_dato[tipo_de_dato] = personajes_tipo_de_dato
    
    mensaje = ""
    for tipo_de_dato in diccionario_tipos_de_dato:
        personajes = diccionario_tipos_de_dato[tipo_de_dato]
        mensaje += "\nTipo '{0}':\n".format(tipo_de_dato)
        for personaje in personajes:
            mensaje += personaje + "\n"
        
    print (mensaje)

        
while True:
    opcion = input  (
                    "\nOPCIONES:\n"
                    "'A': Lista de personajes masculinos \n"
                    "'B': Lista de personajes femeninos \n"
                    "'C': Altura maxima de personajes masculinos\n"
                    "'D': Altura maxima de personajes femeninos\n"
                    "'E': Altura minima de personajes masculinos\n"
                    "'F': Altura minima de personajes femeninos\n"
                    "'G': Promedio de altura de personajes masculinos\n"
                    "'H': Promedio de altura de personajes femeninos\n"
                    "'I': Nombres de los personajes con mayor y menor altura de cada genero\n"
                    "'J': Cantidad de personajes con cada tipo de color de ojos\n"
                    "'K': Cantidad de personajes con cada tipo de color de pelo\n"
                    "'L': Cantidad de personajes con cada tipo de color de inteligencia\n"
                    "'M': Lista de personajes ordenados por color de ojos\n"
                    "'N': Lista de personajes ordenados por color de pelo\n"
                    "'O': Lista de personajes ordenados por inteligencia\n"
                    "'S': Salir del menu\n"
                    "Ingrese su opcion: "
                    )
    if opcion == "A":
        print("Lista de personajes masculinos: ")
        lista_de_nombres_genero("M")

    elif opcion == "B":
        print("Lista de personajes femeninos: ")
        lista_de_nombres_genero("F")

    elif opcion == "C":
        print("Altura maxima de personajes masculinos: ")
        calculo_altura_max_genero("M")

    elif opcion == "D":
        print("Altura maxima de personajes femeninos: ")
        calculo_altura_max_genero("F")

    elif opcion == "E":
        print("Altura minima de personajes masculinos: ")
        calculo_altura_min_genero("M")

    elif opcion == "F":
        print("Altura minima de personajes femeninos: ")
        calculo_altura_min_genero("F")

    elif opcion == "G":
        print("Promedio altura personajes masculinos: ")
        promedio_altura_genero("M")

    elif opcion == "H":
        print("Promedio altura personajes femeninos: ")
        promedio_altura_genero("F")

    elif opcion == "I":
        print("Datos de los personajes con mayor y menor altura de cada genero: ")
        datos_personajes_altura_max_min()

    elif opcion == "J":
        print("Cantidad de personajes por tipo de color de ojo")
        cant_personajes_por_tipo_de("color_ojos")

    elif opcion == "K":
        print("Cantidad de personajes por tipo de color de pelo")
        cant_personajes_por_tipo_de("color_pelo")

    elif opcion == "L":
        print("Cantidad de personajes por tipo inteligencia")
        cant_personajes_por_tipo_de("inteligencia")

    elif opcion == "M":
        print("Lista de personajes ordenados por color de ojos")
        personajes_ordenados_por_tipo_de("color_ojos")

    elif opcion == "N":
        print("Lista de personajes ordenados por color de pelo")
        personajes_ordenados_por_tipo_de("color_pelo")

    elif opcion == "O":
        print("Lista de personajes ordenados por inteligencia")
        personajes_ordenados_por_tipo_de("inteligencia")

    elif opcion == "S":
        print("ADIOS!")
        break
    else:
        print("INGRESE UNA OPCION VALIDA!")

