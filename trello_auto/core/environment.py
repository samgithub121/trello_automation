"""
@ Description : This py file acts as a configurable file for all the
operations in this framework.
@ Author : Sam Mathew
@ Created on : 10/04/2021
@ Modified on : 11/04/2021

"""
# Global python import
import os


class Environment:
    """This is a class for tracking the framework path structure.
       Attributes:  NA
    """
    main_directory_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    CONFIG_FOLDER_PATH = os.path.join(main_directory_path, "config")
    CORE_FOLDER_PATH = os.path.join(main_directory_path, "core")
    LIBRARY_FOLDER_PATH = os.path.join(main_directory_path, "library")
    TEMP_FOLDER_PATH = os.path.join(main_directory_path, "temp")
    UI_PARSER_PATH = os.path.join(CONFIG_FOLDER_PATH, "uiconfig.ini")
    TEST_SUITE_PATH = os.path.join(main_directory_path, "test_suite")
    REPORT_PATH = os.path.join(main_directory_path, "reports")
    TOOLS_PATH = os.path.join(main_directory_path, "tools")
    DATA_SET_PATH = os.path.join(main_directory_path, "config", "trello_data_set.csv")
