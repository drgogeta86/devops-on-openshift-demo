import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/1.0/welcome", methods=['GET'])
def welcome():
    response = {
        'message': os.getenv("WELCOME_MESSAGE", default="Hello World!")
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run()
