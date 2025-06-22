import json
class Cliente:
    def __init__(self, id, nome, email,fone):
        self.id = id
        self.nome = nome    
        self.email = email
        self.fone = fone
        
    def __str__(self):
        return f'id: {self.id}, cliente: {self.nome}, email: {self.email}, fone: {self.fone}'
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

    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_email(self):
        return self.email
    def get_fone(self):
        return self.fone

class Clientes:
    objetos = []
    
    @classmethod
    def inserir(cls, cliente):
        cls.abrir()
        cls.objetos.append(cliente)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        for cliente in cls.objetos:
            print(cliente)
    
    @classmethod
    def listar_id (cls,id):
        cls.abrir()
        for cliente in cls.objetos:
            if cliente.get_id() == id:
                print(cliente)

    @classmethod
    def atualizar(cls, id):
        cls.abrir()
        for cliente in cls.objetos:
            if cliente.get_id() == id:
                novo_nome = input("Digite o nome do cliente: ")              
                novo_email = input("Digite o email do cliente: ")
                novo_fone = input("Digite o telefone do cliente: ")

                cliente.set_nome(novo_nome)              
                cliente.set_email(novo_email) 
                cliente.set_fone(novo_fone)

                cls.salvar()

                print("Cliente atualizado com sucesso!")
                return
        print("Cliente não encontrado.")
    
    @classmethod
    def excluir(cls,id):
        cls.abrir()
        for cliente in cls.objetos:
            if cliente.get_id() == id:
                cls.objetos.remove(cliente)
                cls.salvar()
                print("cliente excluido com sucesso!")
        print("Cliente não encontrado.")
    
    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        with open('objetos.json', mode='r') as arquivo:
            dados = json.load(arquivo)
            for dic in dados: 
                c = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
                cls.objetos.append(c)
    
    @classmethod
    def salvar(cls):
        with open('objetos.json', mode ='w') as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

