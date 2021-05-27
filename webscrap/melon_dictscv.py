import urllib.request

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from pandas import DataFrame

class Bugs2(object): # 크롤링 베이스 형태
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all("div", {"class": self.class_name[0]}):
            self.title_ls.append(i.find("a").text)
        for i in soup.find_all("div", {"class": self.class_name[1]}):
            self.artist_ls.append(i.find("a").text)

    def insert_dict(self):
        d = self.dict
        for i in range(0, len(self.title_ls)):
            d[self.title_ls[i]] = self.artist_ls[i]
        print(d)

    def insert_dF(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def insert_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            m = input('1. input date 2. output 3. dict 4. dataframe 5. csv')
            if m == '1':
                b.set_url('2021052513')
            elif m == '2':
                b.class_name.append('ellipsis rank01')
                b.class_name.append('ellipsis rank02')
                b.get_ranking()
            elif m == '3':
                b.insert_dict()
            elif m == '4':
                b.insert_dF()
            elif m == '5':
                b.insert_csv()
            else:
                print('wrong numb')

Bugs2.main()