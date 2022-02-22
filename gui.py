import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import SistemaChatBot


class Gui:
    def __init__(self, nome_empresa):
        self.__sistema = SistemaChatBot(nome_empresa)

        self.__layout_start = [[sg.Text(self.__sistema.boas_vindas())],
                               *[[sg.Button(f'{self.__sistema.lista_bots[i].nome}')] for i in range(len(self.__sistema.lista_bots))]]

        self.__layout_bot_escolhido= []

                          

        self.__layout3 = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
                          *[[sg.Button(f'Radio {i}', 1)] for i in range(8)]]

        self.__current_layout = self.__layout_start

        self.__window = sg.Window(
            'Sistema Chatbot', self.__current_layout)


    def get_layout_bot_escolhido(self):
        msg_list = self.__sistema.get_comandos_bot()
        self.__layout_bot_escolhido = [[sg.Text(self.__sistema.bot.boas_vindas)],
                          *[[sg.Button(f'{msg_list[i + 1]}')] for i in range(len(msg_list))],
                          [sg.Button('Exit')],
                          [sg.Txt('', key='output') ]]

    def update_window(self):
        self.__window.close()
        self.__window = sg.Window(
            'Sistema Chatbot', self.__current_layout)


    def run_main_loop(self):
        current_layout = 1  # The currently visible layout
        while True:
            event, values = self.__window.read()
            print(event, values)
            if event in (None, 'Exit'):
                break

            # checa o bot escolhido
            for bot in self.__sistema.lista_bots:
                if bot.nome == event:
                    self.__sistema.bot = bot
                    self.get_layout_bot_escolhido()
                    self.__current_layout = self.__layout_bot_escolhido
                    self.update_window()
            if not self.__sistema.bot is None:
                for iden, msg in self.__sistema.get_comandos_bot().items():
                    if msg == event:
                        resposta = self.__sistema.le_envia_comando(iden)
                        self.__window.FindElement('output').Update(resposta)
                



           
        self.__window.close()


gui = Gui('UFSC')
gui.run_main_loop()

