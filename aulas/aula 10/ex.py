class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
    def __str__(self):
        return f'Cliente: {self.nome}, Id: {self.id}'
x = Cliente(1, "Caio")
y = Cliente(2, "João")    

print(x)
print(y)
print(x.__dict__)
print(y.__dict__) #leer o dicionário de atributos
print(vars(x)) #ver os atributos do objeto