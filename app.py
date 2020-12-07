from flask import Flask, render_template, request, redirect, url_for
from models import db, Questions, Result, User
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anketa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey', methods=['get'])
def question_page():
    questions = Questions.query.all()
    return render_template(
        'questinnaire.html',
        questions=questions
    )

@app.route('/process', methods=['POST', 'GET'])
def survey():
    gender = request.form['gender']
    age = request.form['age']

    user = User(
        gender=gender,
        age=age
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    ask = request.form['ask']
    ask2 = request.form['ask2']
    ask3 = request.form['ask3']
    ask4 = request.form['ask4']
    ask5 = request.form['ask5']
    ask6 = request.form['ask6']

    answer = Result(answers_id=user.person_id, ask=ask, ask2=ask2, ask3=ask3, ask4=ask4, ask5=ask5, ask6=ask6)
    db.session.add(answer)
    db.session.commit()
    return render_template('111.html')




@app.route('/rating', methods=['POST', 'GET'])
def stats():
    all_info = {}
    age_stats = db.session.query(
        func.avg(User.age),
        func.min(User.age),
        func.max(User.age)
    ).one()
    all_info['age_mean'] = age_stats[0]
    all_info['age_min'] = age_stats[1]
    all_info['total_count'] = User.query.count()
    return render_template("static.html", all_info=all_info)


if __name__ == '__main__':
    app.run(debug=True)