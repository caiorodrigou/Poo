from classes import Cliente, Clientes

class UI:

    @staticmethod
    def menu():
        s = f"Qual das seguintes opções você deseja executar?\n"
        s += f"1. Inserir cliente;\n"
        s += f"2. Excluir cliente;\n"
        s += f"3. Atualizar cliente;\n"
        s += f"4. Listar clientes;\n"
        s += f"10. Encerrar programa.\n"
        return int(input(f"{s}\nInsira sua escolha: "))
    
    
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = UI.menu()
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_excluir()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_listar()


    @staticmethod
    def cliente_listar():
        print("Estes são todos os clientes cadastrados:")
        for c in Clientes.listar():
            print(c)


    @staticmethod
    def cliente_inserir():
        #id = int(input("Informe o ID do cliente: "))
        nome = input("Informe seu nome: ")
        email = input("Informe seu email: ")
        fone = input("Informe seu telefone: ")
        x = Cliente(0, nome, email, fone)
        Clientes.inserir(x)


    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe seu novo nome: ")
        email = input("Informe seu novo email: ")
        fone = input("Informe seu novo telefone: ")
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)

    
    @staticmethod
    def cliente_excluir():
        UI.cliente_listar
        id = int(input("Informe o ID do cliente que será excluído: "))
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

pass

UI.main()
