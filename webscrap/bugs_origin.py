from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class Bugs(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_dict = {}

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def ger_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------------TITLE------------')
        for i in soup.find_all(name='p', attrs=({"class":self.class_name[0]})):
            print(f' {i.find("a").text}')
        print('------------ARTIST------------')
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            print(f' {i.find("a").text}')

    # title : key, name : value
    def insert_title_dict(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------------TITLE------------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            print(f' {i.find("a").text}')
        print(self.title_dict)

    @staticmethod
    def main():
        b = Bugs()
        while 1:
            m = input('1. input 2. output')
            if m == 1:
                b.set_url()
            elif m == 2:
                b.set_url.append("artist")
                b.set_url.append("title")
                b.ger_ranking()
            else:
                print('wrong numb')
Bugs.main()