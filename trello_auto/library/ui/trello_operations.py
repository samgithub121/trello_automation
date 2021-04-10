"""
@ Description : This is the library created for dealing with the page objects.
@ Author : Sam Mathew
@ Created on : 09/04/2021
@ Last Modified : 09/04/2021
"""

# Global python imports
from time import sleep

# Local python imports
from trello_auto.core.base_driver_init import BaseDriverInit, ActionChains, EC
from trello_auto.config.config_parser import LondonTicketConfigParser
from trello_auto.core.environment import Environment as EV
from trello_auto.core.log import Log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ui_parser = LondonTicketConfigParser(EV.UI_PARSER_PATH)


class BaseParent(object):
    """ This is the base class for initialising the log class and
        the driver class.
    Attributes:  Log
    """
    base = None

    def __init__(self, Log=Log.capture_log()):
        self.Log = Log
        BaseParent.base = BaseDriverInit()

    def get_driver(self):
        return self.base.get_web_driver()


class TrelloOperations(BaseParent):
    """This is a class for creating the library api's associated with TC's.
    Attributes:  NA
    """

    def __init__(self):

        BaseParent.__init__(self)

    def login_to_account(self):
        """ This api is to login a account via UI operation.
        Parameters: NA
        Returns:
          bool: true if login to account is success else false.
        """
        try:
            self.Log.debug("Login to account")
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "txt_gmail")):
                self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "txt_gmail")). \
                    send_keys(ui_parser.get("credentials", "user_name"))

            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "btn_login_atlassian")):
                submit_btn = self.get_driver().find_element_by_xpath(
                    ui_parser.get("Ui Elements", "btn_login_atlassian"))
                submit_btn.click()
            sleep(5)
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "txt_password")):
                self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "txt_password")). \
                    send_keys(ui_parser.get("credentials", "password"))
            sleep(5)
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "btn_login_submit")):
                submit_btn = self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "btn_login_submit"))
                submit_btn.click()
            return True
        except Exception as ex:
            self.Log.error("Exception occurred at - search_for_story {0}".format(ex))
            return False

    def open_board(self, board_name):
        """ This api is for opening a board.
        Parameters: board_name
        Returns:
           bool: true if launching a board is success else false.
       """
        try:
            self.Log.debug("Start opening a board")
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "menu_board_list")):
                submit_btn = self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "menu_board_list"))
                submit_btn.click()

            if self.base.check_element_visibility(timeout=20, locator="XPATH",
                                                  element=ui_parser.get("Ui Elements", "search_for_board")):
                self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "search_for_board")). \
                    send_keys(board_name)
            sleep(5)
            if WebDriverWait(self.get_driver(), 20). until(EC.visibility_of_element_located((By.XPATH,
                                                                    '//*[@title="{0}"]'.format(board_name)))):
                submit_btn = self.get_driver().find_element_by_xpath('//*[@title="{0}"]'.format(board_name))
                submit_btn.click()
            self.Log.info("Successfully opened a board")
            return True
        except Exception as ex:
            self.Log.error("Exception occurred at - open_board {0}".format(ex))
            return False

    def create_card(self, card_data):
        """ This api is for creating a card on a board via UI operation.
        Parameters: NA
        Returns:
            bool: true if card creation is success else false.
        """
        try:
            if self.base.check_element_visibility(timeout=20, locator="XPATH",
                                                  element=ui_parser.get("Ui Elements", "txt_another_card")):
                self.Log.info("Second case")
                btn = self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "txt_another_card"))
                btn.click()
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "card_type_area")):
                self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "card_type_area")). \
                    send_keys(card_data)
                    # send_keys(ui_parser.get("Ui Elements", "card_data_to_pass"))
            sleep(5)
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "btn_add_card")):
                submit_btn = self.get_driver().find_element_by_xpath(ui_parser.get("Ui Elements", "btn_add_card"))
                submit_btn.click()
            if self.base.check_element_visibility(timeout=20, locator="XPATH", element=ui_parser.get("Ui Elements", "card_generated")):
                return True
        except Exception as ex:
            self.Log.error("Exception occurred at - create_card {0}".format(ex))
            return False

    def close(self):
        """ This api is for closing the driver.
        Parameters: NA
        Returns:
            bool: true if closing driver is success else false.
        """
        self.base.driver.quit()
