from titanic.models.service import Service
from titanic.models.dataset import Dataset
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):

    dataset = Dataset()
    service = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)

    def draw_survived_dead(self):
        this = self.entity
        # print(f'Trains type is {type(this)}')
        # print(f'Trains colums is \n{this.columns}')
        # print(f'Trains TOP 5 data is \n{this.head()}')
        # print(f'Trains BOTTOM 5 data is \n{this.tail()}')
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0, dead vs 1. alive')
        ax[0].set_ylabel('')
        ax[1].set_title('0, dead vs 1. alive')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def draw_pclass(self):
        this = self.entity
        this["Survived(human)"] = this["Survived"].replace(0, "Perish").replace(1, "Survived")
        this["Pclass(human)"] = this["Pclass"].replace(1, "1st").replace(2, "2nd").replace(3, "3rd")
        sns.countplot(data=this, x="Pclass(human)", hue="Survived(human)")
        plt.show()

    def draw_sex(self):
        this = self.entity
        this["Survived(human)"] = this["Survived"].replace(0, "Perish").replace(1, "Survived")
        sns.countplot('Sex', data=this, hue='Survived(human)')
        plt.show()


    def draw_embarked(self):
        this = self.entity
        this["Embarked(human)"] = this["Embarked"].replace("C", "Cherbourg").replace("S", "Southampton").replace("Q", "Queenstown")
        sns.countplot(x="Embarked(human)", data=this, hue="Survived(human)")
        plt.show()

'''
Trains type is <class 'pandas.core.frame.DataFrame'>
Trains colums is 
Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')
Trains TOP 5 data is 
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]
Trains BOTTOM 5 data is 
     PassengerId  Survived  Pclass  ...   Fare Cabin  Embarked
886          887         0       2  ...  13.00   NaN         S
887          888         1       1  ...  30.00   B42         S
888          889         0       3  ...  23.45   NaN         S
889          890         1       1  ...  30.00  C148         C
890          891         0       3  ...   7.75   NaN         Q
'''