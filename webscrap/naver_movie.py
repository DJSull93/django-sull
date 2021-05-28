from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class Naver_movie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_code = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    movie_title = []
    dict = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {"class": self.class_code})
        #for loop 사용, comprehention 사용
        for i in all_div:
            self.movie_title.append(i.find("a").text)
        driver.close()

    def insert_dict(self):
        for i in range(0, len(self.movie_title)):
            self.dict[i+1] = self.movie_title[i]

    def insert_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def make_csv(self):
        path = './data/movieRanking.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')


if __name__ == '__main__':
    naver = Naver_movie()
    naver.class_code = input("input tit3")
    naver.scrap()
    naver.insert_dict()
    naver.insert_dataframe()
    naver.make_csv()