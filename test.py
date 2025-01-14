import unittest
from lb5 import CurrenciesLst
import os

class TestCurrenciesLst(unittest.TestCase):
    def setUp(self):
        self.currencies_lst = CurrenciesLst()

    def test_invalid_id(self):
        self.currencies_lst.set_currencies_ids_lst(['R9999'])
        result = self.currencies_lst.get_currencies(['R9999'])
        self.assertEqual(result, [{'R9999': None}])

    def test_singleton(self):
        currencies_lst1 = CurrenciesLst()
        currencies_lst2 = CurrenciesLst()
        self.assertIs(currencies_lst1, currencies_lst2)
        

    def test_valid_ids(self):
        self.currencies_lst.set_currencies_ids_lst(['R01035', 'R01335', 'R01700J'])
        result = self.currencies_lst.get_currencies(['R01035', 'R01335', 'R01700J'])
        self.assertGreater(len(result), 0)
        self.assertIsInstance(result[0], dict)

    def test_visualize_currencies(self):
        self.currencies_lst.set_currencies_ids_lst(['R01035', 'R01335', 'R01700J'])
        self.currencies_lst.get_currencies(['R01035', 'R01335', 'R01700J'])
        self.currencies_lst.visualize_currencies()
        self.assertTrue(os.path.exists('currencies.jpg'))


if __name__ == '__main__':
    unittest.main()