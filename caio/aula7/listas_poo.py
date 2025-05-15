class Playlist():
    def __init__(self,nome ,descrição ):
        self.__nome = nome
        self.__descrição = descrição
        self.__musicas = []
    
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

    def inserir_musica(self):
        self.__musicas.append(musica)

    def listar_musicas(self):
        for i in range (len(self.__musicas)):
            print(f" {self.__musicas[i].get_titulo()} - {self.__musicas[i].get_artista()} - {self.__musicas[i].get_album()}")
    
    def __str__(self):
        return len(self.__musicas)


class musica():
    def __init__(self,titulo ,artista,album):
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
    
    