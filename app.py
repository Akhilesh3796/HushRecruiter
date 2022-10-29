from flask import Flask, render_template, request, session
from flask_mail import Mail, Message
from utilities.candidateSelection import CandidateSelection
from utilities.question_update import Question_Update
from utilities.questions import Questions
from datetime import timedelta
import os.path
import sys

app = Flask(__name__, instance_relative_config=True)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "maxmustermannjob.de@gmail.com",
    "MAIL_PASSWORD": "dummYmaxde#02"
}

app.config["CACHE_TYPE"] = "null"
app.config.update(mail_settings)
mail = Mail(app)

user = ''

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loading", methods=['POST'])
def renderLoadingpage():
    return render_template("loading.html")

@app.route("/success")
def success():
    text = ""
    c = CandidateSelection()
    c.csv_load_to_df()
    c.selection()
    c.selection_Hireable()
    c.selection_Reputation()
    c.selection_repo()
    c.selection_date()
    a = c.selection_tweet()
    if a:
        text = "Worthy one's has been chosen."
        # email.sendEmail("maxmustermannjob.de@gmail.com")
        for i in range(0, len(a)):
            bulk_mail(a[i])
        return render_template("success.html", message = text)
    else:
        return render_template("index.html")

@app.route("/send-email")
def bulk_mail(user):
    # Get all users first
    with app.app_context():
        # for user in users:
        msg = Message(subject="HushHush Recruiter has a code challenge for you!",
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=["maxmustermannjob.de@gmail.com"])
        # pass dynamically the user to the template
        msg.html = render_template('emailSend.html', user = user)
        mail.send(msg)

@app.route("/codeChallenge/<string:user_id>")
def codeChallenge(user_id):
    user = user_id
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
    return render_template('codeEditor.html', user = user)

@app.route("/submissionDone/<string:user_id>", methods=['POST'])
def submissionDone(user_id):
    submit = Question_Update()
    questions = Questions()
    user = user_id
    question1= questions.question1
    question2= questions.question2
    question3= questions.question3
    question = [question1, question2, question3]
    answer = request.form.get("text")
    submit.update(user, question, answer)
    return render_template('submissionSuccess.html', user = user)

@app.route("/timeoutSubmission/<string:user_id>")
def timeoutSubmission(user_id):
    return render_template('timeoutSubmission.html', user = user)

if __name__ == "__main__":
    app.run(port=4998, debug=True)
