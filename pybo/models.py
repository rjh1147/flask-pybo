from pybo import db

class Question(db.Model):    
    id_seq = db.Sequence('QUESTION_SEQ_ID')
    id = db.Column(db.Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id_seq = db.Sequence('ANSWER_SEQ_ID')
    id = db.Column(db.Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set', ))
    content = db.Column(db.Text(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)