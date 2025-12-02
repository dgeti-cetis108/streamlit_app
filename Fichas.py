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

    def __init__(self, nombre, primer_apellido, segundo_apellido, parentesco, telefono, discapacidad, ine="", comprobante_domicilio="", ocupacion="", correo_electronico=""):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.parentesco = parentesco
        self.telefono = telefono
        self.discapacidad = discapacidad
        self.ine = ine
        self.comprobante_domicilio = comprobante_domicilio
        self.ocupacion = ocupacion
        self.correo_electronico = correo_electronico


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