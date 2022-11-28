from . import db

class maths(db.Model):
    __tablename__ = "maths"
    qid = db.Column(db.Integer, primary_key=True)
    subject =db.Column(db.String, nullable=False)
    question =db.Column(db.String, nullable=False)
    option1 = db.Column(db.String, nullable=True)
    option2 = db.Column(db.String, nullable=True)
    option3 = db.Column(db.String, nullable=True)
    option4 = db.Column(db.String, nullable=True)
    answer = db.Column(db.Integer, nullable=True)
    bcol = db.Column(db.String, nullable=True)  

    def __repr__(self):
        return f'< maths {self.subject}>' 


class science(db.Model):
    __tablename__ = "science"
    qid = db.Column(db.Integer, primary_key=True)
    subject =db.Column(db.String, nullable=False)
    question =db.Column(db.String, nullable=False)
    option1 = db.Column(db.String, nullable=True)
    option2 = db.Column(db.String, nullable=True)
    option3 = db.Column(db.String, nullable=True)
    option4 = db.Column(db.String, nullable=True)
    answer = db.Column(db.Integer, nullable=True)
    bcol = db.Column(db.String, nullable=True)  

    def __repr__(self):
        return f'< science {self.subject}>' 
