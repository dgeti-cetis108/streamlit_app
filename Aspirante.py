from dataclasses import dataclass

@dataclass
class Aspirante:
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    secundaria: str
    sexo: str
    edad: int
    fecha_de_nacimiento: str
