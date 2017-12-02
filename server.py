import json
import sys
from flask import Flask, jsonify
sys.path.append("./src/")

from rhyme import rhymes

app = Flask(__name__)


@app.route("/")
def index():
    """ テスト用のHello World! """
    return "Hello World!"


@app.route("/rhyme/<text>")
def rhyme_words(text):
    """ jsonで韻を踏んでいそうな単語を返してくれる """
    words = {i: j for i, j in enumerate(rhymes(text))}

    return jsonify(words)



if __name__ == "__main__":
    app.run()
