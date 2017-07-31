# -*- coding: utf-8 -*-#
from flask import make_response, Flask, flask_cors
from flask_cors import CORS
#import config.database.Database as data

App = Flask(__name__)
CORS(App)

#data.Database.conn();

@App.route('/', methods=['GET'])
def index():
    return make_response('Funcionando!', 204)


if __name__ == '__main__':
    App.run(port=5000, debug=False, host='localhost', use_reloader=True)
