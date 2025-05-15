import datetime
class paciente():
    def __init__(self,nome,cpf,telefone,nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento
        
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if nome == "":
            raise ValueError(f"vc precisa informar um nome")
        else:
            self.__nome = nome
    def get_cpf(self):  
        return self.__cpf           
    def set_cpf(self,cpf):
        if cpf == "":
            raise ValueError(f"vc precisa informar um cpf")
        else:
            self.__cpf = cpf
    def get_telefone(self):
        return self.__telefone
    def set_telefone(self,telefone):
        if telefone == "":
            raise ValueError(f"vc precisa informar um cpf")
        else:
            self.__telefone = telefone
    def get_nascimento(self):
        return self.__nascimento
    def set_nascimento(self,nascimento):
        if nascimento == "":
            raise ValueError(f"vc precisa informar um cpf")
        else:
            self.__nascimento =nascimento

    def __str__(self):
        return(f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento}")

    def idade(self):
        idade = datetime.datetime.now() - self.__nascimento
        return f"{idade.days//365} anos"

    def __str__(self):
        s = ""
        s = f"nome: {self.__nome}"
        s+= f"cpf: {self.__cpf}"
        s+= f"telefone: {self.__telefone}"
        s+= f"nascimento: {self.__nascimento}"
        return s

a = paciente("caio","43370009846","95587633",datetime.datetime(2005,7,31))
print(a.idade())
print(a)