# Create a Class 
class Computer:
    def __init__(self, name, Type, color):
       self.name = name
       self.Type = Type 
       self.color = color 
       print(f'{name} computer is {Type}, and its color is {color}.')


first_computer = Computer('first', 'mac','Black')
second_computer = Computer('secons', 'hp','grey')
