from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, url_for, request, render_template, redirect
import datetime

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def journal():
    jobs = []
    session = db_session.create_session()
    for i in session.query(Jobs).all():
        jobs.append((i.job,
                     i.leader.name,
                     i.leader.surname,
                     i.work_size,
                     i.collaborators,
                     i.if_finished))
    session.close()
    params = {}
    print(jobs)
    params["title"] = "Журнал работ"
    params["static_css"] = url_for('static', filename="css/")
    params["static_img"] = url_for('static', filename="img/")
    params["jobs"] = jobs
    return render_template("journal.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
