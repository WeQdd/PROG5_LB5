import requests
from xml.etree import ElementTree as ET
import time
import matplotlib.pyplot as plt

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CurrenciesLst(metaclass=SingletonMeta):
    def __init__(self):
        self.__cur_lst = []
        self.__currencies_ids_lst = []
        self.__last_request_time = 0
        self.__request_interval = 1  # в секундах

    def get_currencies(self, currencies_ids_lst):
        if time.time() - self.__last_request_time < self.__request_interval:
            return [{'R9999': None}]

        self.__last_request_time = time.time()
        self.__currencies_ids_lst = currencies_ids_lst

        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        result = []

        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")
        for _v in valutes:
            valute_id = _v.get('ID')
            valute = {}
            if str(valute_id) in currencies_ids_lst:
                valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find('Value').text
                valute_charcode = _v.find('CharCode').text
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                result.append(valute)

        self.__cur_lst = result
        return result

    def visualize_currencies(self):
        fig, ax = plt.subplots()
        currencies = []
        for el in self.__cur_lst:
            currencies.append(str(el.keys()))

        for el in self.__cur_lst:
            for key, value in el.items():
                ax.bar(key, float(value[1].replace(',', '.')))

        plt.show()

    def get_cur_lst(self):
        return self.__cur_lst

    def set_cur_lst(self, cur_lst):
        self.__cur_lst = cur_lst

    def get_currencies_ids_lst(self):
        return self.__currencies_ids_lst

    def set_currencies_ids_lst(self, currencies_ids_lst):
        self.__currencies_ids_lst = currencies_ids_lst

    def get_last_request_time(self):
        return self.__last_request_time

    def set_last_request_time(self, last_request_time):
        self.__last_request_time = last_request_time

    def get_request_interval(self):
        return self.__request_interval

    def set_request_interval(self, request_interval):
        self.__request_interval = request_interval


if __name__ == '__main__':
    currencies_lst = CurrenciesLst()
    res = currencies_lst.get_currencies(['R01035', 'R01335', 'R01700J'])
    if res:
        print(res)
        currencies_lst.visualize_currencies()