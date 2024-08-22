from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hola, Mundo!'

if __name__ == '_main':
    app.run(debug=True)