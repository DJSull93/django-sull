from titanic.models.service import Service
from titanic.models.dataset import Dataset


class Controller(object):

    service: object = Service()
    dataset: object = Dataset()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        # make model prototype
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        # Eliminates unnecessary features (Cabin, Ticket)
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        # Structuring by nominal, ordinal
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        # eliminate 'Name'
        this = service.drop_feature(this, 'Name')
        this = service.gender_nominal(this)
        this = service.drop_feature(this, 'Sex')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'Trains type is {type(this.train)}')
        print(f'Trains colums is \n{this.train.columns}')
        print(f'Trains TOP5 is \n{this.train.head()}')
        print(f'tests type is {type(this.test)}')
        print(f'tests colums is \n{this.test.columns}')
        print(f'tests TOP5 is \n{this.test.head()}')
        print('*' * 100)