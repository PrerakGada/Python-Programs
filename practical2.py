class BookStore:
  noOfBooks = 0

  def __init__(self, title, author, qty, price):
    self.title = title
    self.author = author
    self.qty = qty
    self.price = price
    BookStore.noOfBooks += 1

  def bookInfo(self):
    print("Book title:", self.title)
    print("Book author:", self.author)
    print("Book qty:", self.qty)
    print("Book price:", self.price, "\n\n\n")

  def modf(self):
    new_qty = int(input("\nEnter New qty of book:-"))
    new_price = float(input("Enter New price of book:-"))
    self.qty = new_qty
    self.price = new_price

# Driver Code
books = []
print("Enter Number of Books: ")
n = int(input())
for i in range(n):
  print("Enter title,author,quantity and price of book", i + 1)
  title = input()
  author = input()
  qty = int(input())
  price = float(input())
  books.append(BookStore(title, author, qty, price))

for x in books:
  x.bookInfo()

for x in books:
  x.modf()

for x in books:
  x.bookInfo()

print("BookStore.noOfBooks:", BookStore.noOfBooks)
