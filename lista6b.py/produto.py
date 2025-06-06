from datetime import datetime
class Venda():
    def __init__(self,id,descricao,preco,estoque,id_categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria
    
    def __str__(self):
        return f'id: {self.id}, descriçao do produto: {self.descricao}, Preço: {self.preco}, Em estoque: {self.estoque}, id_categoria:{self.id_categoria}'

    def set_id(self,id):
        if id <= 0:
            return ValueError(f'id invalido')
        self.id = id
    
    def set_descricao(self,descricao):
        if descricao == "":
            return ValueError(f'descrição invalida')
        self.descricao = descricao

    def set_preco(self,preco):
        if preco < 0.0:
            return ValueError(f'preço invalido')
        self.preco = preco

    def set_estoque(self,estoque):
        if estoque < 0 :
            return ValueError(f'o estoque não pode ser negativo')
        self.estoque = estoque

    def set_id_categoria(self,id_categoria):
        if id_categoria <= 0:
            return ValueError(f'id da categoria invalido')
        self.id_categoria = id_categoria

    def get_id(self):
        return self.id
    
    def get_descricao(self):
        return self.descricao
    
    def get_preco(self):
        return self.preco
    
    def get_estoque(self):
        return self.estoque

    def get_id_categoria(self):
        return self.id_categoria
    