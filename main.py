from excepciones import CorreoElectronico

while True:
    correo_usuario = input("Introduzca su correo electrónico: ")
    correo = CorreoElectronico(correo_usuario)
    if correo.valido() == False:
        print("No ha introducido un correo válido, por favor inténtelo de nuevo. La dirección de correo debe tener la forma xxx@xxx.xx")
    else:
        if correo.existe() == False:
            print("Cuenta bloqueada a causa de un ataque.")
            exit()
        print("¡Bienvenid@!")
        exit()