from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this Flask course"

@app.route("/index")
def welcome_index():
    return "Vamos beber"

if __name__=="__main__":
    app.run(debug=True)
