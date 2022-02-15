from Bots.Bot import Bot
from Bots.comando import Comando


class BotGenerico(Bot):
    def __init__(self, nome, comandos, despedida, apresentacao, boas_vindas):
        self.__despedida = despedida
        self.__apresentacao = apresentacao
        self.__boas_vindas = boas_vindas
        self.__apresentacao = apresentacao
        self.__nome = nome
        self.__comandos = comandos
 
    @property
    def nome(self):
        return self.__nome  
    
    @property
    def comandos(self):
        return self.__comandos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def apresentacao(self):
        return self.__apresentacao
 
    def mostra_comandos(self):
        mensa = ""
        for i in self.__comandos:
            mensa +=  f"{i.id} --- {i.mensagem}\n"
        return mensa
    
    def executa_comando(self,cmd):
        for i in self.__comandos:
            if i.id == cmd:
                resposta = i.get_resposta_random()
                return resposta
        return 'Comando não encontrado'
        
    def adiciona_comando(self, comando):
        self.__comandos.append(comando)
    @property
    def boas_vindas(self):
        return self.__boas_vindas
    @property
    def despedida(self):
        return self.__despedida