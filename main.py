from flask import Flask, render_template, url_for
from data import db_session
from data.jobs import Jobs
from data.users import User


app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)
    return render_template('index.html', jobs=jobs)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
