from flask import Flask, render_template
import random

app = Flask(__name__)

def generate_random_text():
    list_of_text = [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]
    return random.choice(list_of_text)

@app.route("/")
def home():
    return render_template("index.html", random_text=generate_random_text())

if __name__ == '__main__':
    app.run(debug=True, port=8000)