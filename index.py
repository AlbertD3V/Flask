from flask import Flask

app = Flask(__name__)
@app.route('/cardapio')
def ola():
    return '<h1> Flask -> </h1>'

@app.route('/pizza')

app.run(debug=True)