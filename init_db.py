from datetime import date

from project.clients.models import Clients
from project.books.models import Books
from project.loans.models import Loans
from project import db, app


# ---------- USERS:
client1 = Clients(clientname = "Todd Maddox", age = 37, city = "Bridgnorth")
client2 = Clients(clientname = "Josh Sloan", age = 23, city = "Ipswich")
client3 = Clients(clientname = "Greyson Beltran", age = 52, city = "Saint Augustine")
client4 = Clients(clientname = "Guillermo Blake", age = 41, city = "Bastrop")
client5 = Clients(clientname = "Reynaldo Ho", age = 27, city = "Hutchinson")
client6 = Clients(clientname = "Dayanara Flores", age = 19, city = "Whitehorse")
client7 = Clients(clientname = "Will Foley", age = 25, city = "Olympia")
client8 = Clients(clientname = "Braelyn Fowler", age = 33, city = "Ada")


# ---------- BOOKS:
book1 = Books(bookname = "The Hunger Games", author = "Suzanne Collins", publishdate = "2008-10-14", typeofloan = 1)
book2 = Books(bookname = "Harry Potter and the Order of the Phoenix", author = "J.K. Rowling", publishdate = "2003-06-21", typeofloan = 2)
book3 = Books(bookname = "Pride and Prejudice", author = "Jane Austen", publishdate = "1813-01-28", typeofloan = 3)
book4 = Books(bookname = "To Kill a Mockingbird", author = "Harper Lee", publishdate = "2006-05-23", typeofloan = 1)
book5 = Books(bookname = "The Book Thief", author = "Markus Zusak", publishdate = "2006-03-14", typeofloan = 2)
book6 = Books(bookname = "The Chronicles of Narnia", author = "C.S. Lewis", publishdate = "1956-01-05", typeofloan = 3)
book7 = Books(bookname = "Animal Farm", author = "George Orwell", publishdate = "1945-08-17", typeofloan = 1)
book8 = Books(bookname = "The Little Prince", author = "Antoine de Saint-Exupéry", publishdate = "1943-04-06", typeofloan = 2)


# ---------- LOANS:
loan1 = Loans(customer_id = 8, book_id = 1, loandate = date(2022, 10, 22), returndate = date(2022, 11, 1))
loan2 = Loans(customer_id = 7, book_id = 2, loandate = date(2022, 10, 28), returndate = date(2022, 11, 2))
loan3 = Loans(customer_id = 6, book_id = 3, loandate = date(2022, 11, 1), returndate = date(2022, 11, 3))
loan4 = Loans(customer_id = 5, book_id = 4, loandate = date(2022, 11, 27), returndate = date(2022, 11, 6))
loan5 = Loans(customer_id = 4, book_id = 5, loandate = date(2022, 11, 4), returndate = date(2022, 11, 9))
loan6 = Loans(customer_id = 3, book_id = 6, loandate = date(2022, 11, 9), returndate = date(2022, 11, 11))
loan7 = Loans(customer_id = 2, book_id = 7, loandate = date(2022, 11, 13), returndate = date(2022, 11, 23))
loan8 = Loans(customer_id = 1, book_id = 8, loandate = date(2022, 11, 15), returndate = date(2022, 11, 20))
loan9 = Loans(customer_id = 1, book_id = 8, loandate = date(2021, 11, 15), returndate = date(2021, 11, 20))



with app.app_context():
    db.session.add_all([client1, client2, client3, client4, client5, client6, client7, client8])
    db.session.add_all([book1, book2, book3, book4, book5, book6, book7, book8])
    db.session.add_all([loan1, loan2, loan3, loan4, loan5, loan6, loan7, loan8, loan9])

    db.session.commit()
