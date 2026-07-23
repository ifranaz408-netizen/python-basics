class book:
  def __init__(self,title,author,price,available):
    self.title=title
    self.author=author
    self.price=price
    self.available=available
  def display(self):
    print("book title:",self.title)
    print("book author:",self.author)
    print("book price:",self.price)
    print("book available:",self.available)
  def borrow_book(self):
     if self.available:
        self.available = False
        print("Book issued successfully!")
    else:
        print("Sorry, the book is already issued.")
  def return_book(self):
    if  not self.available:
        self.available = True
        print("Book returned successfully!")
    else:
        print("Sorry! the book is already  in the library")
  def discount(self):
    print("Current price: ", self.price)
    your_price=input("entre new price: ")
    self.price = your_price
    print("price update sucessfully!")
    print("new price:" ,self.price)
book1=book("python","ifranaz",500,True)


book1.display()
book1.borrow_book()
book1.return_book()
book1.discount()
book1.display()
    
    
