#!/bin/python
from flask import Flask, render_template

app = Flask(__name__)

HELLO_MESSAGE = "hello funny world!!"

@app.route("/")
def helloworld():
   return render_template("index.html", message=HELLO_MESSAGE)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
