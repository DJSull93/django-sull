import pandas as pd
from pandas import Series, DataFrame

class Conversion(object):
    i = 0
    f = 0.0
    s = ''
    ls = []
    t = ()
    d = {}
    ts = ()

    def con_1(self):
        self.t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        return self.t
    def con_2(self):
        self.t = list(self.t)
        return self.t
    def con_3(self):
        self.t = list(map(float, self.t))
        return self.t
    def con_4(self):
        self.t = list(map(int, self.t))
        return self.t
    def con_5(self):
        for i in range(0, len(self.t)):
            self.d[i] = self.t[i]
        return self.d
    def con_6(self):
        self.ts = ('h', 'e', 'l', 'l', 'o')
        return self.ts
    def con_7(self):
        self.ts = list(self.ts)
        return self.ts
    def con_8(self):
        self.ts = pd.DataFrame(self.d, index=['number'])
        return self.ts

    @staticmethod
    def main(): # use return in method
        c = Conversion()
        while 1:
            m = input('0. exit\n'
                      '1. make tuple\n'
                      '2. tuple > list\n'
                      '3. list in float type\n'
                      '4. list in int type\n'
                      '5. list > dicti\n'
                      '6. make tuple with hello\n'
                      '7. tuple > list\n'
                      '8. dict > dataframe')
            if m == '0':
                break
            # insert tuple 1~10
            elif m == '1':
                print(c.con_1())
            # change tuple(num1) to list
            elif m == '2':
                print(c.con_2())
            # make num2 list convert to float type
            elif m == '3':
                print(c.con_3())
            # make list numb3 convert to int type list
            elif m == '4':
                print(c.con_4())
            # make list num2 convert in dictionary, key is index which str type
            elif m == '5':
                print(c.con_5())
            # make 'hello' to tuple
            elif m == '6':
                print(c.con_6())
            # make num6 tuple to list
            elif m == '7':
                print(c.con_7())
            # make num5 dict to dataframe
            elif m == '8':
                print(c.con_8())


            else:
                continue

Conversion.main()