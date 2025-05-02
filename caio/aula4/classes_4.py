#triangulo
class triangulo():
    def __init__(self):
        self.b = 0
        self.h = 0

    def calc_area(self):
        return (self.b * self.h) /2

#viagem
class viagem():
    def __init__(self):
        self.distancia_km = 0
        self.horas = 0
        self.minutos = 0
    def calc_velocidade(self):
        return self.distancia_km / (self.horas + (self.minutos / 60))
    
#conta bancaria
class conta():
    def __init__(self):
        self.nome = ""
        self.num_conta = 0
        self.saldo = 0

    def depositar(self):
        numero = int(input("qual o numero da sua conta? "))
        if numero != self.num_conta:
            return print("numero da conta esta errado")
        else:
            valor_depositado = float(input("Digite o valor a ser depositado: "))
            self.saldo = self.saldo + valor_depositado
            return print (f"seu saldo agora é {self.saldo}")
    
    def sacar(self):
        numero = int(input("qual o numero da sua conta? "))
        if numero != self.num_conta:
            print("numero da conta esta errado")
        else:
            valor_sacado = float(input("Digite o valor a ser sacado: "))
            if valor_sacado > self.saldo :
                return print (f"seu saldo é insuficiente")
            else:
                self.saldo = self.saldo - valor_sacado 
                return print (f"seu saldo agora é {self.saldo}")

#cinema
class cinema():
    def __init__(self):
        self.dia = ""
        self.horario = 0.0
        self.ingresso = 0.0

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

caio = cinema()
caio.dia = "quinta"
caio.horario = 18.00
caio.calc_inteira()
caio.calc_meia()

