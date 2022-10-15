from copy import deepcopy
persona_1 = {
    "nombre": "Maximo",
    "apellido": "Cozzetti",
    "domicilio": {
        "calle": "Av. Mitre",
        "altura": 750,
        "localidad": "Avellaneda",
        "barrio": "Avellaneda Centro",
        "cod_postal" : "C1870"
    },    
    "telefonos": [
        {
            "etiqueta": "fijo",
            "cod_pais": "+54",
            "cod_area": "11",
            "numero": "4201-4133"
        },
        {
            "etiqueta": "movil",
            "cod_pais": "+54",
            "cod_area": "11",
            "nro": "4353-0220"
        }
    ],
    
    "identificacion": {
        "tipo": "dni",
        "nro": "30.505.003"
    }
}


# Punto 1: Modificar la calle y altura de 'persona_1' por RamÃ³n Franco 5050. 



# Punto 2: Verificar si existe un numero de telefono con la etiqueta 'trabajo'. Si no existe, entonces crearlo con el valor +54 11 4201-4133. Caso contrario actualizarlo


# Punto 3: imprimir los datos completos de persona_1 recorriendo todas sus claves y valores


# Punto 4: 
#   Obtener el id de 'persona_1' y de 'persona_2'. 
#   Comprarlos, si son iguales imprirmir: 
#       "'ID de persona_1 es: id_persona_1 y el ID de persona_2 es: id_persona_2 entonces son el mismo diccionario' caso contrario imprimir "No son el mismo diccionario"
#   Modificar el nombre y apellido de persona_1 por Emilio Ravenna
#   Imprimir persona_1 y persona_2 y analizar los resultados
persona_2 = persona_1



# Punto 5: 
#   Crear persona_3 a partir de una copia superficial de persona_1
#   Modificar nombre y apellido a persona_3 por Gabriel Medina
#   Modificar el nro de documento por 28.307.401
#   Imprimir persana_1 y persona_3 y analizar los resultados



# Punto 6: 
#   Crear persona_4 a partir de una copia profunda de persona_1
#   Modificar el nombre y apellido por Mario Santos
#   Modificar el nro de documento por: 29.407.901
#   Imprimir persana_1 y persona_3 y analizar los resultados

def punto_uno():
    persona_1["domicilio"].update({"calle": "Raman Franco" , "altura": 5050 })

def punto_dos():
    telefono_existente = False
    for telefono in (persona_1["telefonos"]):
        if ("etiqueta", "trabajo") in telefono.items():
            telefono.update({"etiqueta": "trabajo", "cod_pais": "+54", "cod_area": "11", "numero": "4201-4133"})
            telefono_existente = True

    if not telefono_existente:
            persona_1["telefonos"].append({"etiqueta": "trabajo", "cod_pais": "+54", "cod_area": "11", "numero": "4201-4133"})

def imprimir_items_diccionario(diccionario: dict):
     if type(diccionario) == type ({}):
        for dato in diccionario.items():
            print(dato)

def punto_tres():
    for dato in persona_1.items():
        if type(dato[1]) == type ([]):
            print("\nValores clave {0}: ".format(dato[0].capitalize()))
            for indice,otro_dato in enumerate(dato[1]):
                print("Elemento {0}: ".format(indice))
                imprimir_items_diccionario(otro_dato)

        elif type(dato[1]) == type ({}):
            print("\nValores clave {0}: ".format(dato[0].capitalize()))    
            imprimir_items_diccionario(dato[1])
        else:
            print(dato)

def punto_cuatro():
    id_persona_1 = id(persona_1)
    id_persona_2 = id(persona_2)

    if id_persona_1 == id_persona_2:
        print("El ID de persona_1 es igual al ID de persona_2, por lo tanto hace referencia al mismo diccionario")
    else:
        print("No son el mismo diccionario")

    persona_1.update({"nombre": "Emilio", "apellido": "Ravenna"})

    print(persona_1)
    print(persona_2)
    # Los 'dos' diccionarios cambian el valor de las claves nombre y apellido

def punto_cinco():
    persona_3 = persona_1.copy()
    persona_3.update({"nombre": "Gabriel", "apellido": "Medina"})
    persona_3["identificacion"].update({"nro": "28.307.401"})

    print(persona_1)
    print(persona_3)
    # Los valores del diccionario que sean objetos iterables no se copian, si no que se les pasa la referencia

def punto_seis():
    persona_4 = deepcopy(persona_1)
    persona_4.update({"nombre": "Mario", "apellido": "Santos"})
    persona_4["identificacion"].update({"nro": "29.407.901"})

    print(persona_1)
    print(persona_4)
    # Se crea una copia completa de todo el contenido dentro del diccionario