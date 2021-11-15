from sqlite3.dbapi2 import IntegrityError
from flask import *
import random
from db_access import *

def simulation(P):
    p = random.random()
    if p <= P:
        return 200
    else:
        q = random.random()
        if q <= 1/3:
            return 600
        else:
            return 0

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("consentForm.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/exp/demographics', methods = ['GET', 'POST'])
def exp_demographics():
    if request.method == "POST":
        if request.form['radio1'] == "no" or request.form['radio2'] == "no" or request.form['radio3'] == "no":
            return redirect(url_for('invalid'))
    return render_template("demographicsInfo.html", redirect_to="exp_sampling", sid=db.exp_sid)

@app.route('/desc/demographics', methods = ['GET', 'POST'])
def desc_demographics():
    if request.method == "POST":
        if request.form['radio1'] == "no" or request.form['radio2'] == "no" or request.form['radio3'] == "no":
            return redirect(url_for('invalid'))
    return render_template("demographicsInfo.html", redirect_to="desc_allocate", sid=db.desc_sid)

@app.route('/exp/sampling', methods = ['GET', 'POST'])
def exp_sampling():
    people_saved = -1
    if request.method == "POST":
        try:
            program = request.form['program']
            P = 1 if program == 'a' else 0
            people_saved = simulation(P)
            record = (db.exp_sid,
                    program,
                    people_saved)
            db.insertSample(record)
        except:
            record = (request.form["age"],
                request.form["gender"],
                request.form["education"],
                request.form["major"],
                request.form["occupation"],
                request.form["marital_status"],
                request.form["annual_income"])
            db.insertDemo(record, "exp_demo")
    return render_template("sampling.html", people_saved=people_saved)

@app.route('/exp/allocate', methods = ['GET', 'POST'])
def exp_allocate():
    return render_template("exp_allocate.html")

@app.route('/desc/allocate', methods = ['GET', 'POST'])
def desc_allocate():
    if request.method == "POST":
        record = (request.form["age"],
            request.form["gender"],
            request.form["education"],
            request.form["major"],
            request.form["occupation"],
            request.form["marital_status"],
            request.form["annual_income"])
        db.insertDemo(record, "desc_demo")
    return render_template("desc_allocate.html")

@app.route('/desc/outcome', methods = ['GET', 'POST'])
def desc_outcome():
    people_saved = 0
    if request.method == "POST":
        P = int(request.form['proportion'])/100
        people_saved = simulation(P)

        record = (db.desc_sid,
                request.form["proportion"],
                request.form["preference"],
                people_saved)
        db.insertOutcomes(record, "desc_outcomes")
    return render_template("outcome.html", people_saved = people_saved)

@app.route('/exp/outcome', methods = ['GET', 'POST'])
def exp_outcome():
    people_saved = 0
    if request.method == "POST":
        P = int(request.form['proportion'])/100
        people_saved = simulation(P)

        record = (db.exp_sid,
                request.form["proportion"],
                request.form["preference"],
                people_saved)
        db.insertOutcomes(record, "exp_outcomes")
    return render_template("outcome.html", people_saved = people_saved)

@app.route('/invalid', methods = ['GET', 'POST'])
def invalid():
    return render_template("invalid.html")

if __name__ == '__main__':
    app.run(debug=False)
