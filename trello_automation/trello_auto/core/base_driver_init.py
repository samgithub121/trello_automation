"""
@ Description : This is the library created for dealing with the page objects.
@ Author : Sam Mathew
@ Created on : 25/12/2019
@ Last Modified on : 28/12/2019
"""
# Global python imports
import os

# Local python imports
from trello_auto.core.webelements_wrapper import *
from trello_auto.core.environment import Environment as EV
from trello_auto.config.config_parser import LondonTicketConfigParser
from trello_auto.core.log import Log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Local python imports

ui_parser = LondonTicketConfigParser(EV.UI_PARSER_PATH)


class BaseDriverInit(object):

    def __init__(self, Log=Log.capture_log()):
        self.Log = Log
        self.browser = ui_parser.get("common", "browser_name")
        self.platform = ui_parser.get("common", "platform_name")
        self.pageUrl = ui_parser.get("common", "test_url")
        self.exec_mode = ui_parser.get("execution mode", "exec_mode")
        self.initialize_driver()

    def initialize_driver(self):
        if self.browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            options.add_argument("test-type")
            options.add_argument('start-maximized')
            options.add_argument("--disable-extensions")

            options.add_argument("--js-flags=--expose-gc")
            options.add_argument("--enable-precise-memory-info")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-default-apps")
            options.add_argument("test-type=browser")
            options.add_argument("disable-infobars")
            if self.exec_mode == "headless":
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(options=options,
                                           executable_path=os.path.join(EV.TOOLS_PATH, "chromedriver.exe"))
        else:
            self.Log.error("Framework support only for Chrome as of now")
            raise Exception("Framework support only for Chrome as of now")

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)  # implicit wait for 60 sec
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(self.pageUrl)

    def get_web_driver(self):
        return self.driver

    def check_element_visibility(self, timeout, locator, element):
        if locator == "XPATH":
            if WebDriverWait(self.get_web_driver(), timeout). \
                    until(EC.visibility_of_element_located((By.XPATH, element))):
                return True
            else:
                return False
