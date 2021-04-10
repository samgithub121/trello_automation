"""
@ Description : This is the library wrapper on top of trello apis.
@ Author : Sam Mathew
@ Created on : 08/04/2021
@ Last Modified :  08/04/2021
"""

# Global python imports
import requests

# Local python imports
from trello_auto.config.config_parser import LondonTicketConfigParser
from trello_auto.core.environment import Environment as EV
from trello_auto.core.log import Log

ui_parser = LondonTicketConfigParser(EV.UI_PARSER_PATH)


class TrelloGenericApis():
    """This is a class for creating the library api's associated with TC's.
    Attributes:  NA
    """

    def __init__(self, Log=Log.capture_log()):
        self.Log = Log
        self.card_url = "https://api.trello.com/1/cards"
        self.board_url = "https://api.trello.com/1/boards/"
        self.key = "9ea9ebd8fb05a193390ade85469ba131"
        self.token = "de4a6ac77e30ad11cf1cc9f53b12c3e46b7f051becba755daf48d64a46617253"
        self.idlist = "606bfbe9ea632d8648ee4a9b"
        self.desc = "This is a sample test card created"

    def get_idlist(self, board_name):

        trellousername = "testbonitoautomation@gmail.com"
        key = "9ea9ebd8fb05a193390ade85469ba131"
        token = "de4a6ac77e30ad11cf1cc9f53b12c3e46b7f051becba755daf48d64a46617253"

        # api-endpoint
        URL = "https://api.trello.com/1/members/{0}/boards?key={1}&token={2}".format(trellousername, key, token)

        test_name = board_name
        r = requests.get(url=URL)

        # extracting data in json format
        data = r.json()

        for i in range(len(data)):
            if data[i]['name'] == test_name:
                id_ = data[i]['id']

        URL2 = "https://api.trello.com/1/boards/{0}/lists?key={1}&token={2}".format(id_, key, token)
        r = requests.get(url=URL2)

        # extracting data in json format
        data = r.json()
        for i in range(len(data)):
            if data[i]['name'] == "To Do":
                id_ = data[i]['id']
        return id_

    def create_card(self, card_data, board_name):
        self.Log.debug("Start creating the card")
        query = {
            'key': self.key,
            'token': self.token,
            'idList': self.get_idlist(board_name),
            'name': card_data,
            'desc': self.desc
        }
        response = requests.request(
            "POST",
            self.card_url,
            params=query
        )
        if response.status_code == 200:
            self.Log.info("Card has been created successfully")
            return True
        else:
            self.Log.error("Failed to create card")
            return False

    def create_board(self, board_name):
        self.Log.debug("Start creating a board")
        query = {
            'key': self.key,
            'token': self.token,
            'name': board_name
        }

        response = requests.request(
            "POST",
            self.board_url,
            params=query
        )

        if response.status_code == 200:
            self.Log.info("Board has been created successfully")
            return True
        else:
            self.Log.error("Failed to create board")
            return False
