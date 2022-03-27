import re

while True:
    correo = input("Introduzca su correo elecrónico: ")
    valido = re.search(".+@.+\..+", correo)
    if valido == None:
        print("No ha introducido un correo válido, por favor inténtelo de nuevo.")
    else:
        existe = re.search("\..{2,3}$", correo) # Nos aseguramos que el correo sea válido si después del punto hay dos o tres caracteres
        if existe == None:
            print("Cuenta bloqueada a causa de un ataque.")
            exit()
        print("¡Bienvenid@!")
        exit()