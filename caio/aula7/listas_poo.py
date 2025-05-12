class Playlist():
    def __init__(self,nome = "",descrição = "",musicas = []):
        self.__nome = nome
        self.__descrição = descrição
        self.__musicas = musicas
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_descrição(self):    
        return self.__descrição
    
    def set_descrição(self,descrição):
        self.__descrição = descrição

    def get_musicas(self):
        return self.__musicas
    
    def set_musicas(self,musicas):
        self.__musicas = musicas

    def __str__(self):
        return len(self.__musicas)
    
    def inserir(self):
        self.__musicas.append(input)("digite o nome da música: ")


class musica():
    def __init__(self,titulo = "",artista = "",album = ""):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def get_titulo(self):    
        return self.__titulo                
    def set_titulo(self,titulo):
        self.__titulo = titulo
    def get_artista(self):
        return self.__artista   
    def set_artista(self,artista):
        self.__artista = artista
    def get_album(self):
        return self.__album
    def set_album(self,album):
        self.__album = album

    def __str__(self):
        return (f"{self.__titulo} - {self.__artista} - {self.__album}")
    
    