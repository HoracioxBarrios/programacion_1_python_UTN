''' metodo sub() es un buscar y reemplazar'''
#reemplaza una o mas coincidencias

import re
ejemplo = "abc es el deporte"
#borra abc 
resultado = re.sub("abc", "", ejemplo) 
print(resultado)# es el deporte


#reemplaza abc por xyz
resultado = re.sub("abc", "xyz", ejemplo) 
print(resultado)# xyz es el deporte

#elimina los espacios duplicados
resultado = re.sub(r"\s+", "", ejemplo) #agarra los espacios y reemplaza por vacio
print(resultado)#abceseldeporte  

