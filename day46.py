#day 46 challenge
class Library:
    def __init__(self):
        self.book = 45
        self.shelf = 300


class Science_Sections(Library):
    def __init__(self):
        super().__init__()
        self.name = 'Physics book'


science = Science_Sections()
print(science.book, science.shelf, science.name)

