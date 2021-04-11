""" TC create trello card"""
import pytest


@pytest.mark.usefixtures("objects_api")
class TestCreateTrelloCard:
    def test_create_trello_card(self):
        board_name = "bla bla"
        assert self.trello_api.create_card(self.random_data.get_random_card_detail(), board_name), "Failed to create trello card"
        self.Log.info("Successfully created card on trello board")
