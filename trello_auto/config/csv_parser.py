"""
@ Description : This is a parser file for the csv data set using as part of this project..
@ Author : Sam Mathew
@ Created on : 10/04/2021
@ Modified on : 11/04/2021

"""

import csv
import random
from trello_auto.core.environment import Environment as EV


class CsvParser:
    def __init__(self):
        self.filename = EV.DATA_SET_PATH
        self.fields = []
        self.rows = []
        self.final_data_set = []

    def get_random_card_detail(self):
        # reading csv file
        with open(self.filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                self.rows.append(row)

        for row in self.rows[:int(csvreader.line_num) - 1]:
            self.final_data_set.append(row[0])
        return random.choice(self.final_data_set)
