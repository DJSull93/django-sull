class Gugudan(object):
    dan = 0
    dict = {}
    def cal_gu(self):
        for i in range(1, 10):
            print(f'{self.dan} * {i} = {self.dan * i}')
            i += 1

    def cal_all(self):
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')

    def print_dict_dan(self):
        d = self.dict
        for i in range(1,10):
            d[i] = self.dan * i
        print('Dictionary print')
        print(d)
        for k in d.keys():
            print(f'{self.dan} * {k} = {d.get(k)}')


    @staticmethod
    def main():
        g = Gugudan()
        while 1:
            m = input('1. input dan\n2. print all gugudan\n3. input dan in dict\n')
            if m == '1':
                g.dan = int(input('input dan'))
                g.cal_gu()
            elif m == '2':
                g.cal_all()
            elif m == '3':
                g.dan = int(input('input dan'))
                g.print_dict_dan()
            else:
                continue
Gugudan.main()
