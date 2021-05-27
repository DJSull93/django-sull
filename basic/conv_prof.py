import pandas as pd
from pandas import Series, DataFrame

class Conversion(object):
    @staticmethod
    def con_1() -> ():    ## '-> ()' 값이 튜플임을 명시
        return (1, 2, 3, 4, 5, 6, 7, 8, 9)

    @staticmethod
    def con_2(t) -> []:
        return list(t)

    @staticmethod
    def con_3(ls) -> []:
        return [float(i) for i in ls]

    @staticmethod
    def con_4(ls) -> []:
        return [int(i) for i in ls]

    @staticmethod
    def con_5(ls) -> {}:
        return dict(zip([str(i) for i in ls], ls))

    @staticmethod
    def con_6(st) -> ():
        return tuple(list(st))

    @staticmethod
    def con_7(tp) -> []:
        return list(tp)

    @staticmethod
    def con_8(dict) -> object:
        return pd.DataFrame(dict, index=['index'])

    @staticmethod
    def main():  # use return in method
        c = Conversion()
        tp = ()
        ls = []
        dc = {}
        df = ({})
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
                tp = c.con_1()
                print(tp)
            # change tuple(num1) to list
            elif m == '2':
                ls = c.con_2(tp)
                print(ls)
            # make num2 list convert to float type
            elif m == '3':
                ls = c.con_3(ls)
                print(c.con_3(ls))
            # make list numb3 convert to int type list
            elif m == '4':
                ls = c.con_4(ls)
                print(c.con_4(ls))
            # make list num2 convert in dictionary, key is index which str type
            elif m == '5':
                dc = c.con_5(ls)
                print(c.con_5(dc))
            # make 'hello' to tuple
            elif m == '6':
                tp = c.con_6('hello')
                print(c.con_6(tp))
            # make num6 tuple to list
            elif m == '7':
                ls = c.con_7(tp)
                print(c.con_7(ls))
            # make num5 dict to dataframe
            elif m == '8':
                tp = c.con_1()
                ls = c.con_2(tp)
                dc = c.con_5(ls)
                df = c.con_8(dc)
                print(df)


            else:
                continue


Conversion.main()