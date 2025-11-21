from dataclasses import dataclass

from Tutor import Tutor

@dataclass
class Aspirante:
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    secundaria: str
    sexo: str
    edad: int
    fecha_de_nacimiento: str
    tutor: Tutor
