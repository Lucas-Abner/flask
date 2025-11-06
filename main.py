from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to this Flask course</h1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return "<html><h1>About Page</h1></html>"

@app.route("/form", methods=["GET", "POST"])
def form():
    return render_template("form.html")

@app.route("/success/<score>")
def success(score):
    return f"<h1>Your score is: {score}</h1>"


"""
Existe algumas maneiras de definir o tipo de dado que sera passado para o template de Jinja2.

No HTML , passamos podemos passar os valores
{{ ... }} Para expressões
{% ... %} Para instruções de controle (loops, condicionais)
{# ... #} Para comentários
"""

# Aqui fizemos a passagem do tipo int para o score variavel no route e no html passamos a variavel results {{ results }} como string
@app.route("/success/<int:score>")
def success_int(score):
    
    res = ""

    if score>50:
        res="PASS"
    else:
        res="FAIL"

    return render_template("result.html", results=res)

@app.route("/successres/<int:score>")
def success_res(score):
    res = ""

    if score>50:
        res="PASS"
    else:
        res="FAIL"

    exp={"score": score, "res": res}

    return render_template("result.html", results=exp)

@app.route("/successif/<int:score>")
def success_if(score):

    return render_template("resultif.html", results=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template("resultif.html", results=score)


@app.route("/submit", methods=["POST", "GET"])
def formres():
    total = 0
    if request.method == "POST":
        math = float(request.form["math"])
        datascience = float(request.form["datascience"])
        science = float(request.form["science"])
        english = float(request.form["english"])

        total = (math + datascience + science + english)/4
    return redirect(url_for("success_res", score=total))

if __name__=="__main__":
    app.run(debug=True)