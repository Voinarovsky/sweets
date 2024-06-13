from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3

app = Flask('pomogite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Feedback(dp.Model):
#     id = dp.Column(dp.Ineger, primary_key = True )
#     text = dp.Column(dp.String(500))
#     estimation = dp.Column(dp.Integer(5))
#     def __repr__(self):
#         return f'<Feedback {self.id} / {self.text}> {self.estimation}'

feedbacks = [
    {'id': 8383,
     'response': 'плохо',
     'estimation': 1},
    {'id': 8353,
     'response': 'плохо',
     'estimation': 2},
    {'id': 84533,
     'response': 'плохо',
     'estimation': 3}
    ]

@app.route('/')
def main():
    # feedbacks = Feedback.query.all()
    # print(feedbacks)
    return render_template('main.html', feedbacks_list = feedbacks)


@app.route('/estimation/<int:feedback_id>', methods = ['PATCH'])
def modify_feedback1(feedback_id):
    global feedbacks
    estimation = request.json['estimation']
    for feedback in feedbacks:
        if feedback['id'] == feedback_id:
            feedback.update({'estimation': estimation})
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
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)