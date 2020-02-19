from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV =='dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/wzim'
else: # ENV = 'prod'
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://idfbzevcayhqdo:849c97cd8e873964d5316d1f2e6a5c20bcb7932f9e7713a44da6a5d274d986a1@ec2-18-210-51-239.compute-1.amazonaws.com:5432/df9qekss66goub' # you get it from heroku for example

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # creating our database

#engine = create_engine("postgresql://postgres:123456@localhost/wzim", pool_pre_ping=True)

# The way SQLAlchemy works - we create models, therefore we make a class
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(50))
    teacher = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, student, teacher, rating, comments):
        self.student = student
        self.teacher = teacher
        self.rating = rating
        self.comments = comments
        # now we can make queries to our database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method =='POST':
        student = request.form['student'] # in brackets the name in html file 
        teacher = request.form['teacher']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(student, teacher, rating, comments)
        if student == '' or teacher =='':
            # flash('EJ EJ cos jest nietak', 'danger')
            return render_template('index.html', message='Wprowadz dane gapciu')
        if db.session.query(Feedback).filter(Feedback.student == student).count() < 5:
            # adding data to our table
            data = Feedback(student, teacher, rating, comments)
            db.session.add(data)
            db.session.commit()
            #send_mail(student, teacher, rating, comments)
            return render_template('succes.html')
        return render_template('index.html', message=f'Juz submitnales feedback dla {teacher}')

if __name__ == '__main__':
    app.run()