from project import db,app

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bookname = db.Column(db.String(30))
    author = db.Column(db.String(15))
    publishdate = db.Column(db.String(10))
    typeofloan = db.Column(db.Integer)
    loans = db.relationship('Loans', backref='books')

    def __init__(self,bookname,author,publishdate,typeofloan):
        self.bookname = bookname
        self.author = author
        self.publishdate = publishdate
        self.typeofloan = typeofloan
        
with app.app_context():
    db.create_all()
