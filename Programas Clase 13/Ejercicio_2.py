

def calcular_superficie_circulo(radio : float) -> float:
    '''
    Parametros:
    - El radio del circulo

    Funcion:
    - Calcula la superficie del circulo con el radio pasado
    como parametro

    Retorno:
    - La superficie del circulo, con dos decimales
    '''
    sup_circulo = pow(radio, 2) * 3.1415
    return round(sup_circulo, 2)

print(calcular_superficie_circulo(15))

lista_palabras = [
    "goKU", "vEgETa", "FrIEzA", "CELl", "BeERuS", 'kriLLin'
]

def capitalizar_o_minisculizar_lista(lista_palabras: list, modo = "upper") -> list:
    '''
    Parametros:
    - Una lista con strings
    - El modo en que se cambiara a la lista (lower/upper), por default sera upper

    Funcion:
    - Crea una copia de la lista, la itera y cambia los elementos segun corresponda
    
    Retorno:
    - La lista cambiada
    '''
    palabras = lista_palabras.copy()
    for indice in range(len(palabras)):
        if modo == "lower":
            palabras[indice] = palabras[indice].lower()
        elif modo == "upper":
            palabras[indice] = palabras[indice].upper()
        
    return palabras

lista_cambiada = capitalizar_o_minisculizar_lista(lista_palabras)
print(lista_cambiada)

heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]


def imprimir_mensajes_ataques(lista_heroes: list, lista_ataques: list, lista_villanos: list):
    '''
    Parametros:
    - La lista de heroes
    - La lista de ataques
    - La lista de los villanos
    - Nota: Las tres listas deben ser del mismo tamaño
    Funcion:
    - Itera las listas e imprime los mensajes correspondientes capitalizando los elementos
    '''
    for indice in range(len(lista_heroes)):
        print("{0} Lanza un {1} a {2}".format(lista_heroes[indice].capitalize()\
                                            ,lista_ataques[indice].capitalize()\
                                            , lista_villanos[indice].capitalize()))

imprimir_mensajes_ataques(heroes, ataques, villanos)
