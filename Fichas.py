



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