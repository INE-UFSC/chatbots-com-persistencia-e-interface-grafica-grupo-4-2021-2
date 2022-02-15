##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.nome = nome
        self.comandos = comandos

    #nao esquecer o decorator
    def nome(self):
        pass

    #nao esquecer o decorator
    def nome(nome):
        pass

    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass