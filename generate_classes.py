'''Generate the classes needed for the project.'''
import unittest
class Products():
    '''Creates the Game objects, which has an amount, int, and a brand, str.'''
    def __init__(self) -> None:
        '''Creates a default object with no amount or item setting'''
        self.amount = 0
        self.item = ""
    def set_amount(self, amount) -> None:
        '''Sets the amount for the object. Cannot be negative and no error will be raised.'''
        self.amount = amount
    def get_amount(self) -> int:
        '''Returns the amount for the object.'''
        return self.amount
    def set_item(self,item) -> None:
        '''Sets the item setting used by the api. Must be string. Will not raise an error.'''
        self.item = item
    def get_item(self) -> str:
        '''Returns the item setting'''
        return self.item

class TestProduct(unittest.TestCase):
    '''Tests the Products class and its methods.'''
    def setUp(self) -> None:
        '''Creates an object of the Products class'''
        self.products = Products()
    def test_set_amount(self) -> None:
        '''Sets an amount to the object and tests if the number is correct of the Products class.'''
        self.products.set_amount(15)
        self.assertEqual(self.products.get_amount(), 15)
        self.assertIsInstance(self.products, Products)
    def test_set_item(self) -> None:
        '''Sets an item to the object and tests if it is the right item and of the Products class.'''
        self.products.set_item('Mugs')
        self.assertEqual(self.products.get_item(),'Mugs')
        self.assertIsInstance(self.products, Products)

class Games(Products):
    '''Creates the Game object, which has a brand and an amount.'''
    def __init__(self) -> None:
        '''Overrides the super class default constructor and adds the brand variable.'''
        super().__init__()
        self.brand = ""
    def set_brand(self, brand) -> None:
        '''Sets the brand for the object.'''
        self.brand = brand
    def get_brand(self) -> str:
        '''Returns the brand for the object.'''
        return self.brand

class TestGame(unittest.TestCase):
    '''Tests the Games class and its methods.'''
    def setUp(self) -> None:
        '''Creates an object of the Games class to test.'''
        self.game = Games()
    def test_set_brand(self) -> None:
        '''Sets a brand to the object, tests if it is the correct brand and of the Games class.'''
        self.game.set_brand('EA')
        self.assertEqual(self.game.get_brand(),'EA')
        self.assertIsInstance(self.game, Games)

class Books(Products):
    '''Creates the Book objects, which has an author and an amount.'''
    def __init__(self) -> None:
        '''Overrides the super class default constructor and adds the author variable.'''
        super().__init__()
        self.author = ""
    def set_author(self, author) -> None:
        '''Sets the author for the object.'''
        self.author = author
    def get_author(self) -> str:
        '''Returns the author for the object.'''
        return self.author

class TestBook(unittest.TestCase):
    '''Tests the Books class and its methods.'''
    def setUp(self) -> None:
        '''Creates a Book object to test.'''
        self.book = Books()
    def test_set_author(self) -> None:
        '''Sets an author, tests if it is the correct author and of the Books class.'''
        self.book.set_author('Tolkien')
        self.assertEqual(self.book.get_author(),'Tolkien')
        self.assertIsInstance(self.book, Books)

class Merchandise(Products):
    '''Creates the Merchandise objects, which have a type and an amount.'''
    def __init__(self) -> None:
        '''Overrides the super class default constructor and adds the merch variable.'''
        super().__init__()
        self.merch = ""
    def set_merch(self, merch) -> None:
        '''Sets the merch type for the object.'''
        self.merch = merch
    def get_merch(self) -> str:
        '''Returns the merch type for the object.'''
        return self.merch

class TestMerchandise(unittest.TestCase):
    '''Tests the Merchandise class and its methods.'''
    def setUp(self) -> None:
        '''Creates a merchandise object to test.'''
        self.merch = Merchandise()
    def test_set_merch(self) -> None:
        '''Sets a merch type, tests if it is the correct merch type. Should fail.'''
        self.merch.set_merch('Keychains')
        self.assertEqual(self.merch.get_merch(),'Keychains')
        self.assertIsInstance(self.merch, Games)


class BoardGames(Products):
    '''Creates the Board Games objects, which have a name and an amount.'''
    def __init__(self) -> None:
        '''Overrides the super class default constructor and adds the name variable.'''
        super().__init__()
        self.name = ""
    def set_name(self, name) -> None:
        '''Sets the name for the object.'''
        self.name = name
    def get_name(self) -> str:
        '''Returns the name for the object.'''
        return self.name

class TestBoardGames(unittest.TestCase):
    '''Tests BoardGames class and its methods.'''
    def setUp(self) -> None:
        '''Creates a Board Game object.'''
        self.board_game = BoardGames()
    def test_set_name(self) -> None:
        '''Sets a name, tests if it is the correct name, and of the Board Games class. Should fail.'''
        self.board_game.set_name('Candy Land')
        self.assertEqual(self.board_game.get_name(),'Monopoly')
        self.assertIsInstance(self.board_game, BoardGames)


if __name__ == '__main__':
    raise Exception('Sorry this file is not meant to be ran!')
