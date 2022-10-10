import funciones_lambda

def starwars_app():
    lista_personajes = funciones_lambda.cargar_json("Programa Parcial\data.json")
    personajes_star_wars = list(map(funciones_lambda.castear_claves_numericas, lista_personajes))
    lista_ordenada = []

    while(True):
        print("\n1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Listar los personajes ordenados por peso\n4 - Buscar personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()

        if(respuesta=="1"):
            lista_ordenada = funciones_lambda.imprimir_lista_ordenada(personajes_star_wars, "height")
        elif(respuesta=="2"):
            funciones_lambda.imprimir_personaje_mas_alto(personajes_star_wars, "male")
            funciones_lambda.imprimir_personaje_mas_alto(personajes_star_wars, "female")
            funciones_lambda.imprimir_personaje_mas_alto(personajes_star_wars, "n/a")

        elif(respuesta=="3"):
            lista_ordenada = funciones_lambda.imprimir_lista_ordenada(personajes_star_wars, "mass")

        elif(respuesta=="4"):
            funciones_lambda.imprimir_personajes_busqueda(personajes_star_wars)

        elif(respuesta=="5"):
            funciones_lambda.archivar_lista(lista_ordenada, "Programa Parcial\lista.csv")

        elif(respuesta=="6"):
            break
        else:
            print("Ingrese una opcion valida!")


starwars_app()

