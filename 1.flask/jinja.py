## building URL dynamically , variable Rules in jinja template , jinja 2 template engine 
'''
{{ }}  --> to print output in html
{% %}  --> to write logic in html(for loop, if else etc)
{# #}  --> to write single line comments in html
'''
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def welcome():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form.get('data')
        return f"Form submitted! Hello, {data}."
    return render_template("submit.html")

#variable Rules in URL
@app.route("/user/<username>")
def user_profile(username):
    name = username
    name = name.upper()
    return render_template("profile.html", profile_name =name)

@app.route("/score/<int:mark>")
def success(mark):
    score = mark
    if score >= 50:
        msg = " You passed the exam!"
    else:
        msg = " You failed the exam."
    exp = {"score": mark ,"res" : msg}
    return render_template("result.html", results=exp)

# if condition case
@app.route("/checkIf/<int:num>")
def check_number(num):
    return render_template("check.html", number=num)

# URL_for
@app.route("/fail/<int:n>")
def fail(n):
    score = n
    if score < 50:
        msg = " You failed the exam."
    else:
        msg = " You passed the exam!"
    exp = {"score": n ,"res" : msg}
    return render_template("result.html", results=exp)

@app.route("/getResults" , methods=['GET', 'POST'])
def get_result():
    total_score = 0
    if request.method == 'POST':
        score1 = int(request.form.get('score1'))
        score2 = int(request.form.get('score2'))
        score3 = int(request.form.get('score3'))
        total_score = score1 + score2 + score3
        return redirect(url_for('fail', n=total_score))
    return render_template("getResults.html")

if __name__ == "__main__":
    app.run(debug=True)