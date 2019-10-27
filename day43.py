
# Create a Class 
class Computer:
    def __init__(self, name, Type, color):
       self.name = name
       self.Type = Type
       self.color = color 
       print(f'{name} thing is {Type}, and its color is {color}.')


first_computer = Computer('first', 'mac','Black')
second_computer = Computer('secons', 'hp','grey')

class jet(Computer):
    pass 

first_jet= jet('ABC','123', 'white')
