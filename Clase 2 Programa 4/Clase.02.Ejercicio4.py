# Uño Mauricio Ejericio 4 || Clase 2 Ejericio 1
heroes_para_reclutar = [ 
                "Batman", "BatWoman", "Batgirl",
                "Wonder Woman", "Aquaman", "Shazam",
                "Superman", "Super Girl", "Power Girl"]

heroes_info = {
                "Super Girl": {
                    "ID": 1,
                    "Origen": "Krypton",
                    "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
                    "Identidad": "Kara-Zor-El"
                },
                "Shazam": {
                    "ID": 25,
                    "Origen": "Tierra",
                    "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
                    "Identidad": "Billy Batson"
                },
                "Power Girl": {
                    "ID": 14,
                    "Origen": "Krypton",
                    "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
                    "Identidad": "Karen Starr"
                },
                "Wonder Woman": {
                    "ID": 29,
                    "Origen": "Amazonia",
                    "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
                    "Identidad": "Diana Prince"
                }
                   
}
lista_heroes_elegidos = []
for heroe in heroes_para_reclutar:
    for heroe_elegido in heroes_info:
        # El bloque se ejecuta cuando un heroe se encuentra en las dos "bases de datos"
        if heroe_elegido == heroe:
            heroes_info[heroe_elegido]["Habilidades"] = set(heroes_info[heroe_elegido]["Habilidades"])
            diccionario_heroes_elegidos = {heroe: heroes_info[heroe_elegido]}
            lista_heroes_elegidos.append(diccionario_heroes_elegidos)


# A traves de estos bucles se personaliza la forma en que mostraremos la lista de los heroes
mensaje_datos_heroes = "LISTA DE HEROES"
for datos_del_heroe in lista_heroes_elegidos:
    for nombre in datos_del_heroe:
        mensaje_datos_heroes += "\n\nCodename: " + nombre + "\n" 
        for dato in datos_del_heroe[nombre]:
            mensaje_datos_heroes += dato + ": " + str(datos_del_heroe[nombre][dato]) + "\n"

print(mensaje_datos_heroes)



