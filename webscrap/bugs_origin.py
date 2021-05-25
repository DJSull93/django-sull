from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class Bugs(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = f'{time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def ger_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------------TITLE------------')
        for i in soup.find_all(name='p', attrs=({"class":self.class_name[0]}))
            print(f' {i.find("a").text}')
        print('------------ARTIST------------')
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
            print(f' {i.find("a").text}')
    @staticmethod
    def main():
        m = input('1. input 2. output')
        while 1:
            b = Bugs()
            if m == 1:
                b.set_url()
            elif m == 2:
                b.set_url.append("artist")
                b.set_url.append("title")
                b.ger_ranking()
            else:
                print('wrong numb')
Bugs.main()