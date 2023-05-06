'''
16.Crea un diccionario que represente una lista de tareas 
pendientes, donde las claves son las tareas y los valores son 
"True" si están completadas y "False" sino lo están. Solicita 
al usuario el nombre de una tarea y modifica el valor para
marcarla como completada. Imprimir el listado de tareas 
pendientes

'''

# Crear el diccionario de tareas pendientes
tareas_pendientes = {
    'tarea1': False,
    'tarea2': True,
    'tarea3': False,
    'tarea4': True,
    'tarea5': False
}

# Solicitar al usuario el nombre de la tarea a completar
tarea_completada = input('Ingrese el nombre de la tarea que ha completado: ')

# Marcar la tarea como completada
if tarea_completada in tareas_pendientes:
    tareas_pendientes[tarea_completada] = True
    print(f"La tarea '{tarea_completada}' se ha marcado como completada.")
else:
    print(f"La tarea '{tarea_completada}' no se encuentra en la lista de tareas pendientes.")

# Imprimir el listado de tareas pendientes
print("\nListado de tareas pendientes:")
for tarea, completada in tareas_pendientes.items():
    estado = 'completada' if completada else 'pendiente'
    print(f"- {tarea}: {estado}")
