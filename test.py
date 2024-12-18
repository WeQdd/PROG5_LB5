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

    def test_valid_ids(self):
        self.currencies_lst.set_currencies_ids_lst(['R01035', 'R01335', 'R01700J'])
        result = self.currencies_lst.get_currencies(['R01035', 'R01335', 'R01700J'])
        self.assertTrue(any(valute['CharCode'] == 'GBP' for valute in result))
        self.assertTrue(any(valute['CharCode'] == 'USD' for valute in result))
        self.assertTrue(any(valute['CharCode'] == 'EUR' for valute in result))
        self.assertTrue(all(0 <= float(valute['Value'].replace(',', '.')) <= 999 for valute in result))

    def test_visualize_currencies(self):
        self.currencies_lst.set_currencies_ids_lst(['R01035', 'R01335', 'R01700J'])
        self.currencies_lst.get_currencies(['R01035', 'R01335', 'R01700J'])
        self.currencies_lst.visualize_currencies()
        self.assertTrue(os.path.exists('currencies.jpg'))

if __name__ == '__main__':
    unittest.main()