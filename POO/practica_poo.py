
class Mascota:
    def __init__(self, nombre, apellido) -> None:
        self.name = nombre
        self.surname = apellido

    def nombre_completo(self) -> str:
        return "{0} {1}".format(self.name, self.surname)
    
    def verificar_apellido(self):
        if self.surname == "Rallado":
            print("El apellido es Rallado")

lista_gatos = []

for i in range(2):
    gato = Mascota("Coc{0}".format(i), "Rallado")
    lista_gatos.append(gato)

for gato in lista_gatos:
    print(gato.nombre_completo())


lista_gatos[0].name = "PEPE"
for gato in lista_gatos:
    gato.verificar_apellido()
    print(gato.nombre_completo())