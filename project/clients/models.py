from project import db,app

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    clientname = db.Column(db.String(15))
    age = db.Column(db.Integer)
    city = db.Column(db.String(15))
    loans = db.relationship('Loans', backref='clients')

    def __init__(self,clientname,age,city):
        self.clientname = clientname
        self.age = age
        self.city = city

with app.app_context():
    db.create_all()
