from SistemaChatBot.dao import DAO
import json
class Bots_dao(DAO):
    def __init__(self):
        super().__init__("SistemaChatBot/botsDB.json")

    def get(self, key):
        try:
            return self.__object_cache[key]
        
        except KeyError:
            print('Chave não disponível')
    