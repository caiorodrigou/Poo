class Retangulo():
    def __init__(self, base ,altura):
        self.__base = 0.00
        self.__altura = 0.00
        self.set_base (base)
        self.set_altura( altura )

    def set_base(self,base) :
        if base > 0 :
            self.__base = base 
        else : 
            raise ValueError("Base deve ser maior que 0")
    
    def set_altura(self,altura) :
        if altura > 0 :
            self.__altura = altura
        else : 
            raise ValueError("altura deve ser maior que 0")

    def get_base(self):
        return float(self.__base)

    def get_altura(self):
        return float(self.__altura)
    
    def calc_area(self):
        return self.__base * self.__altura
    
    def calc_diagonal(self):
        return (self.__base**2 + self.__altura**2)**0.5
    
    def __str__(self):
        return f"A sua base é :{self.__base} e a sua altura é : {self.__altura}"

class UI():
    @staticmethod
    def main():
        x = Retangulo(10.00, 20.00)
        comando = 0
        comando = int(input("digite 1 para calcular area ou 2 para calcular diagonal"))
        if comando == 1:
            print (x.calc_area())
        elif comando == 2:
            print (x.calc_diagonal())
        print(x)

UI.main()