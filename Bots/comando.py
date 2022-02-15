from random import randint
class Comando:
    def __init__(self, id, mensagem, respostas: list):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas


    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__mensagem

    def get_resposta_random(self):
        resp = randint(0, len(self.__respostas)-1)
        return(self.__respostas[resp])
