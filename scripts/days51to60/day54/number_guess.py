from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Guess a number between 0 and 9 </h1>" \
           "<p>Add this to the end of the url</p>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'>"


number_chosen = random.randint(0, 9)


@app.route('/<int:number>')
def number_check(number):
    if number < number_chosen:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/Yycc82XEuWDaLLi2GV/giphy.gif' width=400>"
    if number > number_chosen:
        return "<h1 style='color: red'>Too high, try again!<h1>" \
               "<img src='https://media.giphy.com/media/poJG2ByUaYi88/giphy.gif' width=400>"
    if number == number_chosen:
        return "<h1 style='color: green'>That's correct, well done! </h1>" \
               "<img src='https://media.giphy.com/media/kmtKmZEQ9LM1iYm167/giphy.gif' width=400>"


if __name__ == "__main__":
    app.run(debug=True)
