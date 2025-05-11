class cinema():
    def __init__(self, dia, horario):
        self.__dia = dia
        self.__horario = horario
        self.__ingresso = 0

    def set_dia(self, dia):
        if dia in ("segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"):
            self.__dia = dia
        else:
            raise ValueError("Dia inválido. Escolha entre segunda, terca, quarta, quinta, sexta, sabado ou domingo.")
        
    def set_horario(self, horario):
        if horario >= 0.00 and horario <= 23.59:
            self.__horario = horario
        else:
            raise ValueError("Horario inválido. Escolha um horário entre 0.00 e 23.59.")
        
    def set_ingresso(self, ingresso):
        if ingresso >= 0.00:
            self.__ingresso = ingresso
        else:
            raise ValueError("Valor do ingresso inválido. O valor deve ser maior ou igual a 0.")

    def get_dia(self):
        return self.__dia

    def get_horario(self):
        return self.__horario

    def get_ingresso(self):
        return self.__ingresso

    def calc_inteira(self):
        if self.__dia in ("segunda", "terca", "quinta"):
            self.__ingresso = 16.00
        elif self.__dia == "quarta":
            self.__ingresso = 8.00
        elif self.__dia in ("sexta", "sabado", "domingo"):
            self.__ingresso = 20.00   
        if self.__dia != "quarta" and (self.__horario >= 17.00 and self.__horario <= 23.59) :
            self.__ingresso = self.__ingresso + (self.__ingresso /2)
        return self.__ingresso
    
    def calc_meia(self):
        if self.__dia in ("segunda", "terca", "quinta"):
            self.__ingresso = 8.00
        elif self.__dia == "quarta":
            self.__ingresso = 8.00
        elif self.__dia in ("sexta", "sabado", "domingo"):
            self.__ingresso = 10.00
        if self.__dia != "quarta" and (self.__horario >= 17.00 and self.__horario <= 23.59) :
            self.__ingresso = self.__ingresso + (self.__ingresso /2)
        return self.__ingresso
    
class UI():
    @staticmethod
    def main():
        x = cinema("quinta",10.00)
        print ("Bem vindo ao cinema")

        comando = 0

        comando = int(input("qual seu ingresso, digite 1 para inteira ou 2 para meia : "))
        if comando == 1:
            print(x.calc_inteira())
        elif comando == 2:
            print(x.calc_meia())

UI.main()