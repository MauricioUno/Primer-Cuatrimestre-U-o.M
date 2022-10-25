
class Mascota:
    def __init__(self, nombre, apellido) -> None:
        self._name = nombre
        self._surname = apellido

    def nombre_completo(self) -> str:
        return "{0} {1}".format(self._name, self._surname)
    
    @property
    def obtener_nombre(self):
        return self._name

    def modificar_nombre(self, nombre):
        self._name = nombre
    


    

lista_gatos = []

for i in range(2):
    gato = Mascota("Coc{0}".format(i), "Rallado")
    lista_gatos.append(gato)

name_gato = lista_gatos[1].obtener_nombre
lista_gatos[0].modificar_nombre("theoa")

print(name_gato)
for gato in lista_gatos:
    print(gato.nombre_completo())
