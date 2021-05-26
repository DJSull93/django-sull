'''
구구단 프로그램은 단을 입력받고, 받은 단의 1~9의 곱을 출력하는 앱이다.
단, 단은 정수이다.
'''
class Gugudan(object):

    dan = 0

    def calcul_dan(self):
        for i in range(1, 10):
            if i < 10:
                print(f'{self.dan} * {i} = {self.dan * i}')
                i += 1
            else:
                break


    @staticmethod
    def main():
        g = Gugudan()
        while 1:
            m = input('0. Exit\n1. input dan\n')
            if m == '0':
                break
            elif m == '1':
                g.dan = int(input('input dan'))
                g.calcul_dan()
            else:
                continue

Gugudan.main()