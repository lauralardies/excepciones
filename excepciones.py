import re

class CorreoElectronico:

    def __init__(self) -> None:
        self.correo = self.get_correo()

    def get_correo(self):
        correo_usuario = input("Introduzca su correo electrónico: ")
        return correo_usuario

    def valido(self):
        if re.search(".+@.+\..+", self.correo) == None:
            return False
        
    def existe(self):
        if re.search("\..{2,3}$", self.correo) == None:
            return False
        
while True:
    correo = CorreoElectronico()
    if correo.valido() == False:
        print("No ha introducido un correo válido, por favor inténtelo de nuevo. La dirección de correo debe tener la forma xxx@xxx.xx")
    else:
        if correo.existe() == False:
            print("Cuenta bloqueada a causa de un ataque.")
            exit()
        print("¡Bienvenid@!")
        exit()