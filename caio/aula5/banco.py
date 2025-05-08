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
