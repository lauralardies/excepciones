import re

class CorreoElectronico:

    def __init__(self) -> None:
        self.correo = self.get_correo()

    def get_correo(self): 
    # Esta función permite que el usuario pueda introducir la dirección de su correo
        correo_usuario = input("Introduzca su correo electrónico: ")
        return correo_usuario

    def valido(self): 
    # Esta función se asegura que el correo introducido sea de la forma xxx@xxx.xx, de no ser de esa forma hace un return False.
        if re.search(".+@.+\..+", self.correo) == None:
            return False
        
    def existe(self): 
    # Esta función de asegura que el correo introducido existe, después de ver si es válido. Las condiciones que hemos puesto 
    # para que sea válido un correo es que después del último punto haya exclusivamento dos o tres caracteres. De no ser así, 
    # hace un return False.
        if re.search("\..{2,3}$", self.correo) == None:
            return False