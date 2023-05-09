import re
# 1 er ejemplo
''' Una fecha '''
fecha = "2022/04/21 16:19:26"

resultado = re.search("([0-9]{4})/([0-9]{2})/([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})",fecha)
print(resultado)#<re.Match object; span=(0, 19), match='2022/04/21 16:19:26'>

resultado = re.match("([0-9]{4})/([0-9]{2})/([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})",fecha)
print(resultado)#<re.Match object; span=(0, 19), match='2022/04/21 16:19:26'>


'''devuelven listas'''


resultado = re.findall("([0-9]{4})/([0-9]{2})/([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})",fecha)
print(resultado)#[('2022', '04', '21', '16', '19', '26')]

resultado = re.split("([0-9]{4})/([0-9]{2})/([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})",fecha)
print(resultado)#['', '2022', '04', '21', '16', '19', '26', '']


#https://youtu.be/Mc2j8Q-MHB4

