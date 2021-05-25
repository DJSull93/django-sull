from urllib.request import urlopen
from bs4 import BeautifulSoup

class Melon(object):

    url = ''

    def set_rul(self, url):
        self.url = url

    @staticmethod
    def scrap():
        soup = BeautifulSoup(urlopen(mel.url), 'lxml')
        count = 0
        for i in soup.find_all(name='div', attrs=({"class": "ellipsis rank01"})):
            count += 1
            print(f'{count} Rank')
            print(f'artist : {i.found("a").text}')

    @staticmethod
    def main():
        mel = Melon()
        while 1:
            m = input('1. input URL\n2. print TOP 100')
            if m == '1':
                mel.set_url = input('input URL')
            elif m == '2':
                mel.grt_ranking()
            else:
                continue
# https://www.melon.com/chart/index.htm
Melon.main()