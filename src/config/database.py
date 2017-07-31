from os import getenv as getenv
import json
import pymssql
import pymongo
from flask import make_response


class connectMssql:
    def conn(self, commit):
        try:
            pymssql.set_max_connections(5)
            _conn_ = pymssql.connect(host='', user='', password='', database='CENTRO_CIRURGICO', as_dict=True)
            self._cursor_ = _conn_.cursor()
            print('Sucesso na conexão a instância de MSSQL!!')

            if commit:
                self._conn = _conn_
                return self._conn
            else:
                return self._cursor_

        except BaseException as (err):

            print('Erro:' + err)
            return make_response('Erro na conexão', 404)
