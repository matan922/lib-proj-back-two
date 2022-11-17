from project import db,app

class Loans(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    loandate = db.Column(db.Date)
    returndate = db.Column(db.Date)
    returned = db.Column(db.Boolean, nullable=False)



    def __init__(self,customer_id,book_id,loandate,returndate):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loandate = loandate
        self.returndate = returndate
        self.returned = False

with app.app_context():
    db.create_all()
