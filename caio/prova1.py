from datetime import datetime, timedelta
class treino():
    def __init__(self,data,distancia,tempo):
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo
        self.set_data(data)
        self.set_distancia(distancia)   
        self.set_tempo(tempo)

    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    
    def set_data(self,data):
        if data>datetime.today():
            raise ValueError(f"data inválida")
        else:
            self.__data = data
    
    def set_distancia(self,distancia):
        if distancia <= 0 :
            raise ValueError(f"distancia inválida")
        else:
            self.__distancia = distancia

    def set_tempo(self,tempo):
        if tempo.seconds <= 0 :
            raise ValueError(f"tempo inválido")
        else:
            self.__tempo = tempo

    def pace(self):
        return (self.__tempo.seconds /60)/(self.__distancia /1000)
    def __str__(self):
        s = f"data: {self.__data.strftime('%d/%m/%Y %H:%M')} "
        s += f"distancia: {self.__distancia} "
        s += f"tempo: {self.__tempo} "
        return s

class atleta():
    def __init__(self,nome,nascimento):
        self.__nome = nome
        self._nascimento = nascimento
        self.__treinos = []
        self.set_nome(nome)
        self.set_nascimento(nascimento) 


    def get_nome(self):
        return self.__nome
    def get_nascimento(self):
        return self.__nascimento
    def set_nome(self,nome):
        if nome == "":
            raise ValueError(f"vc precisa informar um nome")
        else:
            self.__nome = nome
    def set_nascimento(self,nascimento):
        if nascimento > datetime.now():
            raise ValueError(f"nascimento inválido")
        else:
            self.__nascimento = nascimento

    def inserir(self,treino):
        self.__treinos.append(treino)

    def remover(self,treino):
        self.__treinos.remove(treino)
    def listar(self):
        return self.__treinos
    def distancia_total(self):
        total = 0 
        for treino in self.__treinos:
            total += treino.get_distancia()
        return total

    def menor_pace(self):
        paces = []
        for treino in self.__treinos:
            paces.append(treino.pace())
        return min(paces)

    def __str__(self):
        s = f"nome = {self.__nome} "
        s += f"nascimento = {self.__nascimento.strftime('%d/%m/%Y %H:%M')} "
        s += f"treinos = {len(self.__treinos)} "
        return s


    