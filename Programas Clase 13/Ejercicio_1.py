from functools import reduce
from random import shuffle


lista_palabras = [
    "Goku", "Vegeta", "Frieza", "Cell", "Beerus", 'Krillin'
]


superficie_triangulo = lambda base, altura : (base * altura) / 2
print(superficie_triangulo(4,5))



lista_mayusculas = list(map(lambda palabra : palabra.upper(), lista_palabras))
print(lista_mayusculas)




mas_letras = reduce(lambda maximo, elemento : elemento if len(elemento) > len(maximo) else maximo, lista_palabras)
print(mas_letras)



lista_cantidad_letras = list(filter(lambda palabra: len(palabra) == 6, lista_palabras))
print(lista_cantidad_letras)



lista_random = lista_palabras.copy()
shuffle(lista_random)
print(lista_random)




lista_alfabetica = lista_palabras.copy()
lista_alfabetica.sort()
print(lista_alfabetica)


heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]


for heroe, ataque, villano in zip(heroes, ataques, villanos):
    print("{0} \nLanza un {1}\nA {2}\n".format(heroe.capitalize(), ataque.capitalize(), villano.capitalize()))


