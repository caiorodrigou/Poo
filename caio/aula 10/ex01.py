import json
class Cliente:               #dominio        
    def __init__(self, id, nome,email,telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone    
        self.Clientes = []
        
    def __str__(self):
        return f'Cliente: {self.nome} / Id: {self.id}  / Email: {self.email} / Telefone: {self.telefone}'

class Clientes:              #armazena objetos em um arquivo/banco de dados          
     objetos = []  # atributo de classe

@classmethod
def inserir(cls,obj):
    cls.abrir()
    cls.objetos.append(obj)
    cls.salvar()

@classmethod
def listar(cls):
    return cls.objetos()
    
@classmethod
def abrir(cls):
    cls.objetos = []
    with open('clientes.json', mode ="r") as arquivo:
        s = json.load(f)
        for dic in s:
            obj = Cliente(dic['id'], dic['nome'], dic['email'], dic['telefone'])
            cls.objetos.append(obj)
            
@classmethod
def salvar (cls):
    with open('clientes.json', mode ="r") as arquivo:
        json.dump(cls.objetos, arquivo, default = vars)
 
class UI:
   
    @staticmethod
    def menu():
        print("cadastro de cliente")
        return int(input("1-inserir / 2-listar / 3-atualizar / 4-excluir / 9-fim"))
    
    @staticmethod
    def main():
        op = 0
        Clientes = []
        while op != 9 :
            op = UI.menu()
            if op == 1: UI.cliente.inserir(Clientes)
            if op == 2: UI.cliente.listar(Clientes)
                
    @staticmethod
    def cliente_inserir(cls):
        id = input("id: ")
        nome = input("nome: ")
        email = input("email: ")
        telefone = input("telefone:")
        c = Cliente(id, nome,email,telefone)
        cls.inserir(c)

    @staticmethod
    def cliente_listar(Clientes):
        for c in Clientes: print(c)