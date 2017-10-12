# -*- coding: utf-8 -*-#

# from os import getenv as getenv
# import json
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

    def query(self, conn, script):
        """ Monta querys Mssql """
        cursor = conn.cursor()
        cursor.execute(script)
        payload = cursor.fetchall()
        # print(payload)
        return payload

    def __conexao__(self):
        """ Conexão do Banco MSSQL """
        try:
            _conn_ = pymssql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)
            print('Sucesso na conexão a instância de MSSQL!!')

            self._conn_ = _conn_

            return _conn_

        except BaseException as (err):
            print(err)
            return make_response('Erro na conexão', 404)

    def setConn(self, conn):
        self._conn_ = conn