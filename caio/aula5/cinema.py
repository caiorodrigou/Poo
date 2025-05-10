class cinema():
    def __init__(self, dia = "", horario = 0.0, ingresso = 0.0):
        self.__dia = dia
        self.__horario = horario
        self.__ingresso = ingresso

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
        return self.__dia()

    def set_horario(self):
        return self.__horario()

    def set_ingresso(self):
        return self.__ingresso()

    def calc_inteira(self):
        if self.dia in ("segunda", "terca", "quinta"):
            self.ingresso = 16.00
        elif self.dia == "quarta":
            self.ingresso = 8.00
        elif self.dia in ("sexta", "sabado", "domingo"):
            self.ingresso = 20.00   
        if self.horario >= 17.00 and self.horario <= 23.59 or self.horario == 0.00 and self.dia != "quarta":
            self.ingresso = self.ingresso + (self.ingresso /2)
        return print(f"o valor do ingresso é {self.ingresso}")
    
    def calc_meia(self):
        if self.dia in ("segunda", "terca", "quinta"):
            self.ingresso = 8.00
        elif self.dia == "quarta":
            self.ingresso = 8.00
        elif self.dia in ("sexta", "sabado", "domingo"):
            self.ingresso = 10.00
        if self.horario >= 17.00 and self.horario <= 23.59 or self.horario == 0.00 and self.dia != "quarta":
            self.ingresso = self.ingresso + (self.ingresso /2)
        return print(f"o valor do ingresso é {self.ingresso}")
    
class UI():
    @staticmethod
    def main():
        x = cinema()
        print ("Bem vindo ao cinema")
        x.dia = (input("qual o dia da semana? "))
        x.horario = float(input("qual o horario do filme? "))
        x.ingresso = float(input("qual o valor do ingresso? "))
        comando = 0
        comando = int(input("digite 1 para inteira ou 2 para meia : "))
        if comando == 1:
            x.calc_inteira()
        elif comando == 2:
            x.calc_meia()