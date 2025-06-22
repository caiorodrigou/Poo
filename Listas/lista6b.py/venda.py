from datetime import datetime
class Venda():
    def __init__(self,id,data,carrinho,total,id_cliente):
        self.id = id
        self.data = datetime
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = id_cliente
    
    def __str__(self):
        return f'id: {self.id}, data: {self.data}, carrinho: {self.carrinho}, total: {self.total}, id_cliente:{self.id_cliente}'

    def set_id(self,id):
        if id <= 0:
            return ValueError(f'id invalido')
        self.id = id
    
    def set_data(self,data):
        if data < datetime.now :
            return ValueError(f'data invalida')
        self.data = data

    def set_carrinho(self,carrinho):
        if carrinho != True or False:
            return ValueError(f'carrinho invalido')
        self.carrinho = carrinho

    def set_total(self,total):
        if total < 0 :
            return ValueError(f'o total não pode ser negativo')
        self.total = total
    
    def set_id_cliente(self,id_cliente):
        if id_cliente <= 0:
            return ValueError(f'id invalido')
        self.id_cliente = id_cliente

    def get_id(self):
        return self.id
    
    def get_data(self):
        return self.data
    
    def get_carrinho(self):
        return self.carrinho
    
    def get_total(self):
        return self.total

    def get_id_cliente(self):
        return self.id_cliente
    