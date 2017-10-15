# -*- coding: utf-8 -*-#
""" Json da response """
import json

from flask import Blueprint, make_response, request

from database import Mssql

__user__ = Blueprint('user', __name__)


@__user__.route('/user', methods=['GET'])
def getallusers():
    """ Get de usuarios """
    _db = Mssql("localhost", 1433, "sa", "FocusAdmin7539", "SURGERY", False)
    _db.__conexao__()
    payload = _db.query('Select * from users')

    reply = {"error": False, "code": 200}
    data = list()
    for row in payload:
        user = {
            "id": row[0],
            "nome": row[1],
            "usuario": row[2],
            "email": row[3],
            "senha": row[4]
        }
        data.append(user)
    reply["data"] = data
    reply = make_response(json.dumps(reply), 200)

    return reply


@__user__.route('/user', methods=['POST'])
def createuser():
    """ Criacao de usuario """

    _db = Mssql("localhost", 1433, "sa", "FocusAdmin7539", "SURGERY", True)
    _db.__conexao__()
    script = "INSERT INTO users (nome, usuario, email, password) VALUES(%s, %s, %s, %s) "
    params = (request.form["nome"], request.form["usuario"],
              request.form["email"], request.form["password"])
    _db.querycommit(script, params)

    response = {"message": "Sucesso"}

    return make_response(json.dumps(response), 202)
