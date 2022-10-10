import funciones_lambda_pkmn

def menu_principal():

    lista_pokemones = funciones_lambda_pkmn.extraer_lista("Programas de practica\Pokemon\pokedex.json")
    if funciones_lambda_pkmn.validar_lista_con_diccionarios(lista_pokemones):
        lista_validada = True
    else:
        print("El origen de datos no tiene el formato correcto")
        lista_validada = False

    lista_generada = []

    while lista_validada:
        menu = "\nOpciones:\
                \n1- Listar los ultimos N pokemones\
                \n2- Ordenar y Listar pokemon por poder\
                \n3- Ordenar y Listar pokemon por id.\
                \n4- Ordenar y Listar segun el promedio de (tipos|evoluciones|fortaleza|debilidad)\
                \n5- Buscar y Listar pokemon por tipo\
                \n6- Exportar a CSV la lista de pokemon ordenada según opción elegida anteriormente [1-4]\
                \n7- Salir"
                
        print(menu)
        opcion = input(">> ")
        opcion = int (funciones_lambda_pkmn.validar_dato(opcion, "^[0-9]+$"))
        match opcion:
        
            case 1:
                lista_generada = funciones_lambda_pkmn.listar_e_imprimir_ultimos_N_pokemon(lista_pokemones)

            case 2:
                lista_generada = funciones_lambda_pkmn.listar_e_imprimir_por_clave_numerica(lista_pokemones, "poder")
                
            case 3:
                lista_generada = funciones_lambda_pkmn.listar_e_imprimir_por_clave_numerica(lista_pokemones, "id")     

            case 4:
                lista_generada = funciones_lambda_pkmn.listar_e_imprimir_segun_el_promedio(lista_pokemones)    

            case 5:
                funciones_lambda_pkmn.listar_e_imprimir_pokemon_por_tipo(lista_pokemones)    

            case 6:
                funciones_lambda_pkmn.archivar_lista(lista_generada,"Programas de practica\Pokemon\lista_pokemon.csv")

            case 7:
                print("Adios!")
                break

            case _:
                print("Ingrese una opcion valida!")

menu_principal()