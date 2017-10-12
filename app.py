# -*- coding: utf-8 -*-#
from flask import make_response, Flask, jsonify
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/', methods=['GET'])
def index():
    """ Rota root da API """
    dicc = {
        "name": "Douglas",
        "nickname": "DougTQ",
        "nationality": "Brazilian",
        "age": 21
    }
    reply = make_response(jsonify(dicc), 202)
    return reply


if __name__ == '__main__':
    app.run(port=5000, debug=False, host='localhost', use_reloader=True)
