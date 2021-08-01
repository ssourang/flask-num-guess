from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 9)

@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1'

@app.route('/<int:number>')
def guess(number):
    if number < random_number:
        return f'<h1 style="color: blue">Too low</h1>' \
               f'<img src="https://media.giphy.com/media/3ohk6AkkOXXeaC0bjq/giphy.gif"/>'
    elif number > random_number:
        return f'<h1 style="color: red">Too high</h1>' \
               f'<img src="https://media.giphy.com/media/3ohk6AkkOXXeaC0bjq/giphy.gif"/>'
    else:
        return '<h1 style="color: green">This is the correct number</h1>' \
               '<img src="https://media.giphy.com/media/3ohk6AkkOXXeaC0bjq/giphy.gif"/>'



if __name__ == '__main__':
    app.run(debug=True)

