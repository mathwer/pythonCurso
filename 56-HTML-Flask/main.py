from flask import Flask, render_template

#Usando o https://html5up.net/aerial

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
#Para funcionar a renderização do arquivo html, ele tem que estar dentro
#da pasta templates, no diretório do projeto


app.run(debug=True)