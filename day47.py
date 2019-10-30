#day 47 challenge

class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf


class Science_Sections(Library):
    def __init__(self, book, shelf):
        super(). __init__(book, shelf)

        self.name = 'Physics book'

science = Science_Sections(20, 4)
print(science.book, science.shelf, science.name)

