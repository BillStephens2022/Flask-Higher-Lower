from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route('/')
def home():
    return "<h1 style='color: blue'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route('/<int:guess>')
def guess():
    if guess > random_number:
        return "<h1 style='color: violet'>Too High! Try Again...</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too Low! Try Again...</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>That's Correct!!  Nice Job!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
