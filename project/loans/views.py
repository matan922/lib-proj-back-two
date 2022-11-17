from flask import Blueprint, render_template, request, redirect, flash
from project import db
from datetime import datetime, timedelta
from project.clients.models import Clients
from project.loans.models import Loans
from project.books.models import Books

loans = Blueprint('loans', __name__, template_folder = 'templates', url_prefix = '/loans')

# Function made to render a page showing all loans.
@loans.route("/", methods=['GET'])
def loan_list():
    loans = Loans.query.all()
    return render_template('loans.html', loans=loans)

# Function made to render a page where a user can create a new loan.
@loans.route("/add_loan")
def new_loan_page():
    books = Books.query.all()
    clients = Clients.query.all()
    return render_template('add_loan.html', books = books, clients = clients)

# Function made to create a new loan from the page created by previous function.
@loans.route("/", methods=['POST'])
def loan():
    # Making a form that connects to the <form> html tag for user input.
    request_data = request.form
    customer_id = int(request_data["customer_id"])
    book_id = int(request_data["book_id"])
    # Sets automatic date upon creation of a loan (always the current date).
    loandate = datetime.today()
    if Books.query.get(book_id):
        if Clients.query.get(customer_id):
            for book in Books.query.filter(Books.id):
                if book_id == book.id:
                    # Setting automatic return date based on the type of loan of each book.
                    if book.typeofloan == 1: returndate = loandate + timedelta(days=10)
                    elif book.typeofloan == 2: returndate = loandate + timedelta(days=5)
                    elif book.typeofloan == 3: returndate = loandate + timedelta(days=2)
            new_loan = Loans(customer_id,book_id,loandate,returndate)   
            db.session.add(new_loan)
            db.session.commit()
            flash("New loan has been created.")
        # If client was not found in the Database it flashes on the site with the message.
        else: flash("Client not found.")
    # If book was not found Database it flashes on the site with the message.
    else: flash("Book not found.")
    return redirect("/loans")
    
# Function made to show all late loans that the return date of them has passed.
@loans.route('/late_loans', methods=['GET'])
def show_late_loans():
    late_loans = []
    active_loans = Loans.query.filter_by(returned= False)
    for loan in active_loans:
            # This line checks if the returndate of a specific loan is smaller than today's date.
            if loan.returndate < datetime.today().date():
                late_loans.append(loan)
    return render_template ("late_loans.html", late_loans=late_loans)

# Function made to return a book from the database based on the index (id) of the loan.
@loans.route("/loans_del", methods=['GET','DELETE'])
@loans.route("/loans_del/<ind>")
def return_loan(ind):
    loan = Loans.query.get(int(ind))
    # If the loan does not exist return to the endpoint that shows all loans.
    if loan is None:
        return render_template('loans.html', loans=Loans.query.all())
    try:
        db.session.delete(loan)
        db.session.commit()
    except:
        return render_template('loans.html', loans=Loans.query.all())
    return render_template('loans.html', loans=Loans.query.all())
    # After function is done running it will render the page that shows all loans.
