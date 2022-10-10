import funciones_lambda

def menu_principal():
    lista_generada = []
    while True:
        menu = "\nOpciones:\
                \n1- Listar los primeros N personajes\
                \n2- Ordenar y Listar héroes por altura\
                \n3- Ordenar y Listar héroes por fuerza.\
                \n4- Ordenar y Listar segun el promedio\
                \n5- Buscar y Listar héroes por inteligencia\
                \n6- Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]\
                \n7- Salir"

        print(menu)
        opcion = input(">> ")
        opcion = int (funciones_lambda.validar_string(opcion, "^[0-9]+$"))

        match opcion:
            
            case 1:
                lista_generada = funciones_lambda.guardar_imprimir_cantidad_personajes(lista_personajes)

            case 2:
                lista_generada = funciones_lambda.guardar_imprimir_personajes_ordenados(lista_personajes, "altura")
                
            case 3:
                lista_generada = funciones_lambda.guardar_imprimir_personajes_ordenados(lista_personajes, "fuerza")     

            case 4:
                lista_generada = funciones_lambda.guardar_imprimir_personajes_segun_el_promedio(lista_personajes)    

            case 5:
                funciones_lambda.imprimir_personajes_por_inteligencia(lista_personajes)    

            case 6:
                funciones_lambda.archivar_lista(lista_generada, "Programa Preparcial\lista_archivada.csv")

            case 7:
                print("Adios!")
                break

            case _:
                print("Ingrese una opcion valida!")



lista_personajes = functest.importar_lista("Programa Preparcial\data_stark.json")
menu_principal()