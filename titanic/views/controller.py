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
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Trains type is {type(this.train)}')
        print(f'Trains colums is \n{this.train.columns}')
        print(f'tests type is {type(this.test)}')
        print(f'tests colums is \n{this.test.columns}')
        return this