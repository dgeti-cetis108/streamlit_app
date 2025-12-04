from datetime import date
from enum import Enum


class Secundaria:
    cct: str
    nombre: str
    
    def __init__(self, cct, nombre):
        self.cct = cct
        self.nombre = nombre

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
    sexo: str
    edad: int
    fecha_de_nacimiento: str
    enfermedad: bool
    discapacidad: bool


class Carrera:
    nombre: str
    plan_de_estudios: int

class Ficha:
    numero: int
    fecha_de_registro: date
    aula: str
    opcion_1: Carrera
    opcion_2: Carrera
    opcion_3: Carrera
    aspirante: Aspirante
    secundaria: Secundaria
    tutor: Tutor