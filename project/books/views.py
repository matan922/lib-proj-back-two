from flask import render_template, redirect, Blueprint, request
from project import db
from project.books.models import Books

books = Blueprint('books', __name__, template_folder='templates', url_prefix = '/books')

'''Function that shows books based on index given in the url's endpoint
or shows all books if no index was given.
Default is set to show all books.'''
@books.route("/", methods=["GET"])
@books.route("/<ind>")
def show_book_list(ind = -1):
    res=[]
    if int(ind) is -1:
        for book in Books.query.all():
            res.append({"book_name":book.bookname,"id":book.id,"author":book.author,"publish_date": book.publishdate,"type_of_loan": book.typeofloan})
        return res
    if int(ind) > -1:
        book = Books.query.get(ind)
        res.append({"book_name":book.bookname,"id":book.id,"author":book.author,"publish_date": book.publishdate,"type_of_loan": book.typeofloan})
        return res
            

'''Function made to search a specific book based 
on the index given in the url's endpoint from the function above.'''
@books.route("/book_search", methods=['POST'])
def books_name():
    name = request.form['bookname']
    book = Books.query.filter(Books.bookname==name).first()
    if book is None:
        return redirect('/books')
    return redirect(f"{book.id}") 

# Function made to render a page where a user can add a new book to the library.
# @books.route("/add_book")
# def new_book_page():
#     return render_template('add_book.html')

# Function made to add a new book from the page created by previous function.
@books.route("/add_book", methods=['POST'])
def add_books():
    # Making a form that connects to the <form> html tag for user input.
    request_data = request.json
    print(request_data)
    bookname= request_data["bookname"]
    author = request_data["author"]
    publishdate = request_data["publishdate"]
    typeofloan = request_data["typeofloan"]
    new_book = Books(bookname,author,publishdate,typeofloan)
    db.session.add(new_book)
    db.session.commit()
    return "success"
# Function made to delete a book from the databse based on the index (id) of the book.

@books.route("/books_del", methods=['GET'])
@books.route("/books_del/<ind>")
def delete_book(ind):
    book = Books.query.get(ind)
    if book.id == int(ind):
        db.session.delete(book)
        db.session.commit()
    return [{"book_name":book.bookname,"id":book.id,"author":book.author,"publish_date": book.publishdate,"type_of_loan": book.typeofloan}]

    # if book is None:
    #     return render_template('all_books.html', books=Books.query.all())
    # try:
    #     db.session.delete(book)
    #     db.session.commit()
    # except:
    #     return render_template('all_books.html', books=Books.query.all())
    # return render_template('all_books.html', books=Books.query.all())




