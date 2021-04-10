"""
@ Description : This py file acts as a configurable file for all the
operations in this framework.
@ Author : Sam Mathew
@ Created on : 25/12/2019
@ Modified on : 28/12/2019

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

        # printing the field names
        # print('Field names are:' + ', '.join(field for field in fields))

        for row in self.rows[:int(csvreader.line_num) - 1]:
            self.final_data_set.append(row[0])
        return random.choice(self.final_data_set)
