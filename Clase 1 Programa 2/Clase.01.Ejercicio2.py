''' Uño Mauricio Ejercicio 2
La división de alimentos está trabajando en un pequeño software para cargar
las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
    PESO: (entre 10 y 100 kilos)
    PRECIO POR KILO: (mayor a 0 [cero]).
    TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto, 
o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
    A) El importe total a pagar, BRUTO sin descuento.
    B) El importe total a pagar con descuento (Solo si corresponde).
    C) Informar el tipo de alimento más caro.
    D) El promedio de precio por kilo en total.

'''

acumulador_kg = 0
acumulador_importe_animal = 0
acumulador_importe_vegetal = 0
acumulador_importe_mezcla = 0
while True:

    # Validacion de las variables a utilizar en el programa
    peso_en_kg = input ("Ingrese el peso del producto en kg (10 a 100): ")
    if peso_en_kg.isnumeric() == True :
        peso_en_kg = int(peso_en_kg)

    while ( (type(peso_en_kg) != int) or (peso_en_kg < 10) or (peso_en_kg > 100) ):
        peso_en_kg = input ("ERROR! INGRESE UN PESO VALIDO! (10 a 100): ")
        if peso_en_kg.isnumeric() == True :
            peso_en_kg = int(peso_en_kg)

    precio_por_kg = input ("Ingrese el precio por kilo del producto: ")
    if precio_por_kg.isnumeric() == True :
        precio_por_kg = int(precio_por_kg)

    while ( (type(precio_por_kg) != int) or (precio_por_kg < 1) ):
        precio_por_kg = input ("ERROR! INGRESE UN PRECIO VALIDO!: ")
        if precio_por_kg.isnumeric() == True :
            precio_por_kg = int(precio_por_kg)
    
    tipo_ingresado = input ("Ingrese el tipo de producto (vegetal - animal - mezcla): ")
    while ( tipo_ingresado != "vegetal" and tipo_ingresado != "animal" and tipo_ingresado != "mezcla"):
        tipo_ingresado = input ("ERROR! INGRESE UN TIPO VALIDO! (vegetal - animal - mezcla): ")

    # Fin de las validaciones

    importe_de_la_compra = peso_en_kg * precio_por_kg

    match tipo_ingresado:
        
        case "vegetal":
            acumulador_importe_vegetal += importe_de_la_compra
        
        case "animal":
            acumulador_importe_animal += importe_de_la_compra

        case "mezcla":
            acumulador_importe_mezcla += importe_de_la_compra
    
    acumulador_kg += peso_en_kg

    confirmacion = input ("Para seguir ingresando producto pulse 's': ")
    if confirmacion != 's':
        break

# Punto A Informe del importe total a pagar, BRUTO sin descuento.
importe_bruto = acumulador_importe_vegetal + acumulador_importe_animal + acumulador_importe_mezcla
mensaje_print = "El importe bruto es de: " + str(importe_bruto)

# Punto B Informe del importe total a pagar con descuento (Solo si corresponde).
if acumulador_kg > 300:
    descuento = 25
elif acumulador_kg > 100:
    descuento = 15
else:
    descuento = 0

if descuento != 0:
    importe_con_descuento = importe_bruto - (importe_bruto * descuento / 100)
    importe_final = importe_con_descuento 
    mensaje_print += "\nSe aplico un descuento del " + str(descuento) + "%"
    mensaje_print += "\nEl importe con descuento es de: " + str(importe_con_descuento)
else:
    importe_final = importe_bruto
    mensaje_print += "\nNo se aplico ningun descuento"

# Punto C Informe del tipo de alimento más caro. (no contempla el caso de "2 maximos iguales")
if acumulador_importe_vegetal > acumulador_importe_animal:
    if acumulador_importe_vegetal > acumulador_importe_mezcla:
        producto_mas_caro = "Vegetal"
    else:
        producto_mas_caro = "Mezcla"

elif acumulador_importe_animal > acumulador_importe_mezcla:
    producto_mas_caro = "Animal"

else:
    producto_mas_caro = "Mezcla"

mensaje_print += "\nEl tipo de producto mas caro es: " + producto_mas_caro

# Punto D Informe del promedio de precio por kilo en total.
promedio_precio_por_kg = importe_final / acumulador_kg
mensaje_print += "\nEl promedio de precio por kilo es: " + str(promedio_precio_por_kg)

print(mensaje_print)

