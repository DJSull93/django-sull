from titanic.views.controller import Controller
from titanic.templates.plot import Plot


if __name__ == '__main__':
    while 1:
        m = input('0. exit\n'
                  '1. data visualization\n'
                  '2. modeling\n'
                  '3. machine learning\n'
                  '4. machine release\n'
                  '')
        if m == '0':
            break
        elif m == '1':
            plot = Plot('train.csv')
            plot.draw_survived_dead()
            #plot.draw_pclass()
            #plot.draw_sex()
            #plot.draw_embarked()
        elif m == '2':
            Controller().modeling('train.csv', 'test.csv')
        elif m == '3':
            Controller().learning('train.csv', 'test.csv')
        elif m == '4':
            Controller().submit('train.csv', 'test.csv')
        else:
            continue
