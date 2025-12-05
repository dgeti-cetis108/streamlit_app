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
    parentesco: Parentesco
    discapacidad: bool
    telefono: str

    def __init__(self, nombre, primer_apellido, segundo_apellido, parentesco, telefono, discapacidad):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.parentesco = parentesco
        self.telefono = telefono
        self.discapacidad = discapacidad

class Entidad:
    clave: str
    nombre: str

class Municipio:
    clave: str
    nombre: str
    entidad: Entidad

class Aspirante:
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    sexo: str
    edad: int
    fecha_de_nacimiento: str
    enfermedad: bool
    discapacidad: bool
    entidad_de_nacimiento: Entidad
    entidad_donde_vive: Entidad
    municipio_donde_vive: Municipio


class Carrera:
    nombre: str
    plan_de_estudios: int

    def __init__(self, nombre, plan):
        self.nombre = nombre
        self.plan_de_estudios = plan

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