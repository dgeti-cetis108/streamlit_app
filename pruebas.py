from datetime import date
from random import randint
import Fichas as f

# carreras
programacion = f.Carrera("Programación", 2023)
contabilidad = f.Carrera("Contabilidad", 2023)
electronica = f.Carrera("Electrónica", 2023)
m_automotriz = f.Carrera("Mantenimiento Automotriz", 2023)
soporte = f.Carrera("Soporte y mantenimiento de equipo de cómputo", 2017)
comercio = f.Carrera("Comercio electrónico", 2025)

# entidades
sin = f.Entidad()
sin.clave = "25"
sin.nombre = "Sinaloa"

# municipios
gve = f.Municipio()
gve.entidad = sin
gve.clave = "011"
gve.nombre = "Guasave"

# aspirantes
aspirante1 = f.Aspirante()
aspirante1.nombre = "Martín"
aspirante1.primer_apellido = "López"
aspirante1.segundo_apellido = "Beltrán"
aspirante1.sexo = "H"
aspirante1.fecha_de_nacimiento = date(2010, 7, 1)
aspirante1.enfermedad = False
aspirante1.discapacidad = False
aspirante1.entidad_de_nacimiento = sin
aspirante1.entidad_donde_vive = sin
aspirante1.municipio_donde_vive = gve

# secundarias
eta = f.Secundaria("EST4", "Técnica 4")
esfi = f.Secundaria("ESFI", "Insurgentes I")

# tutores
tutor1 = f.Tutor("Joaquin", "López", "Ruvalcaba", f.Parentesco.Padre,"6870000000", False)

# fichas
ficha1 = f.Ficha()
ficha1.numero = randint(1, 500)
ficha1.fecha_de_registro = date.today()
ficha1.aula = "A01"
ficha1.opcion_1 = programacion
ficha1.opcion_2 = comercio
ficha1.opcion_3 = contabilidad
ficha1.aspirante = aspirante1
ficha1.secundaria = esfi
ficha1.tutor = tutor1
