""" TC create card trello board"""

import pytest


@pytest.mark.usefixtures("launch_close_fixture")
class TestCreateCardTrelloBoard:
    def test_create_card_trello_board(self):
        board_name = "bonito board"
        assert self.page.login_to_account(), "Failed to login to trello-account"
        self.Log.info("Successfully login to trello-account")
        assert self.page.open_board(board_name), "Failed to open board"
        self.Log.info("Successfully opened board")
        assert self.page.create_card(self.random_data.get_random_card_detail()), "Failed to create a card"
        self.Log.info("Successfully created card")
