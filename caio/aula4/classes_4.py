class triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0

    def calc_area(self):
        return (self.b * self.h) /2
    
caio = triangulo()
caio.b = 10 
caio.h = 20 
print (caio.calc_area())
