# Uño Mauricio ordenando una lista (optimizar despues)
def buscar_minimo(lista: list):
    lista_recibida = lista.copy()
    
    indice_minimo = 0
    for indice in range(len(lista_recibida)):
        if lista_recibida[indice] < lista_recibida[indice_minimo]:
            indice_minimo = indice

    return indice_minimo


def ordenar_lista(lista: list):
    lista_recibida = lista.copy()

    for indice in range(len(lista_recibida)-1):
        indice_minimo = buscar_minimo(lista_recibida[indice:]) + indice
        lista_recibida[indice], lista_recibida[indice_minimo] = lista_recibida[indice_minimo], lista_recibida[indice]

    return lista_recibida


