class Viagem():
    def __init__(self, distancia: float, horas: int, minutos: int):
        self.__distancia = distancia
        self.__tempo = self.__converter_para_horas(horas, minutos)

    def __converter_para_horas(self, horas: int, minutos: int) -> float:
        return horas + minutos / 60

    def set_distancia(self, d:float):
        if d > 0:
            self.__distancia = d
        else:
            raise ValueError()

    def set_tempo(self,t:float):
        if t > 0:
            self.__tempo = t
        else:
            raise ValueError()

    def get_distancia(self):
        return self.__distancia
        
    def get_tempo(self):
        return self.__tempo
    
    def calc_velocidade_media(self):
        return self.__distancia / self.__tempo
    
class UI:
    @staticmethod
    def main():
        x = Viagem(100.00, 2 , 0)
        print(x.calc_velocidade_media())

UI.main()