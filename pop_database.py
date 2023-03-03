'''Creates the databases used by the rest of the project files, including the API.'''
import random
import unittest
import os
from generate_classes import Books, Merchandise, BoardGames, Games

def generate_inventory(file_path, file_mode, header, inventory_objects, inventory_list) -> None:
    '''Creates the objects and adds the item and the amount and writes it to a file.'''
    inv_obj = inventory_objects()
    count = 0
    with open(file_path, file_mode, encoding='utf-8') as file:
        file.write(header)
        while count < len(inventory_list):
            item = inventory_list[count]
            amount = random.randint(1, 1000)
            inv_obj.set_amount(amount)
            inv_obj.set_item(item)
            file.write(f"{inv_obj.get_item()},{inv_obj.get_amount()}\n")
            count += 1

def populate_database() -> None:
    '''Creates the array of items and writes them to a file using headers, and the array.'''
    game_array = ["Nintendo","Sony","Microsoft","Ubisoft","EA"]
    book_array = ["Tolkien","Martin","Abnett","Karpyshyn"]
    merch_array = ["Shirts","Mugs","Keychains","Pins","Plushies"]
    bg_array = ["Monopoly","Candy Land","Clue"]
    generate_inventory("Database.csv", 'w', "Brand,Available\n", Games, game_array)
    generate_inventory("Database.csv", 'a', "Author,Available\n", Books, book_array)
    generate_inventory("Database.csv", 'a', "Merchandise,Available\n", Merchandise, merch_array)
    generate_inventory("Database.csv", 'a', "Boardgames,Available\n", BoardGames, bg_array)


class TestGenerateDatabase(unittest.TestCase):
    '''Tests the generation and population of the database.'''
    def setUp(self) -> None:
        '''Creates the test file.'''
        self.database_path = "Database.csv"

    def test_populate_database(self) -> None:
        '''Populates the test file, and tests if the data was added correctly.'''
        populate_database()
        self.assertTrue(os.path.exists(self.database_path))
        with open(self.database_path, "r", encoding='utf-8') as file:
            data = file.read()
            self.assertIn("Brand,Available\n", data)
            self.assertIn("Author,Available\n", data)
            self.assertIn("Merchandise,Available\n", data)
            self.assertIn("Boardgames,Available\n", data)


if __name__ == '__main__':
    populate_database()
    print('Database Generated!')
