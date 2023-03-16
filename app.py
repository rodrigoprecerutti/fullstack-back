from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main():

    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')

    nota1 = float(nota1)
    nota2 = float(nota2)

    media = (nota1 + nota2) / 2

    return f'{media:.1f}'


if __name__ == '__main__':
    app.run(debug=True)
