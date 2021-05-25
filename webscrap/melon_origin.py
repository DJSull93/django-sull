import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugs2(object): # 크롤링 베이스 형태
    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        print('-----------TITLE-----------')
        for i in soup.find_all("div", {"class": self.class_name[0]}):
            print(f' {i.find("a").text}')
        print('-----------ARTIST-----------')
        for i in soup.find_all("div", {"class": self.class_name[1]}):
            print(f' {i.find("a").text}')

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            m = input('1. input date 2. output')
            if m == '1':
                b.set_url('2021052513')
            elif m == '2':
                b.class_name.append('ellipsis rank01')
                b.class_name.append('ellipsis rank02')
                b.get_ranking()
            else:
                print('wrong numb')

Bugs2.main()