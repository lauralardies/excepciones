# excepciones


Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/excepciones)
https://github.com/lauralardies/excepciones

Hemos creado una clase en la que se analice el correo introducido. Al inicializar la clase, se pasa la variable del correo del usuario. Esta clase tiene  dos funciones, una que verifica si tiene la forma xxx@xxx.xx y otra que se asegura que el correo existe. Este es el código de la clase:
```
import re

class CorreoElectronico:

    def __init__(self, correo_usuario) -> None:
        self.correo = correo_usuario

    def valido(self): 
    # Esta función se asegura que el correo introducido sea de la forma xxx@xxx.xx, de no ser de esa forma hace un return False.
        if re.search(".+@.+\..+", self.correo) == None:
            return False
        else:
            return True
        
    def existe(self): 
    # Esta función de asegura que el correo introducido existe, después de ver si es válido. Las condiciones que hemos puesto 
    # para que sea válido un correo es que después del último punto haya exclusivamento dos o tres caracteres. De no ser así, 
    # hace un return False.
        if re.search("\..{2,3}$", self.correo) == None:
            return False
        else:
            return True
```

Para el código principal, he creado un bucle en el que si el correo no es válido haga return False y me pida el correo de nuevo. Si el correo no existe, hace un return False y bloquea la cuenta. Si el correo es válido y existe te da la bienvenida a la página web. Este es el código principal:
```
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
```
