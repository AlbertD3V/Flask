from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def ola():
    return render_template('cardapio.html')

@app.route('/pizza')
def pizza():
    return render_template('pizza.html')

@app.route("/hamburguer")
def hamburguer():
    return render_template('hamburguer.html')

app.run(debug=True)