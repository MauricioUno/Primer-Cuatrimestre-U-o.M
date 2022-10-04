import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("Programa Parcial\data.json")
    personajes_star_wars = funciones.convertir_numeros_lista(lista_personajes)
    lista_ordenada = []

    while(True):
        print("\n1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Buscar personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            lista_ordenada = funciones.imprimir_lista_ordenada(personajes_star_wars, "height")
        elif(respuesta=="2"):
            funciones.imprimir_personaje_mas_alto(personajes_star_wars, "male")
            funciones.imprimir_personaje_mas_alto(personajes_star_wars, "female")
            funciones.imprimir_personaje_mas_alto(personajes_star_wars, "n/a")

        elif(respuesta=="3"):
            lista_ordenada = funciones.imprimir_lista_ordenada(personajes_star_wars, "mass")

        elif(respuesta=="4"):
            funciones.imprimir_personajes_busqueda(personajes_star_wars)

        elif(respuesta=="5"):
            funciones.archivar_lista(lista_ordenada, "Programa Parcial\lista.csv")

        elif(respuesta=="6"):
            break
        else:
            print("Ingrese una opcion valida!")


starwars_app()

