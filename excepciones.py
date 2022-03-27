import re

while True:
    correo = input("Introduzca su correo elecrónico: ")
    valido = re.search(".*@.*\..*", correo)
    if valido == None:
        print("No ha introducido un correo válido, por favor inténtelo de nuevo.")
    else:
        print("¡Bienvenid@!")
        exit()