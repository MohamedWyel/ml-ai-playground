from flask import Flask as flask
# Create a Flask application instance (WSGI application)
app = flask(__name__)

#create a basic route
@app.route("/")
def welcome():
    return "Hello, this is Flask!, welcome to my app."

@app.route("/about")
def about():
    return "This is a simple Flask application descripiton and i'm trying to do something amazing."

if __name__ == "__main__":
    app.run(debug=True)