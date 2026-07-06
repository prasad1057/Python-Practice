'''
1. Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook
'''


class Book:
    
    def __init__(self, book_id=None, book_name=None, price=None, author=None):
        self.bid = book_id
        self.bname = book_name
        self.price = price
        self.author = author
        
        
    def showBook(self):
        print(f'Book ID: {self.bid}\nBook Name: {self.bname}\nBook Price: {self.price}\nBook Author: {self.author}')
        
    
    def __del__(self):
        print('Book Destructor Method')
        
        
        
# Parametrized object
b1 = Book(101, 'Pokemon Book', 10, 'Prasad')
b1.showBook()

print('------------------------')

# Parameterless object
b2 = Book()     #No values passed — still works because of:book_id=None
b2.showBook()