import Fichas as fi

tutor1 = fi.Tutor(
    nombre="Manuel",
    primer_apellido="Montana",
    segundo_apellido="Rodriguez",
    parentesco=fi.Parentesco.Padre,
    discapacidad=False,
    telefono="00000000"
)
print(tutor1.__dict__)

# TODO: Declarar e inicializar un aspirante hijo del tutor1
# aspirante1 = Aspirante()

esfi = fi.Secundaria(nombre="ESFI", domicilio="Guasave, Sinaloa")

print(esfi.__dict__)