class Equacao():
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, a):
        if a == 0.0:
            raise ValueError("O coeficiente 'a' não pode ser zero.")
        self.__a = a

    def set_b(self, b):
        if b == 0.0:
            raise ValueError("O coeficiente 'b' não pode ser zero.")
        self.__b = b

    def set_c(self, c):
        if c == 0.0:
            raise ValueError("O coeficiente 'c' não pode ser zero.")
        self.__c = c
    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c
    
    def delta(self):
        delta = (self.get_a()**2) - 4 * (self.get_b()) * (self.get_c())
        return f"Delta: {delta}"

    def Y(self,x):
        y = (self.get_a()) * (x **2) + (self.get_b() * x) + self.get_c()
        return y

    def X1(self):
        delta = (self.get_b() **2) - 4 * (self.get_a()) * (self.get_c())
        x1 = (-self.get_b() + (delta ** 0.5) / (2 * self.get_a()))
        return f"X1 :{ x1}"

    def X2(self):
        delta = (self.get_b() **2) - 4 * (self.get_a()) * (self.get_c())
        x2 = (-self.get_b() - (delta ** 0.5) / (2 * self.get_a()))
        return f"X2 : { x2}"
    
    def __str__(self):
        return f"A = {self.get_a()} - B = {self.get_b()} - C = {self.get_c()}"