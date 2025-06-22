import enum
class Estacao(enum.Enum):
    primavera = 1
    verão = 2
    outono = 3
    inverno = 4

a = Estacao.inverno
b = Estacao["verão"]
c = Estacao(3)
print(a) # Estacao.INVERNO
print(b) # Estacao.VERAO
print(c) # Estacao.PRIMAVERA