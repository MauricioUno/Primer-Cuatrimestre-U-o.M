''' Uño Mauricio Ejercicio 3
La división de alimentos de industrias Wayne está trabajando 
en un pequeño software para cargar datos de heroínas y héroes, 
para para tener un control de las condiciones de heroes existentes, nos solicitan:
    Nombre de Heroína/Héroe
    EDAD (mayores a 18 años)
    Sexo ("m", "f" o " nb")
    Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
    A) Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
    B) El sexo y nombre de Heroe | Heroína de mayor edad.
    C) La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
    D) El promedio de edad entre Heroinas.
    E) El promedio de edad entre Heroes de fuerza.

'''
cont_heroinas_fuerza_magia = 0
cont_heroinas = 0
acum_edad_heroinas = 0
cont_heroes_fuerza = 0
acum_edad_heroes_fuerza = 0
flag_primer_ingreso = True
flag_fuerza = False

while True:

    # Validacion de las variables a utilizar
    nombre = input ("Ingrese el nombre: ")
    

    edad = input ("Ingrese la edad (mayor a 18): ")
    if edad.isnumeric() == True:
        edad = int(edad)

    while ( (type(edad) != int) or (edad < 19) ):
        edad = input ("ERROR! LA EDAD DEBE SER MAYOR A 18!: ")
        if edad.isnumeric() == True :
            edad = int(edad)
    
    sexo = input ("Ingrese el sexo (masculino - femenino - no binario): ")
    while ( sexo != "masculino" and sexo != "femenino" and sexo != "no binario"):
        sexo = input ("ERROR! INGRESE UN SEXO VALIDO! (masculino - femenino - no binario): ")

    habilidad = input ("Ingrese la habilidad (fuerza - magia - inteligencia): ")
    while ( habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):
        habilidad = input ("ERROR! INGRESE UNA HABILIDAD VALIDA! (fuerza - magia - inteligencia): ")
        
    # Fin de las validaciones

    if flag_primer_ingreso == True or edad_mas_viejo < edad: 
        edad_mas_viejo = edad
        nombre_mas_viejo = nombre
        sexo_mas_viejo = sexo
        flag_primer_ingreso = False

    if habilidad == "fuerza":
        if flag_fuerza == False or edad_mas_joven_f > edad:
            edad_mas_joven_f = edad
            nombre_mas_joven_f = nombre
            flag_fuerza = True


    match sexo:
        case "masculino":
            if habilidad == "fuerza":  
                cont_heroes_fuerza += 1
                acum_edad_heroes_fuerza += edad
        
        case "femenino":
            cont_heroinas += 1
            acum_edad_heroinas += edad
            if (habilidad == "fuerza") or (habilidad == "magia"):
                cont_heroinas_fuerza_magia += 1

    
    confirmacion = input ("Para seguir ingresando datos pulse 's': ")
    if confirmacion != 's':
        break


# Los mensajes que se mostraran al usuario y sus respectivas variaciones
mensaje = "El sexo y nombre con mayor edad es: " +  sexo_mas_viejo + ", " + nombre_mas_viejo + " con " + str(edad_mas_viejo) + " años"

if flag_fuerza == True:
    mensaje += "\nEl nombre de 'Fuerza' mas joven es: " + nombre_mas_joven_f + " con " + str(edad_mas_joven_f) + " años"
else:
    mensaje += "\nNo se ingreso nadie perteneciente a la categoria de 'Fuerza' "

if cont_heroinas_fuerza_magia > 0:
    mensaje += "\nLa cantidad de heroinas de 'Fuerza' o 'Magia' es de: " + str(cont_heroinas_fuerza_magia)
else:
    mensaje += "\nNo se ingreso ninguna heroina con la habilidad de 'Fuerza' o 'Magia' "

if cont_heroinas > 0:
    promedio_edad_heroinas = acum_edad_heroinas / cont_heroinas
    mensaje += "\nEl promedio de edad de las heroinas es de: " + str(promedio_edad_heroinas)
else:
    mensaje += "\nNo se ingreso ninguna heroina"

if cont_heroes_fuerza > 0:
    promedio_edad_heroes_fuerza = acum_edad_heroes_fuerza / cont_heroes_fuerza
    mensaje += "\nEl promedio de edad de los heroes de 'Fuerza' es de: " + str(promedio_edad_heroes_fuerza)
else:
    mensaje += "\nNo se ingreso ningun heroe con la habilidad de 'Fuerza' "

print(mensaje)
    


