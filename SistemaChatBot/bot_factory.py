from Bots.BotGenerico import BotGenerico
from SistemaChatBot.bots_dao import Bots_dao
from Bots.comando import Comando
class Bot_factory:
    def __init__(self):
        self.__bots_dao = Bots_dao()
        self.__bot_list = []
        self.fill_bot_list()
    @property
    def bot_list(self):
        return self.__bot_list

    def fill_bot_list(self):
        for nome, conteudo in self.__bots_dao.object_cache.items():
            temp_comandos = []
            comand_num = 0
            for pergunta,  respostas in conteudo['comandos'].items():
                comand_num += 1
                temp_comandos.append(Comando(comand_num, pergunta, respostas)) 
            self.__bot_list.append(BotGenerico(nome, temp_comandos, conteudo['despedida'], conteudo['apresentacao'], conteudo['boas_vindas']))
    
    

