import funciones_lambda
"""
Modificar el menu y funcionalidades para que cumpla con lo siguiente:

0 - Castear las claves mass y heigt a entero usando [Map] (No sera una opcion del menu).
1 - Listar los personajes ordenados por altura [sort] [opc reverse]
2 - Mostrar el personaje mas alto de cada genero [Reduce] [Lambda]
3 - Ordenar los personajes por peso [sort] [opc reverse]
4 - Armar un buscador de personajes
5 - Filtrar personajes Femeninos [Filter] [Lambda]
6 - Filtrar personajes Masculinos [Filter] [Lambda]
7 - Filtrar personajes Sin Genero [Filter] [Lambda]
>> Nota: Si la key relacionada al genero no existe, buscar en la key 'data' y 
>> 'updatear' la key faltante con el valor correspondiente al genero, para que quede igual
>> que los diccionarios anteriores.
8 - Desordenar la lista de manera random y mostrar el ultimo de la lista [Shuffle]
9 - Exportar lista personajes a CSV
10 - Salir

"""
def starwars_app():
    lista_personajes = funciones_lambda.cargar_json("Programa Parcial\data.json")
    personajes_star_wars = list(map(funciones_lambda.castear_claves_numericas, lista_personajes))
    personajes_star_wars = list(map(funciones_lambda.agregar_clave_genero,personajes_star_wars))
    lista_generada = []

    while(True):
        print("\n1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Listar los personajes ordenados por peso\n4 - Buscar personajes\n5 - Listar personajes Femeninos\n6 - Listar personajes Masculinos\n7 - Listar personajes Sin genero\n8 - Desordenar lista y mostrar el ultimo personaje\n9 - Exportar lista generada en los puntos anteriores\n10 - Salir")
        respuesta = input()

        if(respuesta=="1"):
            lista_generada = funciones_lambda.imprimir_lista_ordenada(personajes_star_wars, "height")
        elif(respuesta=="2"):
            funciones_lambda.imprimir_personaje_mas_alto(personajes_star_wars, "male")
            funciones_lambda.imprimir_personaje_mas_alto(personajes_star_wars, "female")
            funciones_lambda.imprimir_personaje_mas_alto(personajes_star_wars, "n/a")

        elif(respuesta=="3"):
            lista_generada = funciones_lambda.imprimir_lista_ordenada(personajes_star_wars, "mass")

        elif(respuesta=="4"):
            funciones_lambda.imprimir_personajes_busqueda(personajes_star_wars)

        elif(respuesta=="5"):
            lista_generada = funciones_lambda.listar_por_genero(personajes_star_wars, "female", True)

        elif(respuesta=="6"):
            lista_generada = funciones_lambda.listar_por_genero(personajes_star_wars, "male", True)
        
        elif(respuesta=="7"):
            lista_generada = funciones_lambda.listar_por_genero(personajes_star_wars, "n/a", True)

        elif(respuesta=="8"):
            funciones_lambda.imprimir_ultimo_personaje_lista_mezclada(personajes_star_wars)

        elif(respuesta=="9"):
            funciones_lambda.archivar_lista(lista_generada, "Programa Parcial\lista.csv")

        elif(respuesta=="10"):
            print("Adios!")
            break
        else:
            print("Ingrese una opcion valida!")


starwars_app()

