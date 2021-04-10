"""
@ Description : This is the main file on pytest where the fixtures are handled here.
@ Author : Sam Mathew
@ Created on : 25/12/2019
@ Last Modified : 28/12/2019
"""

# Global Python Imports
import pytest

# Local python imports
from trello_auto.library.ui.trello_operations import TrelloOperations
from trello_auto.library.api.trello_generic_api import TrelloGenericApis
from trello_auto.core.log import Log
from trello_auto.config.csv_parser import CsvParser


@pytest.fixture(scope='function')
def launch_close_fixture(request):
    """ This fixture is for initializing the fixture and objects for the test.
    Parameters: request
    Returns: object
    """
    request.cls.page = TrelloOperations()
    request.cls.Log = Log().capture_log()
    request.cls.random_data = CsvParser()
    # Test case setup part can do here
    yield
    # Test case tear down part can do here
    request.cls.page.close()


@pytest.fixture(scope='function')
def objects_api(request):
    """ This fixture is for initializing the fixture and objects for the test.
    Parameters: request
    Returns: object
    """
    request.cls.trello_api = TrelloGenericApis()
    request.cls.Log = Log().capture_log()
    request.cls.random_data = CsvParser()



