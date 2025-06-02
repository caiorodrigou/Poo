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
    def __init__(self):
        self.lista = []
    
    def inserir(self, cliente):
        self.abrir()
        self.lista.append(cliente)
        self.salvar()

    def listar(self):
        self.abrir()
        for cliente in self.lista:
            print(cliente)

    def listar_id (self,id):
        self.abrir()
        for cliente in self.lista:
            if cliente.get_id() == id:
                print(cliente.get_id())

    def atualizar(self, id):
        self.abrir()
        for cliente in self.lista:
            ##################### errooooo ###########################
            if cliente.get_id() == id:
                cliente.set_nome() = input("Digite o nome do cliente: ")              
                cliente.set_email() = input("Digite o email do cliente: ")
                cliente.set_fone() = input("Digite o telefone do cliente: ")
                self.salvar()
                print("Cliente atualizado com sucesso!")
                return
        print("Cliente não encontrado.")

    def excluir(self,id):
        self.abrir()
        for cliente in self.lista:
            if cliente.get_id() == id:
                self.lista.remove(cliente)
                self.salvar()
                print("cliente excluido com sucesso!")
        print("Cliente não encontrado.")
    
    def abrir(self):
        with open('objetos.json', 'r') as arquivo:
            dados = json.load(arquivo)
            self.lista = [Cliente(**cliente) for cliente in dados]

    def salvar(self):
        with open('objetos.json', 'w') as arquivo:
            dados = [cliente.__dict__ for cliente in self.lista]
            json.dump(dados, arquivo, indent=4)

class UI:
    clientes = Clientes()

    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1:
                UI.inserir_cliente()
            elif op == 2:
                UI.listar_clientes()
            elif op == 3:
                UI.atualizar_cliente()
            elif op == 4:
                UI.excluir_cliente()
            elif op == 5 :
                print("Saindo do programa...")
      
        
    @staticmethod
    def menu():
            print("Cadastro de Cliente")
            print("1 - Inserir Cliente")
            print("2 - Listar Clientes")
            print("3 - Atualizar Cliente")
            print("4 - Excluir Cliente")
            print("5 - Sair")
            return int(input("Escolha uma opção: "))
        
    @staticmethod
    def inserir_cliente():
        id = int(input("Digite o ID do cliente: "))
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        fone = input("Digite o telefone do cliente: ")
        cliente = Cliente(id, nome, email, fone)
        return UI.clientes.inserir(cliente)
   
    @staticmethod
    def listar_clientes():
        return UI.clientes.listar()
    
    @staticmethod
    def atualizar_cliente():
        id = int(input("Digite o ID do cliente a ser atualizado: "))
        return UI.clientes.listar(id)
    
    @staticmethod
    def excluir_cliente():
        id = int(input("Digite o ID do cliente a ser atualizado: "))
        return UI.clientes.listar(id)
    


if __name__ == "__main__":
    UI.main()

    


        
        
