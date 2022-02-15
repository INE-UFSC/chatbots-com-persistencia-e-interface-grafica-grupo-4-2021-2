from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots = lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print("Bom dia, esse é o sistemas de chatbot da empresa CSFU")
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Os chatbots disponíveis são:')
        for x, i in enumerate(self.__lista_bots):
            print(f'{x + 1}) {i.nome}: {i.apresentacao}')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        escolha = input('Digite o numero do bot de sua preferência: ')
        if escolha.isnumeric():
            if int(escolha) > 0 and int(escolha) <= len(self.__lista_bots):
                self.__bot = self.__lista_bots[int(escolha) - 1]
                print(f'bot {self.__bot.nome} escolhido.')
                return 
        print('numero não eceito, tente novamente')
        self.escolhe_bot()

        
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        escolha = input('Escolha algum comando: ').upper()
        if escolha.isnumeric():
            if int(escolha) > 0 and int(escolha) <= len(self.__bot.comandos):
                print(self.__bot.executa_comando(int(escolha)))
                return 'continuar'
        elif escolha == 'N':
            return 'parar'
        print('numero nao aceito, tente novamente')
        self.le_envia_comando()
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot     
        self.escolhe_bot() 
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas)
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            self.mostra_comandos_bot()
            saida = self.le_envia_comando()
            if saida == 'parar':
                break
        ##ao sair mostrar a mensagem de despedida do bot
        print(self.__bot.despedida)