from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3

app = Flask('pomogite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Feedback(dp.Model):
    id = dp.Column(dp.Ineger, primary_key = True )
    text = dp.Column(dp.String(500))
    estimation = dp.Column(dp.Integer(5))
    def __repr__(self):
        return f'<Feedback {self.id} / {self.text}> {self.estimation}'

feedbacks = [
    {'id': 8383,
     'response': 'плохо',
     'estimation1': False,
     'estimation2': False,
     'estimation3': False},
    {'id': 8353,
     'response': 'плохо',
     'estimation1': False,
     'estimation2': False,
     'estimation3': False},
    {'id': 84533,
     'response': 'плохо',
     'estimation1': False,
     'estimation2': False,
     'estimation3': False}
    ]

@app.route('/')
def main():
    # feedbacks = Feedback.query.all()
    # print(feedbacks)
    return render_template('main.html', feedbacks_list = feedbacks)


@app.route('/estimation1/<int:feedback_id>', methods = ['PATCH'])
def modify_feedback1(feedback_id):
    global feedbacks
    estimation1 = request.json['estimation1']
    for feedback in feedbacks:
        if feedback['id'] == feedback_id:
            feedback.update({'estimation1': estimation1})
    return 'ok'

@app.route('/estimation2/<int:feedback_id>', methods = ['PATCH'])
def modify_feedback2(feedback_id):
    global feedbacks
    estimation2 = request.json['estimation2']
    for feedback in feedbacks:
        if feedback['id'] == feedback_id:
            feedback.update({'estimation2': estimation2})
    return 'ok'

@app.route('/estimation3/<int:feedback_id>', methods = ['PATCH'])
def modify_feedback3(feedback_id):
    global feedbacks
    estimation3 = request.json['estimation3']
    for feedback in feedbacks:
        if feedback['id'] == feedback_id:
            feedback.update({'estimation3': estimation3})
    return 'ok'
@app.route('/feedback', methods=['POST'])
def create_feedback():
    data = request.json
    last_id = feedbacks[-1]['id']
    new_id = last_id + 1
    data['id'] = new_id
    feedbacks.append(data)
    return 'ok'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)