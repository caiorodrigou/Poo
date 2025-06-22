import random

class Bingo:
    def __init__(self, n_bolas):
        self.__n_bolas = n_bolas
        self.__bolas = []

    def set_n_bolas(self, n_bolas):
        self.__n_bolas = n_bolas

    def get_n_bolas(self):
        return self.__n_bolas

    def proximo(self):
        if len(self.__bolas) < self.__n_bolas:
            while True:
                bola = random.randint(1, self.__n_bolas)
                if bola not in self.__bolas:
                    self.__bolas.append(bola)
                    return bola
        else:
            return -1  # Todas as bolas já foram sorteadas

    def sorteados(self):
        print(f"Bolas sorteadas: {self.__bolas}")