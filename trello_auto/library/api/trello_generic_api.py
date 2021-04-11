"""
@ Description : This is the library wrapper on top of trello apis.
@ Author : Sam Mathew
@ Created on : 08/04/2021
@ Last Modified :  08/04/2021
"""

# Global python imports
import requests

# Local python imports
from trello_auto.config.config_parser import TrelloConfigParser
from trello_auto.core.environment import Environment as EV
from trello_auto.core.log import Log

ui_parser = TrelloConfigParser(EV.UI_PARSER_PATH)


class TrelloGenericApis():
    """This is a class for creating the library api's associated with TC's.
    Attributes:  NA
    """

    def __init__(self, Log=Log.capture_log()):
        self.Log = Log
        self.card_url = "https://api.trello.com/1/cards"
        self.board_url = "https://api.trello.com/1/boards/"
        self.desc = "This is a sample test card created"

    def get_idlist(self, board_name):
        """ This api is for retrieving the idlist via REST APi.
        Parameters: board_name
        Returns:
            int : idlist if successfully retirved else none.
        """

        # api-endpoint
        URL = "https://api.trello.com/1/members/{0}/boards?key={1}&token={2}".\
            format(ui_parser.get("credentials", "user_name"), ui_parser.get("credentials", "key"),
                   ui_parser.get("credentials", "token"))

        test_name = board_name
        r = requests.get(url=URL)

        # extracting data in json format
        data = r.json()

        for i in range(len(data)):
            if data[i]['name'] == test_name:
                id_ = data[i]['id']

        URL2 = "https://api.trello.com/1/boards/{0}/lists?key={1}&token={2}".format(id_,
                   ui_parser.get("credentials", "key"),
                   ui_parser.get("credentials", "token"))
        r = requests.get(url=URL2)

        # extracting data in json format
        data = r.json()
        for i in range(len(data)):
            if data[i]['name'] == "To Do":
                id_ = data[i]['id']
        return id_

    def create_card(self, card_data, board_name):
        """ This api is for creating a card on a board.
        Parameters: card_data, board_name
        Returns:
            bool : true if create card is success else false.
        """
        self.Log.debug("Start creating the card")
        query = {
            'key':  ui_parser.get("credentials", "key"),
            'token':  ui_parser.get("credentials", "token"),
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
        """ This api is for creating a new board.
         Parameters: board_name
         Returns:
            bool : true if create board is success else false.
        """
        self.Log.debug("Start creating a board")
        query = {
            'key':  ui_parser.get("credentials", "key"),
            'token':  ui_parser.get("credentials", "token"),
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
