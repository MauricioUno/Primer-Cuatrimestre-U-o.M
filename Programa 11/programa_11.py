# Uño Mauricio ordenando una lista (optimizar despues)
def buscar_minimo(lista: list, indice: int):
    lista_recibida = lista.copy()
    
    indice_minimo = indice
    while indice < (len(lista_recibida)):
        if lista_recibida[indice] < lista_recibida[indice_minimo]:
            indice_minimo = indice
        indice += 1

    return indice_minimo


def ordenar_lista(lista: list):
    lista_recibida = lista.copy()

    for indice in range(len(lista_recibida)-1):
        indice_minimo = buscar_minimo(lista_recibida, indice)
        lista_recibida[indice], lista_recibida[indice_minimo] = lista_recibida[indice_minimo], lista_recibida[indice]
        print(lista_recibida)
    return lista_recibida



lista_numeros = [0, 3, -3, 2, 1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
print(lista_numeros)
print(ordenar_lista(lista_numeros))

