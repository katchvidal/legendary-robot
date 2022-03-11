#   Aplicacion de Consola Asistente para Tareas

from user import acciones


print("""
    Acciones Disponibles:
    - REGISTRO
    - LOGIN
    - EXIT
""")

doit = acciones.Acciones()
accion = input('¿Que Deseas Hacer :? ').lower()
#print( accion )

if accion == 'registro':
    doit.REGISTRO()

elif accion == 'login':
    doit.LOGIN()
