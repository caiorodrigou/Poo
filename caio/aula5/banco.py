class conta():
    def __init__(self, nome="", conta=0, saldo=0):
        self.__nome = nome
        self.__num_conta = conta
        self.__saldo = saldo

    def set__nome(self, nome):
        if nome == "":
            self.__nome = nome
        else:
            raise ValueError()
        
    def set__num_conta(self, conta):
        if conta > 0:
            self.__num_conta = conta
        else:
            raise ValueError()
    
    def set_raio(self, raio):
        if raio > 0 :
            self.__raio = raio
        else: 
            raise ValueError()
        
    def get__nome(self):
        return self.__nome
    
    def get__num_conta(self):
        return self.__num_conta
    
    def get__saldo(self):
        return self.__saldo

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
class UI():
    @staticmethod
    def main():
        x = conta()
        print ("Bem vindo ao banco")
        x.nome = (input("qual o seu nome? "))
        x.num_conta = int(input("qual o numero da sua conta? "))
        x.saldo = float(input("qual o seu saldo? "))
        comando = 0
        comando = int(input("digite 1 para depositar ou 2 para sacar : "))
        if comando == 1:
            return x.depositar()
        else:
            if comando == 2:
                return x.sacar()
        
UI.main()