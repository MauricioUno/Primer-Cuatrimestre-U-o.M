import funciones

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
        opcion = input("Ingrese una de las opciones: ")
        opcion = int (funciones.validar_string(opcion, "^[+-]?[0-9]+$"))

        match opcion:
            
            case 1:
                lista_generada = funciones.imprimir_n_personajes(lista_personajes)

            case 2:
                lista_generada = funciones.imprimir_personajes_ordenados(lista_personajes, "altura")
                
            case 3:
                lista_generada = funciones.imprimir_personajes_ordenados(lista_personajes, "fuerza")     

            case 4:
                lista_generada = funciones.imprimir_personajes_por_promedio(lista_personajes)    

            case 5:
                funciones.imprimir_personajes_por_inteligencia(lista_personajes)    

            case 6:
                if type (lista_generada) == type([]) and len(lista_generada) > 0 :
                    funciones.guardar_lista(lista_generada)
                    
                else:
                    print("No hay una lista para guardar")

            case 7:
                print("Adios!")
                break

            case _:
                print("Ingrese una opcion valida!")



lista_personajes = funciones.importar_lista("Practica preparcial\data_stark.json")
menu_principal()