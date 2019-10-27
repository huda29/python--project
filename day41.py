#Python Classes and Objects 
class Greet:
    def __init__(self, name):
        self.name = name

    def work(self):
        self.job = input(f'Hello {self.name}, what is your job?' )
        print(f'{self.name},===> {self.job}')


first = Greet('huda')
first.work()
second = Greet('Nada')
second.work()