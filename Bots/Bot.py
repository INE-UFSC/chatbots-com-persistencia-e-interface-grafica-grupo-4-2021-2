from abc import ABC, abstractmethod

class Bot(ABC):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def mostra_comandos(self):
        return self.__comandos

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
    
    @abstractmethod
    def apresentacao():
        pass
