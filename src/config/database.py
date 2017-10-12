# from os import getenv as getenv
# import json
import pymssql 
from flask import make_response


class Mssql:
    """ Classe MSSQL """    
    def __init__(self, host, user, password, database, commit):
        """ Conexão do Banco MSSQL """    
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.commit = commit       
        

    def conexao(self):    
        """ Conexão do Banco MSSQL """    
        try:
            _conn_ = pymssql.connect(self.host, self.user, self.password, self.database, True)
            _cursor_ = _conn_.cursor()
            print('Sucesso na conexão a instância de MSSQL!!')

            if self.commit:
                return _conn_
            else:
                return _cursor_

        except BaseException as (err):
            print('Erro:' + err)
            return make_response('Erro na conexão', 404)
