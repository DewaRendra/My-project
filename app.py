from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "11223344"

@app.route("/hai")
def index():
    flash("What's your name?")
    return render_template("Index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", greet to see you!" )
    return render_template("Index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)