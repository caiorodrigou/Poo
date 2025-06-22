class Retangulo ():
    def __init__(self,base,altura):
        self.__b = base
        self.__h = altura 
        self.set_base(base)
        self.set_altura(altura)
    
    def set_base(self, b):
        if b < 0.0 :
            raise ValueError(f"a base não pode ser negativa")
        else : 
            self.__b = b
        
    def set_altura(self,a):
        if a < 0.0 :
            raise ValueError(f"a altura não pode ser negativa")
        else : 
            self.__a = a

    def get_altura(self):
        return self.__a 

    def get_base(self):
        return self.__b
    
    def calcular_area(self):
        return (self.get_base() * self.get_altura())
    
    def calcular_diagonal(self):
        return ((self.get_base()**2 + self.get_altura())**0.5)

    def __str__(self):
        return f"Base : {self.get_base()} - Altura : {self.get_altura()}"

    