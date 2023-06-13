class Personaje:
    def __init__(self, nombre):
        self.__nombre = nombre
    def get_propiedades(self):
        dicc = {}
        dicc["nombre"] = self.__nombre
        return dicc

personaje = Personaje("Guts") # instaciamos
# print(personaje.get_propiedades())


class Mago(Personaje):
    def __init__(self, nombre, arma):
        super().__init__(nombre)
    
        self.arma = arma
    def get_propiedades(self):
        propiedad = super().get_propiedades()
        propiedad["Arma"] = self.arma
        print(propiedad)
        return propiedad
        
maguito = Mago("Juh", "Libro")

maguito.get_propiedades()
