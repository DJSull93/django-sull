from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import pyautogui
import schedule


class Naver_stock(object):

    @staticmethod
    def get_url(company_code):
        url = 'https://finance.naver.com/item/main.nhn?code='
        result = requests.get(f'{url}{company_code}')
        soup = BeautifulSoup(result.content, "html.parser")
        return soup

    def printer(self, company_code):
        self.get_name_stock(company_code)
        self.get_code_price(company_code)

    def get_code_price(self, company_code):
        no_today = self.get_url(company_code).find("p", {"class": "no_today"})
        blind = no_today.find("span", {"class": "blind"})
        print(blind.text)

    def get_name_stock(self, company_code):
        name_stock = self.get_url(company_code).find("div", {"class": "wrap_company"})
        name = name_stock.find("a").text
        print(name)

    @staticmethod
    def daily_run(job, code):
        schedule.every().day.at("10:30").do(job, code)

    @staticmethod
    def main():
        n = Naver_stock()
        while 1:
            now = datetime.now()
            print(now)
            m = input('0. Exit 1. please input stock code 2. Do everyday on time(10:30)')
            if m == '0':
                break
            elif m == '1':
                code = input('stock code :')
                n.printer(code)
                print('*' * 100)
            elif m == '2':
                n.daily_run(n.printer, code)
            else:
                continue

Naver_stock.main()