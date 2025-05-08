class circulo():
    def __init__(self):
        self.__raio = 0

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
    
#class UI:
    @staticmethod
    def main():
        b = circulo()
        b.set_raio(2)  # Use the instance 'b' to call the method
        print(b.calc_area())  # Use the instance 'b' to call the method
        print(b.calc_circunferencia())  # Use the instance 'b' to call the method

#UI.main()


        