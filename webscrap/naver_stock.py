from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time, datetime
import pyautogui
import schedule


class Naver_stock(object):

    url = 'https://finance.naver.com/item/main.nhn?code='
    company_code = ''

    def get_code(self):
        result = requests.get(self.url)
        soup = BeautifulSoup(result.content, "html.parser")
        return soup
