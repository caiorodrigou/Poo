from classes import Cliente, Clientes

class UI:
    clientes = Clientes()

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
    def inserir_cliente():
        id = int(input("Digite o ID do cliente: "))
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        fone = input("Digite o telefone do cliente: ")
        x = Cliente(id, nome, email, fone)
        Clientes.inserir(x)
        return print(f"o cliente: {x.get_nome} foi adicionado com sucesso")
   
    @staticmethod
    def listar_clientes():
        return Clientes.listar()
    
    @staticmethod
    def atualizar_cliente():
        UI.listar_clientes
        id = int(input("Digite o ID do cliente a ser atualizado: "))
        return Clientes.atualizar(id)
    
    @staticmethod
    def excluir_cliente():
        UI.listar_clientes
        id = int(input("Digite o ID do cliente a ser excluido: "))
        return Clientes.excluir(id)
    

pass
UI.main()
