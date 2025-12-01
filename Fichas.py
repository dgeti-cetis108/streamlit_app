from enum import Enum


class Secundaria:
    nombre: str
    domicilio: str
    cct: str
    telefono: str
    
    def __init__(self, nombre, domicilio="", cct="", telefono=""):
        self.nombre = nombre
        self.domicilio = domicilio
        self.cct = cct
        self.telefono = telefono

class Parentesco(Enum):
    Padre = 1
    Madre = 2
    Abuelo = 3
    Hermano = 4
    Tio = 5
    Encargado = 6

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


class Aspirante:
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    #secundaria: Secundaria
    sexo: str
    edad: int
    fecha_de_nacimiento: str
    #tutor: Tutor


class Ficha:
    pass