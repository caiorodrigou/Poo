import json
class Cliente:
    def __init__(self, id, nome, email,fone):
        self.id = id 
        self.nome = nome    
        self.email = email
        self.fone = fone
        
    def __str__(self):
        return f'cliente: {self.nome}, id: {self.id}, email: {self.email}, fone: {self.fone}'
    
    def set_id(self, id):
        if id <= 0:
            raise ValueError("ID inválido")
        self.id = id
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio")
        self.nome = nome

    def set_email(self, email):
        if email == "":
            raise ValueError("seu email é invalido")
        self.email = email
    
    def set_fone(self, fone):
        if fone == "":
            raise ValueError("seu telefone é invalido")
        self.fone = fone

class Clientes:
    objetos = []  # atributo de classe
    def __init__(self):
        self.lista = []
    
    def abrir(self):
        with open('objetos.json', 'r') as arquivo:
            dados = json.load(arquivo)
            self.lista = [Cliente(**cliente) for cliente in dados]

    def salvar(self):
        with open('objetos.json', 'w') as arquivo:
            dados = [cliente.__dict__ for cliente in self.lista]
            json.dump(dados, arquivo, indent=4)

    def inserir(self, cliente):
        
        
