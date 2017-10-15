# -*- coding: utf-8 -*-#

# from os import getenv as getenv
import json
import pymssql
from flask import make_response
class Mssql:
    """ Classe MSSQL """

    def __init__(self, host, port, user, password, database, commit):
        """ Conexão do Banco MSSQL """
        self.server = 'SQLHOST,1433'
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.commit = commit
        self._conn_ = None

    def query(self, script):
        """ Monta querys Mssql """
        cursor = self._conn_.cursor()
        cursor.execute(script)
        if self.commit:
            return self._conn_.commit()
        else:
            rows = cursor.fetchall()
            return rows

    def querycommit(self, script, params):
        """ Monta querys Mssql """
        try:
            cursor = self._conn_.cursor()
            if self.commit:
                cursor.execute(script,params)
                self._conn_.commit()
        except BaseException as (err):
            print err
            response = {"message": "Falha"}
            return make_response(json.dumps(response), 500)

    def __conexao__(self):
        """ Conexão do Banco MSSQL """
        try:
            _conn_ = pymssql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='UTF-8')
            print('Sucesso na conexão a instância de MSSQL!!')

            self.setconn(_conn_)

            return _conn_

        except BaseException as (err):
            print(err)
            return make_response('Erro na conexão', 404)

    def setconn(self, conn):
        """ Seta o valor da _conn_ """
        self._conn_ = conn

    
    def setcommit(self, commit):
        """ Seta o valor da _conn_ """
        self.commit = commit