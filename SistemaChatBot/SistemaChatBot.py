from Bots.Bot import Bot
from SistemaChatBot.bot_factory import Bot_factory

class SistemaChatBot:
    def __init__(self,nomeEmpresa):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__bot_factory = Bot_factory()
        self.__lista_bots = self.__bot_factory.bot_list
        self.__bot = None


    @property
    def lista_bots(self):
        return self.__lista_bots

    @property 
    def bot(self):
        return self.__bot 

    @bot.setter
    def bot(self, novo):
        self.__bot = novo
    
    def boas_vindas(self):
        return f"Bom dia, esse é o sistemas de chatbot da empresa {self.__empresa}"
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Os chatbots disponíveis são:')
        for x, i in enumerate(self.__lista_bots):
            print(f'{x + 1}) {i.nome}: {i.apresentacao}')
        
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def get_comandos_bot(self):
        return self.__bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self, iden):
        return self.__bot.executa_comando(iden)
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
