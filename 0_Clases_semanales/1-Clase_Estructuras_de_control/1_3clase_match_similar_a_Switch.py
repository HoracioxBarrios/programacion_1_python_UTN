'''Sentencia MATCH: 
esta sentecia es simialal a switch de Js, con algunas diferencia;
En match entre caso y caso no se usa Break, entre otras cosas'''
# status = 404
# match status:
#     case 400 | 401:# es un or
#         print("Error request") 
#     case 404:
#         print("No encontrado")
#     case _:#el guin bajo es como el default del switch de js
#         print("Algo") 


texto = input("Ingrese una accion")

match texto:
    case "SALTR":
        print("SATAR la orden es {0}".format(texto))
    case "CORRER":
        print("CORRER la orden es {0}".format(texto))
    case other:
        print("la orden es {0}".format(texto))