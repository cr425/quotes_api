from flask import Flask, jsonify ,request, render_template

import random

from quotes import funny_quotes

app = Flask(__name__)

@app.route("/api/funny")
def serve_funny_quote():
    user = "crystal"
    quotes = funny_quotes()
    nr_of_quotes = len(quotes)
    selected_quote = quotes[random.randint(0, nr_of_quotes - 1)]['quote']

    return render_template('hello.html', name = user, quote = selected_quote)

@app.route("/<usr>")
def home(usr):
    return render_template('hello.html', name=usr)

@app.route("/login/<usr>", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "post"
    else:
        return "GET"

if __name__ == "__main__": 
    app.run(debug=True)