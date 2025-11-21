# nombre, sexo, fecha de nacimiento,
# edad, ine, parentesco, curp, domicilio, 
# usa botitas, cabello rizado, acta de nacimiento,
# ocupación, fotografía, color de piel, estatura,
# color de ojos, complexión, discapacidad

# Proceso de abstracción

# nombre, primer apellido, segundo apellido, ine,
# parentesco, comprobante de domicilio, ocupación,
# discapacidad, teléfono1, teléfono2, correo electrónico

from dataclasses import dataclass
from enum import Enum

class Parentesco(Enum):
    Padre = 1
    Madre = 2
    Abuelo = 3
    Hermano = 4
    Tio = 5
    Encargado = 6

@dataclass
class Tutor:
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    ine: str # "images/tutores/20260115_tutor_ine.jpg"
    parentesco: Parentesco
    comprobante_domicilio: str
    ocupacion: str
    discapacidad: bool
    telefono: str
    correo_electronico: str
