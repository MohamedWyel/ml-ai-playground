from flask import Flask,render_template 

# Create a Flask application instance (WSGI application)
app = Flask(__name__)

#create a basic route
@app.route("/")
def welcome():
    #return "<html><body><h1>Hello, this is Flask!, welcome to my app.</h1></body></html>"
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)