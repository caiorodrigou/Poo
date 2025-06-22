class circulo():
    def __init__(self,raio):
        self.__raio = raio

    def set_raio(self, raio):
        if raio > 0 :
            self.__raio = raio
        else: 
            raise ValueError()
        
    def get_raio(self):
        return self.__raio
    
    def calc_area(self):
        return 3.14 * (self.__raio ** 2)
    
    def calc_circunferencia(self):
        return 2 * 3.14 * self.__raio
    
class UI():
    @staticmethod
    def main():
        raio = int(input("qual o raio:"))
        b = circulo(raio) 
        print(b.calc_area())  
        print(b.calc_circunferencia())  

UI.main()


        