from bs4 import BeautifulSoup
from urllib.request import urlopen
class Bugsmusic(object):
    url = ''

    def __str__(self):
        return f'URL = {self.url}'

#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01

    @staticmethod
    def type(soup):
        print(f'--------------------{type} RANKING--------------------')
        count = 0
        for link1 in soup.find_all(name='p', attrs=({"class": f'{type}'})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{type} : {link1.find("a").text}')

    @staticmethod
    def main():
        bugs = Bugsmusic()
        soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
        while 1:
            menu = int(input(f'0. exit\n1. Input URL\n2. Artist Ranking\n3. Title Ranking\n4. delete\n'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URL\n')
            elif menu == 2:
                print(f'input URL is {bugs}')
                print(Bugsmusic.type(str('artist')))

            elif menu == 3:
                print(f'input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                print('--------------------TITLE RANKING--------------------')
                count = 0
                for link1 in soup.find_all(name='p', attrs=({"class": "title"})):
                    count += 1
                    print(f'{str(count)} RANKING')
                    print(f'ARTIST: {link1.find("a").text}')
            else:
                print('Wrong Number')
                continue

Bugsmusic.main()