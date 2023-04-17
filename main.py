import random

from flask import Flask
app = Flask(__name__)
def bold(function):
    def result():
        return f"<b>{function()}</b>"
    return result
def emphasis(function):
    def result():
        return f"<em>{function()}</em>"
    return result
def underline(function):
    def result():
        return f"<u>{function()}</u>"
    return result
def high():
    return "<h2 style='color: red;'>It's too high</h2> <br> <iframe src='https://giphy.com/embed/3o6ZtaO9BZHcOjmErm' width='480' height='453' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
def low():
    return "<h2 style='color:gray;'>It's too low</h2> <br> <iframe src='https://giphy.com/embed/jD4DwBtqPXRXa' width='384' height='480' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
def correct():
    return "<h2 style='color:green;'>you are correct</h2><iframe src='https://giphy.com/embed/4T7e4DmcrP9du' width='458' height='480' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"


@app.route("/")
def hello_word():
    return "guess a number"
@app.route("/<num>")
def check(num):
    num = int(num)
    if num == kp:
        return correct()
    elif num<kp:
        return low()
    elif num>kp:
        return high()


if __name__== "__main__":
    kp = random.randint(1, 9)
    app.run(debug=True)

