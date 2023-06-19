
'''
poo
'''
class Persona:
    def __init__(self) -> None:
        self.__nombre = None
    
    @property
    def nombre(self) -> str:
        """Esto es un Getter del nombre"""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Esto es un setter del nombre, el cual valida y lo guarda modificado"""
        if nuevo_nombre == 'Facu':
            self.__nombre = f'Profe {nuevo_nombre}'
        else:
            self.__nombre = f'Alumno {nuevo_nombre}'

persona = Persona()
# Seteo nombre con la propiedad 'setter'
persona.nombre = 'Facu'
# leo el nombre con la propiedad 'getter'
print(persona.nombre)

otra_persona = Persona()
# Seteo nombre con la propiedad 'setter'
otra_persona.nombre = 'Vegeta'
# leo el nombre con la propiedad 'getter'
print(otra_persona.nombre)

"""
Output:
Profe Facu
Alumno Vegeta
"""

# que la camara te siga se llama paralax