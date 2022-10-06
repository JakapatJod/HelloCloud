from crud import Session
from models import Book

s = Session()
ิbooks = s.query(Book).all()

for book in books:
    if book.price == None:
        price = input(
            f"Price for '{book.title}': Old Price:'{book.price}' New Price : $"
        book.price = price
        s.add(book)
        )

s.commit()
s.close()