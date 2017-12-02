import sys
from flask import Flask, jsonify
sys.path.append("./src/")

from analysis import Mor_analysis

app = Flask(__name__)


@app.route("/")
def index():
    """ テスト用のHello World! """
    return "Hello World!"


@app.route("/rhyme/<text>")
def rhyme_words(text):
    """ jsonで韻を踏んでいそうな単語を返してくれる """
    mor = Mor_analysis(text)

    words = {"text": mor.make_text()}
    if words["text"] == "":
        words = {"text": None}

    return jsonify(words)


if __name__ == "__main__":
    app.run()
