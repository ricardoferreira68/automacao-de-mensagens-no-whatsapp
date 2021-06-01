import psycopg2

class Conexao(object):

    def __init__(self, host, db, usuario, senha):
        self._db = psycopg2.connect(host=host, database=db, user=usuario,  password=senha)
    def manipular(self, sql, vars=None):
        try:
            cur=self._db.cursor()
            cur.execute(sql,vars)
            cur.close()
            self._db.commit()
        except:
            return False
        return True
    
    def consultar(self, sql, vars=None):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql,vars)
            rs=cur.fetchall()
        except:
            return None
        return rs

    def fechar(self):
        self._db.close()
