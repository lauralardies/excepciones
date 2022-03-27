import re

while True:
    correo = input("Introduzca su correo elecrónico: ")
    valido = re.search(".+@.+\..+", correo)
    if valido == None: # Es decir, el correo no tiene la forma xxx@xxx.xx
        print("No ha introducido un correo válido, por favor inténtelo de nuevo. La dirección de correo debe tener la forma xxx@xxx.xx")
    else:
        existe = re.search("\..{2,3}$", correo) # Nos aseguramos que el correo sea válido si después del punto hay dos o tres caracteres
        if existe == None: # Es decir, el coreo no tiene la forma xxx@xxx.xx o xxx@xxx.xxx
            print("Cuenta bloqueada a causa de un ataque.")
            exit()
        print("¡Bienvenid@!")
        exit()