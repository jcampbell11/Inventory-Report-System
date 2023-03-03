'''Creates the Inventory Report using the data gathered by the API and displays it.'''
import webbrowser
import unittest
import csv
from typing import Dict
import pandas as pd
from pop_database import populate_database




class InventoryAPI:
    '''Class creates the api and reads the data from the database.'''
    def __init__(self, filename) -> None:
        self.filename = filename

    def read_data(self) -> Dict[str,int]:
        '''Reads the data from the database and creates a dictionary for each header.'''
        inv_data = {}
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'Brand' in row:
                    key = row['Brand']
                elif 'Author' in row:
                    key = row['Author']
                elif 'Merchandise' in row:
                    key = row['Merchandise']
                elif 'Boardgames' in row:
                    key = row['Boardgames']
                else:
                    continue
                try:
                    available = int(row['Available'])
                except ValueError:
                    continue
                inv_data[key] = available
        return inv_data

class TestAPI(unittest.TestCase):
    '''Tests the API and Read data'''
    def setUp(self) -> None:
        '''Creates the test API'''
        self.api = InventoryAPI('Database.csv')
    def test_read_data(self) -> None:
        '''Test the read data method and if the data read is correct.'''
        data = self.api.read_data()
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)
        for key in data:
            self.assertIsInstance(key, str)
            self.assertIsInstance(data[key], int)

def generate_report() -> None:
    '''Generates the game portion of the report, and creates the file.'''
    api = InventoryAPI('Database.csv')
    inv_data = api.read_data()
    inv_df = pd.DataFrame.from_dict(inv_data, orient='index', columns=['Available'])
    inv_df.index.name='Item'
    inv_df.to_csv('Inventory_Report.csv', sep='\t', float_format='%>.2f', index_label='Item')
    print(inv_df)

def open_file(file_name) -> None:
    '''Opens the file specified in main().'''
    webbrowser.open(file_name)

def main() -> None:
    '''Ensures all needed functions run at the right time and the report is created and
    opened after all functions are ran.'''
    populate_database()
    generate_report()
    open_file('Inventory_Report.csv')

if __name__ == "__main__":
    main()
    print('Here is the Report!')
