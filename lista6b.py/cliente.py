class Cliente:
    def __init__(self, id, nome, email,fone):
        self.id = id
        self.nome = nome    
        self.email = email
        self.fone = fone
        
    def __str__(self):
        return f'id: {self.id}, cliente: {self.nome}, email: {self.email}, fone: {self.fone}'
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