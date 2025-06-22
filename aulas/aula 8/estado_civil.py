import enum
class pessoa:
    def __init__(self):
        self.nome = ""
        self.estado_civil = estado_civil.CASADO

class estado_civil(enum.Enum):
    SOLTEIRO = 1
    CASADO = 2
    DIVORCIADO = 3
    VIUVO = 4
    UNIÃO_ESTAVEL = 5
