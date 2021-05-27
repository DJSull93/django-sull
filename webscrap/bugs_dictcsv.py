from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
from pandas import DataFrame

class Bugs(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None
    cs = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            self.title_ls.append(i.find("a").text)
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[0]})):
            self.artist_ls.append(i.find("a").text)

    # key = title, value = name
    def insert_dict(self):
        d = self.dict
        for i in range(0, len(self.title_ls)):
            d[self.title_ls[i]] = self.artist_ls[i]
        print(d)

    def insert_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def insert_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        b = Bugs()
        while 1:
            m = input('1. input 2. output 3. dictionary print 4. dict to Dataframe 5. DF to csv')
            if m == '1':
                b.set_url('wl_ref=M_contents_03_01')
            elif m == '2':
                b.class_name.append("artist")
                b.class_name.append("title")
                b.get_ranking()
            elif m == '3':
                b.insert_dict()
            elif m == '4':
                b.insert_dataframe()
            elif m == '5':
                b.insert_csv()
            else:
                print('wrong numb')
Bugs.main()