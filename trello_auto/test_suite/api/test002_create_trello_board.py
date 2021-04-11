""" TC create trello board"""
import pytest


@pytest.mark.usefixtures("objects_api")
class TestCreateTrelloCard:
    def test_create_trello_card(self):
        board_name = 'bonito'
        assert self.trello_api.create_board(board_name), "Failed to create trello board"
        self.Log.info("Successfully trello board")
