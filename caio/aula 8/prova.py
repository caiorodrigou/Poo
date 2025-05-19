import datetime
class carrinho():
    def __init__(self,cliente,data):
        self.__cliente = cliente
        self.__data = data
        self.__itens = []
        

    def get_cliente(self):
        return self.__cliente
    def set_cliente(self,cliente):
        if self.__cliente == "":
            raise ValueError(f"vc precisa informar um cliente")
        else:
            self.__cliente = cliente

    def get_data(self):   
        return self.__data          
    def set_data(self,data):
        if data > datetime.now():
            raise ValueError(f"data inválida")
        else:
            self.__data = data

    def inserir(self,item):
        self.__itens.append(item)

    def remover(self,item):
        self.__itens.remove(item)

    def listar(self):
        return self.__itens
    
    def preco_total(self):
        total = 0
        for itens in self.__itens:
            total += itens.total()
        return total


    def __str__(self):  
        s = f" cliente = {self.__cliente} "
        s += f" data = {self.__data} "
        s += f" itens quantidade = {len(self.__itens)} "

        return s

        
class item():
    def __init__(self,produto,quantidade,preco):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__preco = preco
       

    def get_produto(self):
        return self.__produto
    def get_quantidade(self):
        return self.__quantidade
    def get_preco(self):
        return self.__preco
    
    def set_produto(self,produto):
        if self.__produto == "":
            raise ValueError(f"vc precisa informar um produto")
        else:
            self.__produto = produto
    def set_quantidade(self,quantidade):
        if quantidade <= 0:
            raise ValueError(f"quantidade inválida")
        else:
            self.__quantidade = quantidade
    def set_preco(self,preco):
        if preco <= 0.00:
            raise ValueError(f"preco inválido")
        else:
            self.__preco = preco

    def total(self):
        return self.__preco * self.__quantidade
    
    def __str__(self):
        s = f"produto = {self.__produto}"
        s += f"quantidade = {self.__quantidade}"
        s += f"preco = {self.__preco}"
        return s

a = carrinho ("caio",datetime.datetime(2024,5,12,6,30))
b = item("banana",2,3.00)
c = item("maça",3,2.00)
a.inserir(b)
a.inserir(c)
a.remover(b)
print("itens:")
for itens in a.listar():
    print(itens)
print(a)
print(a.preco_total())
