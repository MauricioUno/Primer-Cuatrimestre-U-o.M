#Uño Mauricio Ejercicio 5

lista_habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    },
    {
        "Nombre": "Vacío",
        "Poder": 570
    },
    {
        "Nombre": "Necromancia",
        "Poder": 981
    },
    {
        "Nombre": "Brujeria",
        "Poder": 1500
    }
]

nueva_lista_habilidades = []
for habilidad in lista_habilidades:
    
    lista_valores = []
    for dato in habilidad:
        lista_valores.append(habilidad[dato])
    lista_valores = tuple(lista_valores)

    nueva_lista_habilidades.append(lista_valores)

# No entiendo del todo el funcionamiento, asi que lo dejo comentado
'''
def nivel_de_poder(indice_poder):
    return indice_poder[1]
nueva_lista_habilidades.sort(key = nivel_de_poder)
'''

diccionario_habilidades = {"Habilidades UTN": nueva_lista_habilidades}
for clave in diccionario_habilidades:
    mensaje = "\n" + clave + "\n\n"
    for valor_dato in diccionario_habilidades[clave]:
        mensaje += "Habilidad: {0} | ".format(valor_dato[0])
        mensaje += "Poder: {0} \n".format(valor_dato[1])
  
print(mensaje)