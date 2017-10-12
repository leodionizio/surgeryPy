# -*- coding: utf-8 -*-#
import json
from route import __user__ as user
from flask import Flask
import flask_cors

__app__ = Flask(__name__)
__app__.register_blueprint(user)
flask_cors.CORS(__app__)


@__app__.route('/', methods=['GET'])
def index():
    """ Rota root da API """
    data = {
        "name": "Douglas",
        "nickname": "DougTQ",
        "nationality": "Brazilian",
        "age": 21
    }

    reply = __app__.response_class(
        response=json.dumps(data), status=202, mimetype='__app__lication/json')
    # reply = make_response(jsonify(dicc), 202)
    return reply


if __name__ == '__main__':
    __app__.run(port=5000, debug=False, host='localhost', use_reloader=True)
