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