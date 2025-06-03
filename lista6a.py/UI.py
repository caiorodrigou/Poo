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
