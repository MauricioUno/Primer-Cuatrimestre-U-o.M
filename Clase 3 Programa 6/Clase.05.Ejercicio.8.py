# Mauricio Uño Ejercicio 8

from data_stark import lista_personajes

def casteo_de_datos(diccionario_datos, clave, tipo_a_castear):
    if type(diccionario_datos[clave]) == str:
                diccionario_datos[clave] = tipo_a_castear(diccionario_datos[clave])
                return True

def stark_normalizar_datos(lista):

    if len(lista) > 0:
        datos_modificados = False
        for diccionario in lista:
            datos_modificados = casteo_de_datos(diccionario, "altura", float)
            datos_modificados = casteo_de_datos(diccionario, "peso", float)
            datos_modificados = casteo_de_datos(diccionario, "fuerza", int)
        if datos_modificados:
            print("Se modificaron datos!")
        else:
            print("No se modificaron datos")
    else:
        print ("LA LISTA ESTA VACIA!")
                


stark_normalizar_datos(lista_personajes)