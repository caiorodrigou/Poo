class paciente():
    def __init__(self,nome,cpf,telefone,nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento
        
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        self.__nome = nome
    def get_cpf(self):  
        return self.__cpf           
    def set_cpf(self,cpf):
        self.__cpf = cpf
    def get_telefone(self):
        return self.__telefone
    def set_telefone(self,telefone):
        self.__telefone = telefone
    def get_nascimento(self):
        return self.__nascimento
    def set_nascimento(self,nascimento):
        self.__nascimento = nascimento

    def __str__(self):
        return(f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento}")

    def 