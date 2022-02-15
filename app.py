#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from SistemaChatBot.bot_factory import Bot_factory

###construa a lista de bots disponíveis aqui
factory = Bot_factory()
print(factory.bot_list)

sys = scb.SistemaChatBot("CrazyBots",factory.bot_list)
sys.inicio()
