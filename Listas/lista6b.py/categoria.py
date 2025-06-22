class Categoria():
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao   

    def __str__(self):
        return f'ID: {self.id}", Descrição: {self.descricao}'
    
    def set_id(self,id):
        if id <= 0:
            raise ValueError("ID inválido")
        self.id = id

    def set_descricao(self,descricao):
        if descricao == "":
            raise ValueError("a descricao não pode ser vazia")
        self.descricao = descricao

    def get_id(self):
        return self.id

    def get_descricao(self):
        return self.descricao

    