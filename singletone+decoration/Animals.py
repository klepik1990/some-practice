from Singletone import Singlet

class Animals(Singlet):

    def __init__(self, weight):

        self.weight = weight
        instances = None

    def decorator(func):
        def sayHi(self):
            print('Привет, человек')
            func(self)
        return sayHi

    @decorator
    def get_weight(self):
        print('Мой вес: {}'.format(self.weight))
