# -*- coding: utf-8 -*-#
""" Json da response """
import json

from flask import Blueprint, make_response

from database import Mssql

__user__ = Blueprint('user', __name__)


@__user__.route('/user', methods=['GET'])
def create():
    """ Criacao de usuario """
    db = Mssql("localhost", 1433, "sa", 
    "FocusAdmin7539", "SURGERY", True)
    conexao = db.__conexao__()
    payload = db.query(conexao, 'Select * from users')
    reply = []
    for row in payload:
        data = {
            "data" : {
                "id": row[0],
                "nome": row[1],
                "usuario": row[2],
                "email": row[3],
                "senha": row[4]
            }
        }
        reply.append(data)
        
    reply = make_response(json.dumps(reply), 200)

    return reply