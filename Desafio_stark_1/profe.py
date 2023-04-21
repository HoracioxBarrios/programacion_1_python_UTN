'''
def heroe_segun_altura_genero_v2(lista_heroes: list, genero: str, min_max: str) -> None:
    heroe_aux = {}
    for heroe in lista_heroes:
        if not heroe_aux and heroe['genero'] == genero:
            heroe_aux = heroe
        
        if (heroe_aux and heroe['genero'] == genero):
            if ((min_max == 'Bajo' and float(heroe_aux['altura']) > float(heroe['altura'])) or 
                (min_max == 'Alto' and float(heroe_aux['altura']) < float(heroe['altura']))):
                    heroe_aux = heroe

    print(f"Nombre: {heroe_aux['nombre']} - Altura: {heroe_aux['altura']} mts.")
'''