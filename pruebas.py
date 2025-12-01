from Fichas import Tutor, Secundaria

tutor1 = Tutor(
    nombre="Manuel",
    primer_apellido="Montana",
    segundo_apellido="Rodriguez",
    ine="",
    parentesco=Parentesco.Padre,
    comprobante_domicilio="",
    ocupacion="",
    discapacidad=False,
    telefono="",
    correo_electronico=""
)

# TODO: Declarar e inicializar un aspirante hijo del tutor1
# aspirante1 = Aspirante()

esfi = Secundaria(nombre="ESFI", domicilio="Guasave, Sinaloa")

print(esfi.__dict__)