import pandas as pd
from titanic.models.service import Service
from titanic.models.dataset import Dataset
from sklearn.ensemble import RandomForestClassifier


class Controller(object):

    service: object = Service()
    dataset: object = Dataset()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self, train, test) -> object:
        this = self.modeling(train, test)
        print(f'SVC Algorithm Accuracy of Sikit-Learn\n : {self.service.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    def preprocess(self, train, test):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Name', 'Sex', 'Age', 'Fare', 'Cabin', 'Ticket')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'1. Trains type is {type(this.train)}')
        print(f'2. Trains colums is \n{this.train.columns}')
        print(f'3. Trains TOP is \n{this.train.head()}')
        print(f'4. Trains number of null is \n{this.train.isnull().sum()}')
        print(f'5. Tests type is {type(this.test)}')
        print(f'6. Tests colums is \n{this.test.columns}')
        print(f'7. Tests TOP is \n{this.test.head()}\n')
        print(f'8. Tests number of null is \n{this.train.isnull().sum()}')
        print('*' * 100)