import json


class Cliente:   # Domínio - Entidades - Várias instâncias

    def _init_(self, id, nome, email, fone):
        self.id = id       # atributo da instância
        self.nome = nome
        self.email = email
        self.fone = fone


    def _str_(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    

#x = Cliente(1, "Alex", "alex@email.com", "987654321")
#print(x)

class Clientes:    # Persistência - Armazena os objetos em um arquivo/banco de dados

    objetos = []   # atributo de classe / estático - Não tem instância


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            maior = max(cliente.id for cliente in cls.objetos)
            obj.id = maior + 1
        else:
            obj.id = 0
        cls.objetos.append(obj)
        cls.salvar()


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []    
        with open("clientes.json", mode="r") as arquivo:
            s = json.load(arquivo)
            for dic in s: 
                c = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
                cls.objetos.append(c)


    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)