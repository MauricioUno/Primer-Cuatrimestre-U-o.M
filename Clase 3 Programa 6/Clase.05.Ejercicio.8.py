# Mauricio Uño Ejercicio 8

from data_stark import lista_personajes


def stark_normalizar_datos(lista: list, clave: str, tipo_de_casteo: type): 


    if type (lista) == type ([]) and len(lista) > 0 and type(clave) == type("") and type(tipo_de_casteo) == type(type):
        datos_normalizados = 0
        for personaje in lista:
            if type(personaje[clave]) == type(""):
                personaje[clave] = tipo_de_casteo(personaje[clave])
                datos_normalizados += 1

        if datos_normalizados > 0:
            print("Cantidad de datos '{0}' normalizados : {1}".format(clave, datos_normalizados))
        else:
            print("Ningun dato '{0}' fue normalizado".format(clave))


    else:
        print ("ESTO NO ES UNA LISTA!")
                

stark_normalizar_datos(lista_personajes, "altura", float)
stark_normalizar_datos(lista_personajes, "peso", float)
stark_normalizar_datos(lista_personajes, "fuerza", int)
#print(lista_personajes)