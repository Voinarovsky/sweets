import dp as dp
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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

@app.route('/')
def main():
    feedbacks = Feedback.query.all()
    print(feedbacks)
    return render_template('main.html', feedback_list = feedback)

@app.route('/ready/<int: feedbac_id>', methods = ['PATCH'])
def modify_feedback(feedback_id):
    global feedbacks
    ready = request.json['ready']
    for feedback in feedbacks:
        if feedback['id'] == feedback_id:
            feedback.update({'ready': ready})
    return ' '


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)