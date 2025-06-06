class Venda:
    def __init__(self,id,data,carrinho,total,id_cliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = id_cliente
    
    def __str__(self):
        return f'id: {self.id}, data: {self.data}, carrinho: {self.carrinho}, total: {self.total}, id_cliente:{self.id_cliente}'

    def get