''' metodo split()   Retorna una lista con las ocurrencias'''
''' En resumen separa por la expresion pasada y 
crea una lista con los resultados'''
import re 

texto = "QUEVEDO || BZRP Music Sessions #52"
fecha = "20-07-06 00:00:00"

print(re.split("[\|]{2}|[#]{1}",texto))
#['QUEVEDO ', ' BZRP Music Sessions ', '52']

print(re.split("[\- :]{1}", fecha)) 
#['20', '07', '06', '00', '00', '00']


'''equivalente al de arriba'''
print(re.split("\-| |:{1}", fecha))
#['20', '07', '06', '00', '00', '00']





print(re.split(r"[\|]{2}|[#]{1}",texto))
#['QUEVEDO ', ' BZRP Music Sessions ', '52']

print(re.split(r"[\- :]{1}", fecha)) 
#['20', '07', '06', '00', '00', '00']


'''equivalente al de arriba'''
print(re.split(r"\-| |:{1}", fecha))
#['20', '07', '06', '00', '00', '00']